#!/usr/bin/env python3
"""把一篇 Markdown 文章转成朗之文的文章页 index.html：
站点页头 + 标题区 + 两级目录 + 正文 + 页脚 + 回到顶部按钮，引用 ../site.css 和 style.css。

用法：
  python3 md2html.py 文章.md 输出/index.html --date 2026-11
  可选：--lang en（缺省 zh-CN） --subtitle "副标题" --layout css-h2 / standalone（缺省 articles）

需要 pandoc（-f gfm）。转换后自动处理 article-css skill 原则 19 里的几处：
  - md 的第一个 # 标题作为页面标题，放进标题区，不进正文；正文里还有别的 # 会提示
  - h2 编号 s1、s2…，h3 编号 s1-1、s1-2…，按这两级生成目录
  - 删掉 <hr>：article h2 自带上边线，再有 hr 就是两条线
  - 单独成段的 <p><img></p> 改成 <figure><img></figure>；
    图片夹在一段文字中间时，把段落从图片处断开，图片单独成一个 figure
  - 删掉表格行的 class="odd" / class="even"
  - 图片路径里的空格转成 %20（md 的图片路径有空格时 pandoc 不认）
  - 裸网址加尖括号：GFM 的自动链接一直延伸到空格，网址后面紧跟中文（如"）时"）会被一起吞进链接
  - 没被识别的 **加粗**：结尾的 ** 前面是标点、后面紧跟汉字时（"……。**哈耶克"），
    CommonMark 的规则不认它是加粗，转出来还是两个星号，这里补成 <strong>
  - articles 布局在 </body> 前加 GoatCounter 访问统计脚本（练习仓库和 standalone 不加）
"""
import argparse, html, re, subprocess, sys

