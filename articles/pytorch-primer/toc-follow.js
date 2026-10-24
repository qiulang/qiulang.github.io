/* 目录跟随（只有这一篇用：目录 51 项，比窗口高得多）
   宽屏时目录在左栏单独滚动（site.css 第六节：.toc details 设了 max-height 和 overflow-y: auto）。
   正文往下读，高亮的当前项会跑到目录可见区域外面。CSS 只能给当前项变色，
   不能让一个滚动区域自己滚，所以用这几行 JS：页面滚动停下后，把当前项挪回目录的可见区域。
   当前项直接用 CSS 的判断（:target-current），不另算一遍；
   浏览器不认识这个伪类（Safari、Firefox 目前不支持）时，什么都不做 */
(() => {
  const box = document.querySelector(".toc details");
  if (!box) return;
  let timer;

  function follow() {
    let cur;
    try {
      cur = box.querySelector("a:target-current");
    } catch {
      return;                                   // 不认识这个伪类，querySelector 会抛错
    }
    if (!cur) return;
    const b = box.getBoundingClientRect();
    const c = cur.getBoundingClientRect();
    const margin = 40;                          // 当前项上下各留一点，不贴着目录边缘
    if (c.top < b.top + margin) box.scrollTop -= b.top + margin - c.top;
    else if (c.bottom > b.bottom - margin) box.scrollTop += c.bottom - (b.bottom - margin);
  }

  // 浏览器更新"当前项"比 scroll / scrollend 事件晚一点（实测事件触发时拿到的还是上一项），
  // 所以等滚动停下 100 毫秒再对一次。滚动中每来一次事件就重新计时，停下来才真正执行
  addEventListener("scroll", () => {
    clearTimeout(timer);
    timer = setTimeout(follow, 100);
  }, { passive: true });
})();
