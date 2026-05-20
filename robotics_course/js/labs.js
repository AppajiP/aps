/*  Azone Academy — Robotics Course
    Per-lab simulators. Each chapter wires up its simulator after DOMContentLoaded.
    Designed by Appaji Patil.
*/

(function (global) {
  "use strict";

  // ---------- Helpers shared by all simulators ----------
  function $(root, sel) { return root.querySelector(sel); }
  function $$(root, sel) { return Array.from(root.querySelectorAll(sel)); }

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

  function bindCheckbox(root, name, onChange) {
    const c = $(root, `input[data-name="${name}"]`);
    if (!c) return () => false;
    const update = () => onChange && onChange(c.checked);
    c.addEventListener("change", update);
    update();
    return () => c.checked;
  }

  function bindSelect(root, name, onChange) {
    const s = $(root, `select[data-name="${name}"]`);
    if (!s) return () => "";
    const update = () => onChange && onChange(s.value);
    s.addEventListener("change", update);
    update();
    return () => s.value;
  }

  function setLED(root, name, on, color) {
    const el = $(root, `.led[data-name="${name}"]`);
    if (!el) return;
    el.classList.toggle("on", !!on);
    ["red", "green", "blue"].forEach(c => el.classList.remove(c));
    if (on && color) el.classList.add(color);
  }

  function setText(root, sel, text) {
    const el = $(root, sel);
    if (el) el.textContent = text;
  }

  function setPin(root, label, value) {
    const cell = $(root, `[data-pin="${label}"]`);
    if (cell) cell.innerHTML = `<b>${value}</b>`;
  }

  // Convert 0..100 (or any number) to HIGH/LOW around a threshold.
  function digital(v, threshold) {
    return v >= threshold ? "HIGH" : "LOW";
  }

  // ============================================================
  // Foundation labs
  // ============================================================

  // Ohm's law calculator (chapter 3)
  global.initOhmsLawLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getV = bindRange(root, "v", update);
    const getR = bindRange(root, "r", update);
    function update() {
      const v = getV(), r = getR();
      const i = r > 0 ? (v / r) : 0;
      const p = v * i;
      setText(root, ".out-i", i.toFixed(3) + " A");
      setText(root, ".out-i-ma", (i * 1000).toFixed(1) + " mA");
      setText(root, ".out-p", p.toFixed(3) + " W");
      // LED needs ~ 10–20 mA to glow; below 1 mA = off; above 30 mA = burnt.
      const led = $(root, ".led[data-name='led']");
      led.classList.remove("on", "red");
      if (i * 1000 > 30) { led.classList.add("on", "red"); setText(root, ".led-msg", "⚠ LED जळून जाईल!"); }
      else if (i * 1000 > 2) { led.classList.add("on"); setText(root, ".led-msg", "✓ LED योग्य प्रकारे चमकत आहे."); }
      else { setText(root, ".led-msg", "विद्युतप्रवाह कमी आहे — LED मंद किंवा बंद."); }
    }
    update();
  };

  // Resistor color code (chapter 4)
  global.initResistorColorLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const colors = [
      { name: "काळा (Black)", d: 0,  m: 1,         t: "" },
      { name: "तपकिरी (Brown)", d: 1, m: 10,       t: "1%" },
      { name: "लाल (Red)", d: 2, m: 100,           t: "2%" },
      { name: "नारिंगी (Orange)", d: 3, m: 1000,   t: "" },
      { name: "पिवळा (Yellow)", d: 4, m: 10000,    t: "" },
      { name: "हिरवा (Green)", d: 5, m: 100000,    t: "0.5%" },
      { name: "निळा (Blue)", d: 6, m: 1000000,     t: "0.25%" },
      { name: "जांभळा (Violet)", d: 7, m: 10000000,t: "0.1%" },
      { name: "करडा (Grey)", d: 8, m: 0,           t: "" },
      { name: "पांढरा (White)", d: 9, m: 0,        t: "" },
      { name: "सोनेरी (Gold)", d: -1, m: 0.1,      t: "5%" },
      { name: "चंदेरी (Silver)", d: -1, m: 0.01,   t: "10%" }
    ];
    ["b1", "b2", "b3", "b4"].forEach(name => {
      const sel = $(root, `select[data-name="${name}"]`);
      if (!sel) return;
      colors.forEach((c, i) => {
        if (name === "b4" && c.d >= 0 && c.t === "") return;
        if (name !== "b4" && c.d < 0) return;
        const opt = document.createElement("option");
        opt.value = i; opt.textContent = c.name;
        sel.appendChild(opt);
      });
      sel.addEventListener("change", update);
    });
    function update() {
      const b1 = colors[+$(root, "select[data-name='b1']").value];
      const b2 = colors[+$(root, "select[data-name='b2']").value];
      const b3 = colors[+$(root, "select[data-name='b3']").value];
      const b4 = colors[+$(root, "select[data-name='b4']").value];
      const val = (b1.d * 10 + b2.d) * b3.m;
      let display;
      if (val >= 1e6) display = (val / 1e6) + " MΩ";
      else if (val >= 1e3) display = (val / 1e3) + " kΩ";
      else display = val + " Ω";
      setText(root, ".out-r", display);
      setText(root, ".out-tol", "± " + (b4.t || "—"));
      // colour the band visuals
      ["b1", "b2", "b3", "b4"].forEach((n, i) => {
        const band = $(root, `.band[data-name="${n}"]`);
        if (band) band.style.background = bandCSS(+$(root, `select[data-name="${n}"]`).value);
      });
    }
    function bandCSS(idx) {
      const css = ["#111","#7b3f00","#c0392b","#e67e22","#f1c40f","#27ae60","#2980b9","#8e44ad","#7f8c8d","#ecf0f1","#d4af37","#bdc3c7"];
      return css[idx] || "#444";
    }
    // populate defaults: red(2), red(2), red(*100) -> 2200 = 2.2k
    $(root, "select[data-name='b1']").value = 2;
    $(root, "select[data-name='b2']").value = 2;
    $(root, "select[data-name='b3']").value = 2;
    $(root, "select[data-name='b4']").value = 10;
    update();
  };

  // Sensor explorer (chapter 5)
  global.initSensorLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const kindSel = $(root, "select[data-name='kind']");
    const slider = $(root, "input[data-name='val']");
    const sliderVal = $(root, ".val[data-for='val']");
    const threshSlider = $(root, "input[data-name='th']");
    const threshVal = $(root, ".val[data-for='th']");
    function labelOf(kind, v) {
      switch (kind) {
        case "ir":
          return v < 30 ? "अडथळा जवळ ✓" : v < 60 ? "मध्यम अंतर" : "मोकळी जागा";
        case "ldr":
          return v < 30 ? "अंधार 🌑" : v < 70 ? "मंद प्रकाश" : "तेजस्वी प्रकाश ☀";
        case "touch":
          return v > 50 ? "स्पर्श झाला 👆" : "स्पर्श नाही";
        case "tilt":
          return v > 50 ? "कलला 🔄" : "स्थिर";
        case "ultra":
          return "अंतर: " + Math.round(v * 4) + " cm";
        default: return "—";
      }
    }
    function update() {
      const v = parseFloat(slider.value), th = parseFloat(threshSlider.value);
      const kind = kindSel.value;
      sliderVal.textContent = v;
      threshVal.textContent = th;
      setText(root, ".out-analog", v.toString());
      setText(root, ".out-digital", v >= th ? "HIGH (1)" : "LOW (0)");
      setText(root, ".out-meaning", labelOf(kind, v));
      // a small visual bar
      const bar = $(root, ".sensor-bar");
      if (bar) bar.style.width = v + "%";
    }
    kindSel.addEventListener("change", update);
    slider.addEventListener("input", update);
    threshSlider.addEventListener("input", update);
    update();
  };

  // Motor / actuator lab (chapter 6)
  global.initActuatorLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const speed = bindRange(root, "pwm", update);
    const dir = bindSelect(root, "dir", update);
    function update() {
      const s = speed(), d = dir();
      setText(root, ".out-pwm", s);
      setText(root, ".out-dir", d === "fwd" ? "पुढे →" : d === "rev" ? "← मागे" : "थांब");
      const fan = $(root, ".fan");
      fan.classList.toggle("spinning", s > 0 && d !== "stop");
      fan.classList.toggle("fast", s > 60);
      // motor speed label
      setText(root, ".out-speed-mark", s === 0 ? "बंद" : s < 40 ? "मंद" : s < 80 ? "मध्यम" : "वेगवान");
    }
    update();
  };

  // Arduino "blink" trace lab (chapter 7) — fake serial output
  global.initBlinkTraceLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const out = $(root, ".lab-output");
    const status = $(root, ".run-status");
    let timer = null, on = false, n = 0;
    $(root, "button[data-act='start']").addEventListener("click", () => {
      if (timer) return;
      const delay = parseInt($(root, "input[data-name='delay']").value, 10) || 500;
      n = 0; out.textContent = "";
      timer = setInterval(() => {
        on = !on;
        n++;
        const t = n * delay;
        out.textContent += `t=${String(t).padStart(5)} ms : digitalWrite(13, ${on ? "HIGH" : "LOW "}) — LED ${on ? "चालू" : "बंद"}\n`;
        out.scrollTop = out.scrollHeight;
        setLED(root, "led", on);
        if (n > 14) { clearInterval(timer); timer = null; status.textContent = "थांबवले."; }
      }, delay);
      status.textContent = "चालू आहे...";
    });
    $(root, "button[data-act='stop']").addEventListener("click", () => {
      if (timer) { clearInterval(timer); timer = null; }
      setLED(root, "led", false);
      status.textContent = "थांबवले.";
    });
  };

  // ============================================================
  // Project labs (chapters 8 .. 16)
  // ============================================================

  // 8 — Tilt sensor using obstacle (IR) sensor: object close => "tilt"
  global.initTiltObstacleLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getDist = bindRange(root, "dist", update);
    const getTh   = bindRange(root, "th",   update);
    function update() {
      const d = getDist(), th = getTh();
      const tilted = d < th;
      setPin(root, "IR", tilted ? "LOW (अडथळा)" : "HIGH (मोकळी)");
      setPin(root, "LED", tilted ? "ON" : "OFF");
      setPin(root, "Buzzer", tilted ? "ON" : "OFF");
      setLED(root, "led", tilted, "red");
      setText(root, ".out-status", tilted ? "⚠ झुकले! अलर्ट चालू." : "✓ स्थिर.");
      setText(root, ".out-buzz", tilted ? "🔊 बीप बीप" : "—");
    }
    update();
  };

  // 9 — Light Controlled Machine: LDR-based on/off
  global.initLightMachineLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getL = bindRange(root, "light", update);
    const getTh = bindRange(root, "th", update);
    const getMode = bindSelect(root, "mode", update);
    function update() {
      const l = getL(), th = getTh(), mode = getMode();
      const dark = l < th;
      const on = mode === "dark-on" ? dark : !dark;
      setPin(root, "LDR", l + " (" + (dark ? "अंधार" : "उजेड") + ")");
      setPin(root, "Relay", on ? "HIGH" : "LOW");
      const fan = $(root, ".fan");
      fan.classList.toggle("spinning", on);
      setLED(root, "led", on, "green");
      setText(root, ".out-status", on ? "✓ यंत्र चालू (पंखा/दिवा)" : "बंद");
    }
    update();
  };

  // 10 — Cliff Avoiding Robot: IR pointing downward; no reflection => cliff
  global.initCliffLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getH = bindRange(root, "height", update);
    const getTh = bindRange(root, "th", update);
    function update() {
      const h = getH(), th = getTh();
      const cliff = h > th;
      setPin(root, "IR-down", cliff ? "HIGH (कडा)" : "LOW (जमीन)");
      setPin(root, "Left motor",  cliff ? "STOP / REV" : "FWD");
      setPin(root, "Right motor", cliff ? "FWD" : "FWD");
      setLED(root, "led", cliff, "red");
      setText(root, ".out-status", cliff ? "⚠ कडा! रोबो वळतोय." : "✓ पुढे चालू.");
      // tiny robot animation hint via transform
      const bot = $(root, ".bot");
      if (bot) bot.style.transform = cliff ? "rotate(-25deg)" : "rotate(0deg)";
    }
    update();
  };

  // 11 — Line Follower: two IR sensors under bot
  global.initLineFollowerLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getL = bindCheckbox(root, "left", update);
    const getR = bindCheckbox(root, "right", update);
    function update() {
      const l = getL(), r = getR();
      let leftM = "FWD", rightM = "FWD", state = "सरळ चालू";
      if (l && !r) { leftM = "STOP"; rightM = "FWD"; state = "← डावीकडे वळ"; }
      else if (!l && r) { leftM = "FWD"; rightM = "STOP"; state = "उजवीकडे वळ →"; }
      else if (l && r) { leftM = "STOP"; rightM = "STOP"; state = "🛑 क्रॉसिंग / थांब"; }
      setPin(root, "L sensor", l ? "BLACK (1)" : "WHITE (0)");
      setPin(root, "R sensor", r ? "BLACK (1)" : "WHITE (0)");
      setPin(root, "Left motor", leftM);
      setPin(root, "Right motor", rightM);
      setText(root, ".out-status", state);
    }
    update();
  };

  // 12 — Touch me not Robot: touch sensor triggers retreat / buzz
  global.initTouchNotLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getT = bindCheckbox(root, "touch", update);
    function update() {
      const t = getT();
      setPin(root, "Touch", t ? "HIGH (स्पर्श)" : "LOW");
      setPin(root, "Motors", t ? "REVERSE" : "STOP");
      setPin(root, "Buzzer", t ? "ON" : "OFF");
      setLED(root, "led", t, "red");
      setText(root, ".out-status", t ? "⚠ मला स्पर्श करू नका! मागे जातोय." : "✓ शांत.");
    }
    update();
  };

  // 13 — Smart street light: time + LDR + motion
  global.initStreetLightLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getL = bindRange(root, "light", update);
    const getM = bindCheckbox(root, "motion", update);
    function update() {
      const l = getL(), m = getM();
      const dark = l < 35;
      let brightness = 0;
      if (dark && m) brightness = 100;
      else if (dark) brightness = 25;
      setPin(root, "LDR", l + (dark ? " (अंधार)" : " (उजेड)"));
      setPin(root, "PIR", m ? "HIGH (हालचाल)" : "LOW");
      setPin(root, "PWM out", brightness);
      const led = $(root, ".led[data-name='led']");
      led.classList.toggle("on", brightness > 0);
      led.style.opacity = (brightness / 100 + 0.2).toFixed(2);
      setText(root, ".out-status",
        brightness === 100 ? "🌕 पूर्ण उजेड (कोणीतरी आहे)" :
        brightness === 25  ? "🌗 मंद उजेड (फक्त अंधार)" :
        "बंद (दिवस)");
    }
    update();
  };

  // 14 — Light Seeking Robot: two LDRs; bot turns toward brighter side
  global.initLightSeekerLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    const getL = bindRange(root, "left", update);
    const getR = bindRange(root, "right", update);
    function update() {
      const l = getL(), r = getR();
      let leftM, rightM, state;
      const diff = l - r;
      if (Math.abs(diff) < 8)      { leftM = "FWD"; rightM = "FWD"; state = "↑ प्रकाशाकडे सरळ"; }
      else if (diff > 0)           { leftM = "FWD"; rightM = "STOP"; state = "→ उजव्या बाजूचा प्रकाश कमी, उजवीकडे वळ"; }
      else                         { leftM = "STOP"; rightM = "FWD"; state = "← डाव्या बाजूचा प्रकाश कमी, डावीकडे वळ"; }
      setPin(root, "L-LDR", l);
      setPin(root, "R-LDR", r);
      setPin(root, "Left motor", leftM);
      setPin(root, "Right motor", rightM);
      setText(root, ".out-status", state);
      const bot = $(root, ".bot");
      if (bot) bot.style.transform = `rotate(${Math.max(-30, Math.min(30, diff / 2))}deg)`;
    }
    update();
  };

  // 15 — Remote Controlled Lamp & Buzzer: IR remote buttons
  global.initRemoteLampLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    let lampOn = false, buzzOn = false;
    function refresh() {
      setLED(root, "lamp", lampOn);
      setPin(root, "Lamp", lampOn ? "ON" : "OFF");
      setPin(root, "Buzzer", buzzOn ? "ON" : "OFF");
      setText(root, ".out-status",
        (lampOn ? "💡 दिवा चालू" : "💡 दिवा बंद") + "  •  " +
        (buzzOn ? "🔊 बझर चालू" : "🔇 बझर बंद"));
      setText(root, ".out-buzz", buzzOn ? "BEEP BEEP" : "—");
    }
    $(root, "button[data-key='1']").addEventListener("click", () => { lampOn = true; refresh(); pushLog(root, "Key 1 → लॅम्प चालू"); });
    $(root, "button[data-key='2']").addEventListener("click", () => { lampOn = false; refresh(); pushLog(root, "Key 2 → लॅम्प बंद"); });
    $(root, "button[data-key='3']").addEventListener("click", () => { buzzOn = true; refresh(); pushLog(root, "Key 3 → बझर चालू"); });
    $(root, "button[data-key='4']").addEventListener("click", () => { buzzOn = false; refresh(); pushLog(root, "Key 4 → बझर बंद"); });
    refresh();
  };

  // 16 — Remote Controlled Fan: IR remote with speed levels
  global.initRemoteFanLab = function (id) {
    const root = document.getElementById(id);
    if (!root) return;
    let speed = 0;
    function refresh() {
      const fan = $(root, ".fan");
      fan.classList.toggle("spinning", speed > 0);
      fan.classList.toggle("fast", speed >= 2);
      setPin(root, "Speed", speed === 0 ? "OFF" : speed);
      setPin(root, "PWM",   speed === 0 ? 0 : speed === 1 ? 80 : speed === 2 ? 170 : 255);
      setText(root, ".out-status",
        speed === 0 ? "बंद" :
        speed === 1 ? "🌀 मंद वेग" :
        speed === 2 ? "🌪 मध्यम वेग" :
                       "🌪🌪 जलद वेग");
    }
    $(root, "button[data-key='off']").addEventListener("click", () => { speed = 0; refresh(); pushLog(root, "OFF"); });
    $(root, "button[data-key='1']").addEventListener("click",   () => { speed = 1; refresh(); pushLog(root, "Speed 1"); });
    $(root, "button[data-key='2']").addEventListener("click",   () => { speed = 2; refresh(); pushLog(root, "Speed 2"); });
    $(root, "button[data-key='3']").addEventListener("click",   () => { speed = 3; refresh(); pushLog(root, "Speed 3"); });
    refresh();
  };

  function pushLog(root, msg) {
    const log = root.querySelector(".lab-output");
    if (!log) return;
    log.textContent += msg + "\n";
    log.scrollTop = log.scrollHeight;
  }

})(window);
