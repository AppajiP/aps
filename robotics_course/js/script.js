/*  Azone Academy — Robotics Course (Marathi)
    Shared script: theme toggle, progress tracking, quizzes, code helpers.
    Designed by Appaji Patil.
*/

(function () {
  "use strict";

  /* ---------- Theme ---------- */
  const themeKey = "azone-rob-theme";
  const savedTheme = localStorage.getItem(themeKey);
  if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);

  window.toggleTheme = function () {
    const cur = document.documentElement.getAttribute("data-theme") || "dark";
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem(themeKey, next);
    const btn = document.getElementById("themeBtn");
    if (btn) btn.textContent = next === "dark" ? "☾  गडद" : "☀  उजळ";
  };

  /* ---------- Progress ---------- */
  const progKey = "azone-rob-progress";
  function readProgress() {
    try { return JSON.parse(localStorage.getItem(progKey)) || {}; }
    catch { return {}; }
  }
  function writeProgress(p) { localStorage.setItem(progKey, JSON.stringify(p)); }

  window.markChapterDone = function (id) {
    const p = readProgress();
    p[id] = true;
    writeProgress(p);
    renderProgress();
    const btn = document.getElementById("doneBtn");
    if (btn) {
      btn.textContent = "✓  धडा पूर्ण झाला!";
      btn.classList.add("primary");
    }
  };

  function renderProgress() {
    const total = parseInt(document.body.dataset.totalChapters || "16", 10);
    const p = readProgress();
    const done = Object.keys(p).filter(k => p[k]).length;
    const pct = Math.min(100, Math.round((done / total) * 100));
    const bar = document.getElementById("progressBar");
    const txt = document.getElementById("progressText");
    if (bar) bar.style.width = pct + "%";
    if (txt) txt.textContent = `${done} / ${total} धडे पूर्ण (${pct}%)`;
    document.querySelectorAll("[data-chapter-id]").forEach(card => {
      const id = card.getAttribute("data-chapter-id");
      if (p[id]) card.style.outline = "2px solid var(--success)";
    });
  }

  /* ---------- Code helpers (copy / reset) ---------- */
  window.copyLab = async function (labId) {
    const root = document.getElementById(labId);
    if (!root) return;
    const editor = root.querySelector("textarea.editor");
    if (!editor) return;
    try {
      await navigator.clipboard.writeText(editor.value);
      const status = root.querySelector(".run-status");
      if (status) status.textContent = "कोड कॉपी झाला ✓";
    } catch {
      /* clipboard not available — ignore */
    }
  };

  window.resetLab = function (labId) {
    const root = document.getElementById(labId);
    if (!root) return;
    const editor = root.querySelector("textarea.editor");
    if (editor) {
      const initial = editor.getAttribute("data-initial");
      if (initial !== null) editor.value = initial;
    }
    const out = root.querySelector(".lab-output");
    if (out) { out.textContent = ""; out.classList.remove("error"); }
    const status = root.querySelector(".run-status");
    if (status) status.textContent = "";
    // Per-lab reset hook
    const resetFn = root.getAttribute("data-reset");
    if (resetFn && typeof window[resetFn] === "function") window[resetFn](root);
  };

  /* ---------- Quizzes ---------- */
  window.checkQuiz = function (quizId) {
    const root = document.getElementById(quizId);
    if (!root) return;
    let correct = 0, total = 0;
    root.querySelectorAll(".q").forEach(q => {
      total++;
      const ans = q.getAttribute("data-answer");
      const sel = q.querySelector("input[type=radio]:checked");
      const fb = q.querySelector(".feedback");
      if (sel && sel.value === ans) {
        correct++;
        fb.textContent = "✓ बरोबर!";
        fb.className = "feedback ok";
      } else {
        fb.textContent = "✗ चुकीचे — योग्य उत्तर: " + (q.getAttribute("data-answer-text") || ans);
        fb.className = "feedback bad";
      }
    });
    const summary = root.querySelector(".quiz-summary");
    if (summary) summary.textContent = `गुण: ${correct} / ${total}`;
  };

  /* ---------- Init ---------- */
  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("textarea.editor").forEach(t => {
      if (!t.hasAttribute("data-initial")) t.setAttribute("data-initial", t.value);
    });
    renderProgress();
    const btn = document.getElementById("themeBtn");
    const cur = document.documentElement.getAttribute("data-theme") || "dark";
    if (btn) btn.textContent = cur === "dark" ? "☾  गडद" : "☀  उजळ";
  });
})();
