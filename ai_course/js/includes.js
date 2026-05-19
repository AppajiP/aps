/* Renders the shared navbar + footer used on every page.
   `data-base` on <body> says how to reach the course root from this page.
*/
(function () {
  const base = document.body.getAttribute("data-base") || "./";

  function navHTML() {
    return `
      <nav class="navbar">
        <div class="inner">
          <a class="brand" href="${base}index.html" aria-label="Azone Academy">
            <span class="brand-logo">AZ</span>
            <span>
              <div class="brand-title">Azone Academy</div>
              <div class="brand-sub">AI शिक्षण • मराठी • महाराष्ट्र राज्य मंडळ</div>
            </span>
          </a>
          <div class="nav-links">
            <a href="${base}index.html">मुख्यपृष्ठ</a>
            <a href="${base}syllabus.html">अभ्यासक्रम</a>
            <a href="${base}chapters/chapter01.html">धडे</a>
            <a href="${base}projects/index.html">प्रकल्प</a>
            <a href="${base}glossary.html">शब्दकोश</a>
            <a href="${base}about.html">आमच्याबद्दल</a>
            <button id="themeBtn" class="theme-toggle" onclick="toggleTheme()">☾  गडद</button>
          </div>
        </div>
      </nav>
    `;
  }

  function footerHTML() {
    const year = new Date().getFullYear();
    return `
      <footer class="footer">
        <div>
          <strong>Azone Academy</strong> &middot; AI अभ्यासक्रम (मराठी) &middot; महाराष्ट्र राज्य शिक्षण मंडळासाठी
        </div>
        <div class="mt-1">
          अभ्यासक्रम रचना: <strong>Appaji Patil</strong> &nbsp;|&nbsp;
          © ${year} Azone Academy. सर्व हक्क राखीव.
        </div>
        <div class="mt-1 text-muted">
          हा अभ्यासक्रम पूर्णतः ब्राउझरमध्ये Python (Pyodide) वापरून चालतो — कोणतीही स्थापना (installation) आवश्यक नाही.
        </div>
      </footer>
    `;
  }

  document.addEventListener("DOMContentLoaded", () => {
    const navHolder = document.getElementById("nav-holder");
    if (navHolder) navHolder.innerHTML = navHTML();
    const footHolder = document.getElementById("footer-holder");
    if (footHolder) footHolder.innerHTML = footerHTML();

    // Re-bind theme button label after injection.
    const btn = document.getElementById("themeBtn");
    if (btn) {
      const cur = document.documentElement.getAttribute("data-theme") || "dark";
      btn.textContent = cur === "dark" ? "☾  गडद" : "☀  उजळ";
    }
  });
})();
