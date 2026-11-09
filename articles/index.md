---
# 主题把 title 显示成页面大标题，正文里就不再写一级标题
title: "文章 Articles"
# 主题把 classes 加到 <body> 的 class 上。页头导航的"中文 / English"指向首页的两个小标题，
# 在这一页没有意义，_includes/head/custom.html 里按这个 class 把它藏掉
classes: hide-site-nav
---

- [读《通往奴役之路》的一点感受](./The-road-to-serfdom/index.html) · 中文 · 2026年11月  
  读完哈耶克《通往奴役之路》的感受：中文世界对这本书的几处常见误读，书里的 socialism 到底指什么，还有我和 Bruce Caldwell 的通信。  
  Notes on Hayek's _The Road to Serfdom_: common misreadings of the book in the Chinese-speaking world, what Hayek meant by socialism, and my emails with Bruce Caldwell (in Chinese).

- [PyTorch Crash Course (Part 1)](./pytorch-primer/index.html) · English · 2026年10月  
  市面上那些 PyTorch 书和文章绝大多数在回答**另一个问题**：怎么从零造一个模型、并把它训出来，而我这篇文章针对的是已经实际部署和使用了各种基于PyTorch的模型，但对PyTorch本身还不了解的人。  
  For people who deploy models but never learned the framework underneath because almost all of the PyTorch books and articles out there answer **a different question**: how to build a model from scratch and train it.

- [I Documented Claude's Every Decision. Then I Reviewed It with Claude.](./vibe-coding/index.html) · English · 2026年5月  
  我一次 vibe coding 经历的完整记录：五个会话，代码全部由 Claude 写。  
  A full record of one vibe coding project: five sessions, all code written by Claude.

- [Birth of the Monkey King](./monkey-king-story/index.html) · English · 2025年5月（2026年4月补充 Epilogue）  
  图画书《美猴王》的文字版，忠实于《西游记》原著情节。  
  The text of my picture book, faithfully following the narrative of _Journey to the West_.

- [选什么样的话题能快速识别GPT们是不是在胡说八道](./llm-hallucination-2024/index.html) · 中文 · 2024年1月  
  怎么用几道题快速鉴定大模型是不是在胡说八道。  
  How to tell quickly, with a few questions, whether an LLM is making things up (in Chinese).

- [Flying the Hump · 飞越驼峰](./flying-hump-2016/index.html) · 中英对照 · 2023年12月  
  飞虎队、驼峰航线的历史，英文原文和我的中文翻译对照。  
  The history of the Flying Tigers and the Hump, English original and my Chinese translation side by side.

- [My take on the ending of _Endurance: Shackleton's Incredible Voyage_ by Alfred Lansing](./shackleton/index.html) · English · 2022年11月  
  Lansing 的《Endurance》结尾一句"Some said that Sørlle turned away and wept"一直让我想不通。我对照沙克尔顿和沃斯利本人的记述，查这句话是从哪儿来的。  
  Lansing's _Endurance_ ends with "Some said that Sørlle turned away and wept." I checked it against what Shackleton and Worsley wrote themselves to find where the line came from.

<!-- 全站访问量，数据来自 GoatCounter（需在 GoatCounter 设置里打开 "Allow adding visitor counts on your website"）。
     只放在"读书笔记"和"文章"两个目录页。数字最多有 4 小时延迟；访问量不到 100 或读取失败时不显示 -->
<p id="site-visits" hidden><span>访问量 Visitors</span><strong>…</strong></p>
<script>
  fetch('https://qiulang.goatcounter.com/counter/TOTAL.json')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) {
      // count 是带千位分隔符的字符串，如 "1,234"
      if (parseInt(String(d.count).replace(/,/g, ''), 10) >= 100) {
        document.querySelector('#site-visits strong').textContent = d.count;
        document.getElementById('site-visits').hidden = false;
      }
    })
    .catch(function () {});
</script>
