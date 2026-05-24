/*  Azone Academy — ६ वी सामान्य विज्ञान (मराठी)
    Per-chapter custom mini-simulators (small DOM widgets that
    accompany the embedded PhET/OLabs iframe).
    Designed by Appaji Patil.
*/

(function (global) {
  "use strict";

  function $(root, sel) { return root.querySelector(sel); }
  function bindRange(root, name, onChange) {
    const r = $(root, `input[data-name="${name}"]`);
    const v = $(root, `.val[data-for="${name}"]`);
    if (!r) return () => 0;
    const update = () => {
      if (v) v.textContent = r.value;
      onChange && onChange(parseFloat(r.value));
    };
    r.addEventListener("input", update);
    update();
    return () => parseFloat(r.value);
  }
  function bindSelect(root, name, onChange) {
    const s = $(root, `select[data-name="${name}"]`);
    if (!s) return () => "";
    const update = () => onChange && onChange(s.value);
    s.addEventListener("change", update);
    update();
    return () => s.value;
  }
  function setText(root, sel, text) {
    const el = $(root, sel);
    if (el) el.textContent = text;
  }

  /* ---------- Chapter 5: States of Matter mini sim ---------- */
  global.initStatesMini = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const stage = $(root, ".stage-canvas");
    function draw(state) {
      const N = state === "solid" ? 25 : state === "liquid" ? 22 : 18;
      let html = "";
      for (let i = 0; i < N; i++) {
        let x, y;
        if (state === "solid") {
          x = 12 + (i % 5) * 32; y = 14 + Math.floor(i / 5) * 32;
        } else if (state === "liquid") {
          x = 8 + (i % 6) * 28 + Math.random() * 6;
          y = 70 + Math.floor(i / 6) * 28 + Math.random() * 6;
        } else {
          x = Math.random() * 175;
          y = Math.random() * 175;
        }
        html += `<div class="mol" style="left:${x}px;top:${y}px"></div>`;
      }
      stage.innerHTML = html;
    }
    bindSelect(root, "state", v => {
      draw(v);
      const msg = {
        solid: "रेणू एकमेकांना घट्ट चिकटून आहेत — आकार व आकारमान स्थिर.",
        liquid: "रेणू सरकू शकतात — पात्राचा आकार घेतात, आकारमान स्थिर.",
        gas: "रेणू मुक्तपणे फिरतात — आकार व आकारमान दोन्ही बदलतात.",
      }[v];
      setText(root, ".state-msg", msg);
    });
  };

  /* ---------- Chapter 9: Speed calculator ---------- */
  global.initSpeedCalc = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getD = bindRange(root, "d", update);
    const getT = bindRange(root, "t", update);
    function update() {
      const d = getD(), t = getT();
      const v = t > 0 ? (d / t) : 0;
      setText(root, ".out-v", v.toFixed(2) + " m/s");
      setText(root, ".out-vk", (v * 3.6).toFixed(2) + " km/तास");
      const car = $(root, ".car");
      if (car) {
        const dur = Math.max(0.4, 5 - v);
        car.style.animationDuration = dur + "s";
      }
      const msg = v < 1.5 ? "👶 चालण्याचा वेग" :
                  v < 5   ? "🚶 जलद चालणे / धावणे" :
                  v < 15  ? "🚴 सायकलचा वेग" :
                  v < 30  ? "🏍 दुचाकीचा वेग" :
                            "🚗 मोटारीचा वेग";
      setText(root, ".speed-msg", msg);
    }
    update();
  };

  /* ---------- Chapter 10: Force directions ---------- */
  global.initForceLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getL = bindRange(root, "left", update);
    const getR = bindRange(root, "right", update);
    const box = $(root, ".box");
    function update() {
      const net = getR() - getL();
      setText(root, ".out-net", net.toFixed(0) + " N");
      let msg, dir;
      if (net > 0) { msg = "→ उजवीकडे ढकलले जाते"; dir = "right"; }
      else if (net < 0) { msg = "← डावीकडे ढकलले जाते"; dir = "left"; }
      else { msg = "● संतुलित बल — वस्तू स्थिर"; dir = "none"; }
      setText(root, ".force-msg", msg);
      if (box) {
        box.style.transform = `translateX(${Math.max(-80, Math.min(80, net * 1.5))}px)`;
      }
    }
    update();
  };

  /* ---------- Chapter 11: Work calculator ---------- */
  global.initWorkCalc = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getF = bindRange(root, "force", update);
    const getD = bindRange(root, "dist", update);
    function update() {
      const F = getF(), d = getD();
      const W = F * d;
      setText(root, ".out-w", W.toFixed(0) + " J (ज्यूल)");
      const msg = W === 0 ? "विस्थापन शून्य → कार्य = ० J" :
                  F === 0 ? "बल शून्य → कार्य = ० J" :
                            `बल × विस्थापन = ${F} × ${d} = ${W} J`;
      setText(root, ".work-msg", msg);
    }
    update();
  };

  /* ---------- Chapter 12: Lever simulator ---------- */
  global.initLever = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getLoad = bindRange(root, "load", update);
    const getEffArm = bindRange(root, "earm", update);
    const getLoadArm = bindRange(root, "larm", update);
    const beam = $(root, ".beam");
    function update() {
      const load = getLoad(), eA = getEffArm(), lA = getLoadArm();
      // E × eA = L × lA   =>   E = L*lA/eA
      const eff = eA > 0 ? (load * lA) / eA : 0;
      const MA = lA > 0 ? eA / lA : 0;
      setText(root, ".out-eff", eff.toFixed(1) + " N");
      setText(root, ".out-ma", MA.toFixed(2));
      const tilt = Math.max(-10, Math.min(10, (eff * eA - load * lA) * 0.05));
      if (beam) beam.style.transform = `rotate(${tilt}deg)`;
      const msg = MA > 1 ? "✓ यांत्रिक लाभ > १ → कमी बलाने जास्त भार उचलू शकतो" :
                  MA === 1 ? "● यांत्रिक लाभ = १ → बल = भार (दिशा बदलते)" :
                  "△ यांत्रिक लाभ < १ → वेग वा अंतर वाढतो";
      setText(root, ".lever-msg", msg);
    }
    update();
  };

  /* ---------- Chapter 13: Sound — pitch/loudness ---------- */
  global.initSoundLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getFreq = bindRange(root, "freq", update);
    const getAmp = bindRange(root, "amp", update);
    const svg = $(root, ".wave-svg");
    function update() {
      const f = getFreq(), a = getAmp();
      if (svg) {
        const path = buildWave(f, a, 320, 80);
        svg.innerHTML = `<path d="${path}" stroke="var(--primary)" stroke-width="2" fill="none"/>`;
      }
      const pitch = f < 200 ? "🔉 खर्जातील (कमी कंप्रता)" :
                    f < 800 ? "🔊 मध्यम स्वर" :
                              "🎵 उच्च स्वर (टिपेचा आवाज)";
      const loud = a < 20 ? "मंद आवाज" : a < 60 ? "मध्यम आवाज" : "मोठा आवाज";
      setText(root, ".sound-msg", `${pitch}  •  ${loud}  •  कंप्रता: ${f} Hz`);
    }
    function buildWave(f, a, w, h) {
      const cy = h / 2;
      const steps = 200;
      const k = (f / 100) * (Math.PI * 2 / w) * 3;
      let d = `M 0 ${cy}`;
      for (let x = 0; x <= w; x += w / steps) {
        const y = cy - (a / 100) * (h * 0.4) * Math.sin(k * x);
        d += ` L ${x.toFixed(1)} ${y.toFixed(1)}`;
      }
      return d;
    }
    update();
  };

  /* ---------- Chapter 14: Shadow simulator ---------- */
  global.initShadowLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getDist = bindRange(root, "dist", update);
    const getH = bindRange(root, "objh", update);
    const shadow = $(root, ".shadow");
    const obj = $(root, ".obj");
    function update() {
      const d = getDist(), h = getH();
      // simple geometric: shadow length increases as light is farther and object taller
      const sl = Math.max(10, h * (100 / Math.max(20, d)) * 2);
      if (shadow) shadow.style.width = sl + "px";
      if (obj) obj.style.height = h + "px";
      const msg = d < 50 ? "प्रकाश जवळ → सावली मोठी आणि अस्पष्ट" :
                  d < 120 ? "प्रकाश मध्यम अंतरावर → सावली सुस्पष्ट" :
                            "प्रकाश दूर → सावली लहान आणि स्पष्ट";
      setText(root, ".shadow-msg", `${msg}  •  सावली लांबी ≈ ${Math.round(sl)} px`);
    }
    update();
  };

  /* ---------- Chapter 15: Magnet — attract / repel ---------- */
  global.initMagnetLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getA = bindSelect(root, "polea", update);
    const getB = bindSelect(root, "poleb", update);
    const m1 = $(root, ".mag1"), m2 = $(root, ".mag2");
    function update() {
      const a = getA(), b = getB();
      const attract = (a === "N" && b === "S") || (a === "S" && b === "N");
      if (m1 && m2) {
        const tx = attract ? "translateX(40px)" : "translateX(-40px)";
        m2.style.transform = tx;
      }
      const msg = attract
        ? "✓ विरुद्ध ध्रुव → आकर्षण (दोन चुंबक एकमेकांकडे ओढले जातात)"
        : "✗ समान ध्रुव → प्रतिकर्षण (दोन चुंबक एकमेकांपासून दूर ढकलले जातात)";
      setText(root, ".magnet-msg", msg);
    }
    update();
  };

  /* ---------- Chapter 16: Solar system distance scaler ---------- */
  global.initSolarLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const planets = [
      { name: "बुध",      dist:  58, color: "#a89070" },
      { name: "शुक्र",     dist: 108, color: "#d8b272" },
      { name: "पृथ्वी",    dist: 150, color: "#5ab4ff" },
      { name: "मंगळ",     dist: 228, color: "#d96850" },
      { name: "गुरू",     dist: 778, color: "#e0c08a" },
      { name: "शनी",      dist:1430, color: "#e6c97a" },
      { name: "युरेनस",  dist:2880, color: "#86dadd" },
      { name: "नेपच्यून",  dist:4500, color: "#5570ff" },
    ];
    function render(scale) {
      const stage = $(root, ".solar-stage");
      const maxDist = 4500;
      let h = `<div class="sun">☉</div>`;
      for (const p of planets) {
        const x = 30 + (p.dist / maxDist) * 540 * scale;
        h += `<div class="planet" style="left:${x.toFixed(0)}px;background:${p.color}" title="${p.name} — ${p.dist} दशलक्ष किमी">${p.name}</div>`;
      }
      stage.innerHTML = h;
    }
    bindRange(root, "scale", v => {
      render(v);
      setText(root, ".solar-msg", `१ पिक्सेल ≈ ${(4500/(540*v)).toFixed(0)} दशलक्ष किमी`);
    });
  };

})(window);
