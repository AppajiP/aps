/* Azone Academy — AI Course (Marathi)
   Shared JS: theme toggle, Pyodide-backed labs, quizzes, progress.
   Designed by Appaji Patil.
*/

(function () {
  "use strict";

  // ---------- Theme ----------
  const themeKey = "azone-ai-theme";
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

  // ---------- Progress ----------
  const progKey = "azone-ai-progress";
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
      btn.textContent = "✓  पूर्ण झाले!";
      btn.classList.add("primary");
    }
  };

  function renderProgress() {
    const total = parseInt(document.body.dataset.totalChapters || "12", 10);
    const p = readProgress();
    const done = Object.keys(p).filter(k => p[k]).length;
    const pct = Math.min(100, Math.round((done / total) * 100));
    const bar = document.getElementById("progressBar");
    const txt = document.getElementById("progressText");
    if (bar) bar.style.width = pct + "%";
    if (txt) txt.textContent = `${done} / ${total} धडे पूर्ण (${pct}%)`;
    // Highlight completed cards on the index page.
    document.querySelectorAll("[data-chapter-id]").forEach(card => {
      const id = card.getAttribute("data-chapter-id");
      if (p[id]) card.style.outline = "2px solid var(--success)";
    });
  }

  // ---------- Pyodide ----------
  let pyodideInstance = null;
  let pyodideLoading = null;

  async function getPyodide(statusEl) {
    if (pyodideInstance) return pyodideInstance;
    if (pyodideLoading) return pyodideLoading;

    if (statusEl) statusEl.innerHTML = '<span class="spinner"></span> Python (Pyodide) लोड होत आहे... पहिल्या वेळी थोडा वेळ लागेल.';

    pyodideLoading = (async () => {
      if (typeof loadPyodide !== "function") {
        throw new Error("Pyodide स्क्रिप्ट लोड झालेली नाही. इंटरनेट कनेक्शन तपासा.");
      }
      const py = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/"
      });
      pyodideInstance = py;
      return py;
    })();

    try {
      const py = await pyodideLoading;
      if (statusEl) statusEl.textContent = "Python तयार आहे ✓";
      return py;
    } catch (e) {
      pyodideLoading = null;
      if (statusEl) statusEl.textContent = "Python लोड करता आले नाही.";
      throw e;
    }
  }

  function captureStdoutCode(userCode) {
    // Wrap user code so that stdout/stderr are captured to a Python string.
    return [
      "import sys, io, traceback",
      "_az_buf = io.StringIO()",
      "_az_old_out, _az_old_err = sys.stdout, sys.stderr",
      "sys.stdout = _az_buf",
      "sys.stderr = _az_buf",
      "try:",
      "    exec(compile(_az_user_code, '<lab>', 'exec'), {'__name__':'__main__'})",
      "except SystemExit:",
      "    pass",
      "except BaseException:",
      "    traceback.print_exc()",
      "finally:",
      "    sys.stdout, sys.stderr = _az_old_out, _az_old_err",
      "_az_buf.getvalue()"
    ].join("\n");
  }

  window.runLab = async function (labId) {
    const root = document.getElementById(labId);
    if (!root) return;
    const editor = root.querySelector("textarea.editor");
    const output = root.querySelector(".lab-output");
    const status = root.querySelector(".run-status");
    const inputBox = root.querySelector("input.lab-input");

    output.classList.remove("error");
    output.textContent = "";
    status.innerHTML = '<span class="spinner"></span> चालू आहे...';

    try {
      const py = await getPyodide(status);

      // Simple input() emulation: read from a comma/newline separated list.
      let inputs = [];
      if (inputBox && inputBox.value.trim() !== "") {
        inputs = inputBox.value.split("\n").flatMap(l => l.split("|")).map(s => s.trim());
      }
      py.globals.set("_az_inputs", py.toPy(inputs));
      // Override input() so labs that ask for input still work.
      py.runPython([
        "import builtins",
        "_az_inputs_iter = iter(list(_az_inputs)) if _az_inputs is not None else iter([])",
        "def _az_input(prompt=''):",
        "    try:",
        "        v = next(_az_inputs_iter)",
        "    except StopIteration:",
        "        v = ''",
        "    print(str(prompt) + str(v))",
        "    return v",
        "builtins.input = _az_input"
      ].join("\n"));

      py.globals.set("_az_user_code", editor.value);
      const result = py.runPython(captureStdoutCode(editor.value));
      output.textContent = (result && result.toString().length) ? result.toString() : "(कोणतेही आउटपुट नाही)";
      status.textContent = "यशस्वी ✓";
    } catch (err) {
      output.classList.add("error");
      output.textContent = String(err.message || err);
      status.textContent = "त्रुटी";
    }
  };

  window.resetLab = function (labId) {
    const root = document.getElementById(labId);
    if (!root) return;
    const editor = root.querySelector("textarea.editor");
    const initial = editor.getAttribute("data-initial");
    if (initial !== null) editor.value = initial;
    const output = root.querySelector(".lab-output");
    output.textContent = "";
    output.classList.remove("error");
    const status = root.querySelector(".run-status");
    if (status) status.textContent = "";
  };

  window.copyLab = async function (labId) {
    const root = document.getElementById(labId);
    if (!root) return;
    const editor = root.querySelector("textarea.editor");
    try {
      await navigator.clipboard.writeText(editor.value);
      const status = root.querySelector(".run-status");
      if (status) status.textContent = "कॉपी झाले ✓";
    } catch {}
  };

  // ---------- Quizzes ----------
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

  // ---------- Initialise on DOM ready ----------
  document.addEventListener("DOMContentLoaded", () => {
    // Save initial editor values for "reset".
    document.querySelectorAll("textarea.editor").forEach(t => {
      if (!t.hasAttribute("data-initial")) t.setAttribute("data-initial", t.value);
    });
    renderProgress();
    // Sync theme button label.
    const btn = document.getElementById("themeBtn");
    const cur = document.documentElement.getAttribute("data-theme") || "dark";
    if (btn) btn.textContent = cur === "dark" ? "☾  गडद" : "☀  उजळ";
  });
})();