# 页头里的路径和引用的样式表。
# articles：qiulang.github.io/articles/篇名/；css-h2：练习仓库/篇名/；
# standalone：单独一个目录，图标都在当前目录，只引一份完整的 style.css
LAYOUTS = {
    "articles":   dict(favicon="../../favicon.ico", site="../../index.html", logo="../logo-wide-song.svg",
                       home="../index.html", home_icon="../../nav-home.svg", css=["../site.css", "style.css"],
                       stats=True),
    "css-h2":     dict(favicon="../favicon.ico", site="../", logo="../logo-wide-song.svg",
                       home="../", home_icon="../nav-home.svg", css=["../site.css", "style.css"]),
    "standalone": dict(favicon="favicon.ico", site="index.html", logo="logo-wide-song.svg",
                       home="index.html", home_icon="nav-home.svg", css=["style.css"]),
}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("out")
    ap.add_argument("--date", required=True, help="发布年月，如 2026-11")
    ap.add_argument("--lang", default="zh-CN")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--layout", default="articles", choices=LAYOUTS)
    a = ap.parse_args()
    L = LAYOUTS[a.layout]
    zh = a.lang.startswith("zh")

    md = open(a.md, encoding="utf-8").read()
    # 图片路径里的空格转成 %20
    md = re.sub(r"(!\[[^\]]*\]\()([^)]*)\)", lambda m: m.group(1) + m.group(2).strip().replace(" ", "%20") + ")", md)
    # 裸网址加尖括号，只收 ASCII 字符，遇到中文标点就停（前面是 ( < " 的是已经写好的链接，不动）
    md = re.sub(r"(?<![(<\"])(https?://[A-Za-z0-9\-._~:/?#@!$&'*+,;=%]+)", r"<\1>", md)

    body = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=preserve"],
                          input=md, capture_output=True, text=True, check=True).stdout

    # 第一个 h1 是页面标题
    m = re.search(r"<h1[^>]*>(.*?)</h1>\n?", body)
    if not m:
        sys.exit("md 里没有 # 标题")
    title_html = m.group(1)
    body = body[:m.start()] + body[m.end():]
    if "<h1" in body:
        print("提示：正文里还有 # 一级标题，一页只留文章标题一个 h1，附录要整体降一级", file=sys.stderr)

    # 标题编号，同时收集目录
    toc, n2, n3 = [], 0, 0
    def number(m):
        nonlocal n2, n3
        level, inner = m.group(1), m.group(2)
        if level == "2":
            n2, n3 = n2 + 1, 0
            hid = f"s{n2}"
            toc.append([hid, inner, []])
        else:
            n3 += 1
            hid = f"s{n2}-{n3}"
            if toc:
                toc[-1][2].append([hid, inner])
        return f'<h{level} id="{hid}">{inner}</h{level}>'
    body = re.sub(r'<h([23])[^>]*>(.*?)</h\1>', number, body)

    body = re.sub(r"<hr\s*/?>\n?", "", body)                                    # 删 hr
    body = re.sub(r"<p>\s*(<img[^>]*>)\s*</p>", r"<figure>\1</figure>", body)    # 单独的图片 → figure
    def split_img(m, wrap_first=True):                                            # 段落中间的图片 → 断开
        parts = re.split(r"\s*(<img[^>]*>)\s*", m.group(1))
        out = []
        for i, part in enumerate(parts):
            if i % 2:
                out.append(f"<figure>{part}</figure>")
            elif part.strip():
                # 列表项里的第一段文字不包 <p>：和别的列表项写法一致。
                # 包了 <p> 的话，它缺省的上外边距会穿出 li，这一项和上一项的间距比别处大
                out.append(part if i == 0 and not wrap_first else f"<p>{part}</p>")
        return "\n".join(out)
    body = re.sub(r"<p>((?:(?!</p>).)*<img(?:(?!</p>).)*)</p>", split_img, body, flags=re.S)
    # 紧凑列表的 li 里文字不包 <p>，图片夹在中间时同样断开
    body = re.sub(r"<li>((?:(?!</li>|<li>|<p>|<ol|<ul).)*<img(?:(?!</li>|<li>|<ol|<ul).)*)</li>",
                  lambda m: "<li>" + split_img(m, wrap_first=False) + "</li>", body, flags=re.S)
    body = re.sub(r'<tr class="(odd|even)">', "<tr>", body)                      # 表格行的 class
    body = re.sub(r"\*\*([^*<>]+?)\*\*", r"<strong>\1</strong>", body)               # 没被识别的加粗

    def link(hid, inner):
        text = re.sub(r"</?a[^>]*>", "", inner)
        return f'<a href="#{hid}">{text}</a>'
    items = []
    for hid, inner, subs in toc:
        if subs:
            sub = "\n".join(f"                <li>{link(h, i)}</li>" for h, i in subs)
            items.append(f"            <li>{link(hid, inner)}\n              <ol>\n{sub}\n              </ol>\n            </li>")
        else:
            items.append(f"            <li>{link(hid, inner)}</li>")

    y, mo = a.date.split("-")[:2]
    shown = f"{y}年{int(mo)}月" if zh else f"{MONTHS[int(mo) - 1]} {y}"
    title_text = html.unescape(re.sub(r"<[^>]+>", "", title_html))
    subtitle = f'\n        <p class="subtitle">{html.escape(a.subtitle)}</p>' if a.subtitle else ""

    # 访问统计，只在后台 https://qiulang.goatcounter.com 看
    stats = ('\n    <!-- 访问统计（GoatCounter） -->'
             '\n    <script data-goatcounter="https://qiulang.goatcounter.com/count"'
             '\n            async src="//gc.zgo.at/count.js"></script>') if L.get("stats") else ""
    css_links = "\n".join(f'    <link rel="stylesheet" href="{c}" />' for c in L["css"])
    page = f"""<!doctype html>
<html lang="{a.lang}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title_text)}</title>
    <link rel="icon" href="{L['favicon']}" />
{css_links}
  </head>
  <body>
    <header>
      <a href="{L['site']}"><img src="{L['logo']}" alt="朗之文" width="84" height="32" /></a>
      <a href="{L['home']}"><img src="{L['home_icon']}" alt="{'文章首页' if zh else 'Articles'}" width="39" height="36" /></a>
    </header>
    <main>
      <header>
        <h1>{title_html}</h1>{subtitle}
        <p class="post-meta">
          {'发布于' if zh else 'First published'} <time datetime="{y}-{mo}">{shown}</time>
        </p>
      </header>
      <nav class="toc">
        <details open>
          <summary>{'目录' if zh else 'Contents'}</summary>
          <ol>
{chr(10).join(items)}
          </ol>
        </details>
      </nav>
      <article>
{body.strip()}
      </article>
    </main>
    <footer>
      <p>
        Copyright © {y} Lang Qiu (邱朗). This text is licensed under
        <a href="https://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a>.
      </p>
    </footer>
    <a class="to-top" href="#top" aria-label="{'回到顶部' if zh else 'Back to top'}">↑</a>{stats}
  </body>
</html>
"""
    open(a.out, "w", encoding="utf-8").write(page)
    print(f"写好 {a.out}：{len(toc)} 节，{sum(len(t[2]) for t in toc)} 个小节")


if __name__ == "__main__":
    main()
