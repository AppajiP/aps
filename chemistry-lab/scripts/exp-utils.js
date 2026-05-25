/*
 * exp-utils.js — small helpers shared by every experiment page.
 * Loaded with a regular <script> tag (no modules) so pages remain openable
 * directly from the filesystem.
 */
(function (global) {
  "use strict";

  function setupCanvas(canvas) {
    const ctx = canvas.getContext("2d");
    function resize() {
      const dpr = global.devicePixelRatio || 1;
      const rect = canvas.getBoundingClientRect();
      canvas.width  = Math.max(1, Math.floor(rect.width  * dpr));
      canvas.height = Math.max(1, Math.floor(rect.height * dpr));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    resize();
    let resizeTimer;
    global.addEventListener("resize", () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(resize, 80);
    });
    return { ctx, resize, width: () => canvas.clientWidth, height: () => canvas.clientHeight };
  }

  function rng(seed) {
    let s = seed | 0 || 1;
    return function () {
      s = (s * 1103515245 + 12345) | 0;
      return ((s >>> 16) & 0x7fff) / 0x7fff;
    };
  }

  function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }
  function lerp(a, b, t)  { return a + (b - a) * t; }

  function loop(step) {
    let raf, last = performance.now();
    let stopped = false;
    function tick(now) {
      if (stopped) return;
      const dt = Math.min(50, now - last) / 1000;
      last = now;
      step(dt, now / 1000);
      raf = global.requestAnimationFrame(tick);
    }
    raf = global.requestAnimationFrame(tick);
    return {
      stop: () => { stopped = true; cancelAnimationFrame(raf); }
    };
  }

  function statusPill(el, kind, text) {
    el.classList.remove("ok", "warn", "err");
    if (kind) el.classList.add(kind);
    el.querySelector(".text").textContent = text;
  }

  global.ChemUtils = { setupCanvas, rng, clamp, lerp, loop, statusPill };
})(window);
