/*
 * theory-page.js — renders a static "study notes" experiment page.
 *
 * Each theory HTML file calls `renderTheory({...})` with its own content.
 * This keeps the per-page HTML tiny and ensures every theory page has a
 * consistent layout matching the rest of the lab.
 */
(function (global) {
  "use strict";

  function el(tag, attrs, ...kids) {
    const e = document.createElement(tag);
    if (attrs) for (const k in attrs) {
      if (k === "style") e.setAttribute("style", attrs[k]);
      else if (k === "class") e.className = attrs[k];
      else e[k] = attrs[k];
    }
    kids.flat().forEach(k => e.append(k instanceof Node ? k : document.createTextNode(String(k))));
    return e;
  }

  function renderList(items, ordered) {
    const list = document.createElement(ordered ? "ol" : "ul");
    items.forEach(t => list.appendChild(el("li", null, t)));
    return list;
  }

  function renderTheory(cfg) {
    document.title = cfg.title + " — Virtual Chemistry Lab";
    document.body.innerHTML = "";

    const head = el("header", { class: "topbar" });
    head.innerHTML = `
      <div class="topbar-inner">
        <div class="brand">
          <div class="brand-logo">⚗</div>
          <div>
            <div class="brand-text">Virtual Chemistry Lab</div>
            <div class="brand-sub">${cfg.subtitle || cfg.title}</div>
          </div>
        </div>
        <nav><a href="../index.html">All experiments</a></nav>
      </div>`;
    document.body.appendChild(head);

    const main = el("main", { class: "container" });
    main.appendChild(el("div", { class: "crumbs", innerHTML:
      `<a href="../index.html">Library</a> &raquo; ${cfg.title}` }));
    main.appendChild(el("h1", { style: "margin:6px 0 4px" }, cfg.title));
    if (cfg.lede) main.appendChild(el("p", { style: "color:var(--muted);margin:0" }, cfg.lede));

    const layout = el("div", { class: "exp-layout" });

    // Left column: diagram + body sections
    const left = el("div");
    if (cfg.diagram) {
      const dia = el("div", { class: "diagram" });
      dia.innerHTML = cfg.diagram;
      left.appendChild(dia);
    }
    (cfg.sections || []).forEach(sec => {
      const p = el("div", { class: "panel", style: "margin-top:14px" });
      p.appendChild(el("h2", null, sec.heading));
      if (sec.body) {
        if (typeof sec.body === "string") p.appendChild(el("p", null, sec.body));
        else if (Array.isArray(sec.body)) sec.body.forEach(t => p.appendChild(el("p", null, t)));
      }
      if (sec.formula) {
        const f = el("div", { class: "formula" });
        f.innerHTML = sec.formula;
        p.appendChild(f);
      }
      if (sec.list)    p.appendChild(renderList(sec.list, false));
      if (sec.steps)   p.appendChild(renderList(sec.steps, true));
      left.appendChild(p);
    });
    layout.appendChild(left);

    // Right column: aside
    const right = el("aside");
    const aside = el("div", { class: "panel" });
    aside.appendChild(el("h2", null, cfg.asideTitle || "Why it matters"));
    if (cfg.aside) {
      if (typeof cfg.aside === "string") aside.appendChild(el("p", null, cfg.aside));
      else cfg.aside.forEach(t => aside.appendChild(el("p", null, t)));
    }
    if (cfg.questions) {
      aside.appendChild(el("h3", null, "Check your understanding"));
      aside.appendChild(renderList(cfg.questions, true));
    }
    right.appendChild(aside);
    layout.appendChild(right);

    main.appendChild(layout);
    document.body.appendChild(main);

    const foot = el("footer", { class: "site" });
    foot.textContent = "Virtual Chemistry Lab";
    document.body.appendChild(foot);
  }

  global.renderTheory = renderTheory;
})(window);
