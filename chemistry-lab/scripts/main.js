/*
 * main.js — renders the gallery on index.html
 *
 * Reads window.CHEM_EXPERIMENTS (from experiments.js), builds an interactive
 * grid with search + filter chips, and uses inline SVG thumbnails so the
 * site needs no external image assets.
 */

(function () {
  "use strict";

  const FILTERS = [
    { key: "all",         label: "All" },
    { key: "inquiry",     label: "Inquiry" },
    { key: "interactive", label: "Interactive" },
    { key: "3d",          label: "3D / Model" },
    { key: "demo",        label: "Demo Video" },
    { key: "theory",      label: "Study Notes" }
  ];

  // ----- Thumbnail generator -----------------------------------------------
  // Each thumbnail is a small SVG built on the fly from a hash of the id,
  // so every card looks distinct without bundling images.
  const PALETTES = [
    ["#4f8cff", "#29d3a0"],
    ["#ff5d6c", "#ffb347"],
    ["#7b61ff", "#29d3a0"],
    ["#ffb347", "#ff5d6c"],
    ["#29d3a0", "#4f8cff"],
    ["#6aa6ff", "#7b61ff"],
    ["#ffd166", "#ef476f"],
    ["#06d6a0", "#118ab2"],
    ["#f78c6b", "#ffd166"],
    ["#3a86ff", "#8338ec"]
  ];

  function hashStr(s) {
    let h = 0;
    for (let i = 0; i < s.length; i++) {
      h = (h * 31 + s.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  }

  function svgThumb(exp) {
    const h = hashStr(exp.id);
    const [c1, c2] = PALETTES[h % PALETTES.length];
    // Choose an icon glyph based on the badge/type
    const icon = pickIcon(exp);
    const initials = (exp.title.match(/[A-Z]/g) || ["C"]).slice(0, 2).join("");
    return `
      <svg viewBox="0 0 320 160" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="g-${exp.id}" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="${c1}" stop-opacity="0.85"/>
            <stop offset="100%" stop-color="${c2}" stop-opacity="0.85"/>
          </linearGradient>
          <radialGradient id="b-${exp.id}" cx="70%" cy="20%" r="80%">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="320" height="160" fill="url(#g-${exp.id})"/>
        <rect width="320" height="160" fill="url(#b-${exp.id})"/>
        <g opacity="0.92">${icon}</g>
        <text x="14" y="146" font-family="Inter, sans-serif" font-size="11"
              fill="rgba(255,255,255,0.85)" font-weight="600"
              letter-spacing="1.5">${initials.toUpperCase()}</text>
      </svg>
    `;
  }

  function pickIcon(exp) {
    // A small library of inline SVG glyphs sized to fit the thumb area.
    // The chosen icon is matched by keyword on title/formula.
    const t = (exp.title + " " + (exp.formula || "")).toLowerCase();
    if (/o[xs]ygen|kmno|kclo|h2o2|phosphor/.test(t)) return iconFlask("#fff");
    if (/iron|fe|metal|zn|cu|copper/.test(t))        return iconBars("#fff");
    if (/electrolys|water|h2o/.test(t))              return iconBubbles("#fff");
    if (/dust|explosion|fire|extinguisher/.test(t))  return iconFlame("#fff");
    if (/co2|carbon|ammonia|nh3|fountain/.test(t))   return iconBeaker("#fff");
    if (/atom|nucleus|gold foil|element/.test(t))    return iconAtom("#fff");
    if (/balanc|equation|conservation/.test(t))      return iconScale("#fff");
    if (/candle|flame|alcohol|sulfur|charcoal/.test(t)) return iconFlame("#fff");
    if (/distill|hard|soft|leak/.test(t))            return iconTube("#fff");
    if (/iodine|sublim|naoh|caoh|salt/.test(t))      return iconCrystal("#fff");
    if (/serpent|golden rain|smoke/.test(t))         return iconSparkle("#fff");
    return iconFlask("#fff");
  }

  // SVG glyph helpers — coordinates inside 320x160 viewBox
  function iconFlask(c) {
    return `<path d="M188 36h-56v22l-26 56c-6 13 3 28 18 28h72c15 0 24-15 18-28l-26-56V36z"
              fill="none" stroke="${c}" stroke-width="3"/>
            <path d="M132 84h56" stroke="${c}" stroke-width="2" stroke-dasharray="3 3"/>
            <circle cx="150" cy="108" r="4" fill="${c}" opacity=".7"/>
            <circle cx="170" cy="100" r="3" fill="${c}" opacity=".6"/>`;
  }
  function iconBeaker(c) {
    return `<path d="M118 38h84v18l-10 12v50c0 8-7 14-15 14h-34c-8 0-15-6-15-14V68l-10-12V38z"
              fill="none" stroke="${c}" stroke-width="3"/>
            <line x1="118" y1="38" x2="202" y2="38" stroke="${c}" stroke-width="3"/>
            <path d="M132 110h56" stroke="${c}" stroke-width="2" stroke-dasharray="3 3"/>`;
  }
  function iconAtom(c) {
    return `<g transform="translate(160 80)">
              <ellipse rx="46" ry="16" fill="none" stroke="${c}" stroke-width="2"/>
              <ellipse rx="46" ry="16" fill="none" stroke="${c}" stroke-width="2" transform="rotate(60)"/>
              <ellipse rx="46" ry="16" fill="none" stroke="${c}" stroke-width="2" transform="rotate(-60)"/>
              <circle r="6" fill="${c}"/>
            </g>`;
  }
  function iconFlame(c) {
    return `<path d="M160 38c12 18 24 28 24 48 0 18-14 34-32 34s-32-14-32-32c0-22 18-26 24-50 2 16 8 22 16 0z"
              fill="none" stroke="${c}" stroke-width="3"/>`;
  }
  function iconBars(c) {
    return `<g stroke="${c}" stroke-width="3" fill="none">
              <rect x="120" y="80" width="14" height="40"/>
              <rect x="146" y="60" width="14" height="60"/>
              <rect x="172" y="44" width="14" height="76"/>
              <rect x="198" y="70" width="14" height="50"/>
            </g>`;
  }
  function iconBubbles(c) {
    return `<g fill="none" stroke="${c}" stroke-width="2.5">
              <circle cx="140" cy="100" r="14"/>
              <circle cx="170" cy="76" r="10"/>
              <circle cx="190" cy="106" r="8"/>
              <circle cx="156" cy="60" r="6"/>
            </g>`;
  }
  function iconScale(c) {
    return `<g fill="none" stroke="${c}" stroke-width="3">
              <line x1="160" y1="40" x2="160" y2="118"/>
              <line x1="120" y1="60" x2="200" y2="60"/>
              <path d="M120 60l-16 28a18 18 0 0 0 32 0z"/>
              <path d="M200 60l-16 28a18 18 0 0 0 32 0z"/>
              <line x1="140" y1="118" x2="180" y2="118"/>
            </g>`;
  }
  function iconTube(c) {
    return `<g fill="none" stroke="${c}" stroke-width="3">
              <path d="M150 36v60a10 10 0 0 0 20 0V36z"/>
              <line x1="146" y1="36" x2="174" y2="36"/>
              <line x1="150" y1="80" x2="170" y2="80" stroke-dasharray="3 3"/>
            </g>`;
  }
  function iconCrystal(c) {
    return `<g fill="none" stroke="${c}" stroke-width="3">
              <polygon points="160,40 200,80 160,120 120,80"/>
              <line x1="160" y1="40" x2="160" y2="120"/>
              <line x1="120" y1="80" x2="200" y2="80"/>
            </g>`;
  }
  function iconSparkle(c) {
    return `<g fill="${c}">
              <path d="M160 44l4 14 14 4-14 4-4 14-4-14-14-4 14-4z" opacity=".95"/>
              <path d="M200 90l3 9 9 3-9 3-3 9-3-9-9-3 9-3z" opacity=".75"/>
              <path d="M122 100l2 7 7 2-7 2-2 7-2-7-7-2 7-2z" opacity=".75"/>
            </g>`;
  }

  // ----- Rendering --------------------------------------------------------

  function badgeText(b) {
    switch (b) {
      case "core":   return "Curriculum";
      case "fun":    return "Demo";
      case "ext":    return "Extension";
      case "theory": return "Theory";
      default:       return b;
    }
  }

  function renderFilters(activeKey, onChange) {
    const host = document.getElementById("filter-chips");
    host.innerHTML = "";
    FILTERS.forEach(f => {
      const el = document.createElement("button");
      el.type = "button";
      el.className = "chip" + (f.key === activeKey ? " active" : "");
      el.textContent = f.label;
      el.addEventListener("click", () => onChange(f.key));
      host.appendChild(el);
    });
  }

  function renderGrid(items) {
    const host = document.getElementById("grid");
    host.innerHTML = "";

    if (!items.length) {
      host.innerHTML = `<div class="panel" style="grid-column:1/-1;text-align:center;color:var(--muted)">
        No experiments match your filter.
      </div>`;
      return;
    }

    items.forEach(exp => {
      const a = document.createElement("a");
      a.className = "card";
      a.href = exp.file;
      a.setAttribute("data-id", exp.id);
      a.innerHTML = `
        <div class="thumb">${svgThumb(exp)}</div>
        <div class="body">
          <div class="title">${escapeHtml(exp.title)}</div>
          <div class="meta">
            <span class="badge ${exp.badge}">${badgeText(exp.badge)}</span>
            <span>${escapeHtml(exp.unit)}</span>
          </div>
        </div>
      `;
      host.appendChild(a);
    });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }

  // ----- Boot --------------------------------------------------------------
  document.addEventListener("DOMContentLoaded", () => {
    const list = window.CHEM_EXPERIMENTS || [];
    let filter = "all";
    let query = "";

    function apply() {
      const q = query.trim().toLowerCase();
      const items = list.filter(e => {
        const passFilter =
          filter === "all" ||
          (filter === "interactive" && (e.interactive === true || e.type === "interactive")) ||
          e.type === filter;
        const passQuery = !q ||
          e.title.toLowerCase().includes(q) ||
          (e.summary || "").toLowerCase().includes(q) ||
          (e.unit || "").toLowerCase().includes(q) ||
          (e.formula || "").toLowerCase().includes(q);
        return passFilter && passQuery;
      });
      renderGrid(items);
      const counter = document.getElementById("count");
      if (counter) counter.textContent = items.length;
    }

    renderFilters(filter, k => { filter = k; renderFilters(filter, arguments.callee); apply(); });
    // simpler stable wiring (avoid arguments.callee in strict mode):
    const filterHost = document.getElementById("filter-chips");
    filterHost.addEventListener("click", e => {
      const btn = e.target.closest(".chip");
      if (!btn) return;
      const label = btn.textContent.trim();
      const f = FILTERS.find(x => x.label === label);
      if (!f) return;
      filter = f.key;
      renderFilters(filter, () => {});
      apply();
    });

    const input = document.getElementById("search-input");
    input.addEventListener("input", () => { query = input.value; apply(); });

    document.getElementById("total").textContent = list.length;
    document.getElementById("interactive-count").textContent =
      list.filter(e => e.interactive === true || e.type === "interactive").length;

    apply();
  });
})();
