/*
 * Master registry of experiments displayed on the resource gallery.
 * Each entry is a self-contained record consumed by main.js.
 *
 * categories:
 *   - "core"   : standard curriculum experiment
 *   - "fun"    : demo / fun experiment
 *   - "ext"    : extension / advanced
 *   - "theory" : conceptual / model
 *
 * type: matches the filter chip groups
 *   - "inquiry"   (探究)
 *   - "3d"        (3D model)
 *   - "demo"      (video-style demo)
 *   - "interactive" (interactive simulation)
 *   - "theory"    (study/notes)
 */
window.CHEM_EXPERIMENTS = [
  {
    id: "kmno4-decomposition",
    title: "Preparing Oxygen by Heating Potassium Permanganate",
    badge: "core",
    type: "inquiry",
    unit: "Unit 2 — Air & Oxygen",
    formula: "2 KMnO\u2084 \u2192 K\u2082MnO\u2084 + MnO\u2082 + O\u2082\u2191",
    interactive: true,
    file: "experiments/kmno4-decomposition.html",
    summary: "Heat KMnO₄ in a test tube and collect oxygen over water."
  },
  {
    id: "iron-in-oxygen",
    title: "Burning Iron Wire in Oxygen",
    badge: "core",
    type: "inquiry",
    unit: "Unit 2 — Air & Oxygen",
    formula: "3 Fe + 2 O\u2082 \u2192 Fe\u2083O\u2084",
    interactive: true,
    file: "experiments/iron-in-oxygen.html",
    summary: "Observe the sparkling combustion of an iron spiral in pure O₂."
  },
  {
    id: "electrolysis-water",
    title: "Composition of Water — Electrolysis",
    badge: "core",
    type: "inquiry",
    unit: "Unit 4 — Natural Resources",
    formula: "2 H\u2082O \u2192 2 H\u2082\u2191 + O\u2082\u2191",
    interactive: true,
    file: "experiments/electrolysis-water.html",
    summary: "Split water with electric current; collect H₂:O₂ in a 2:1 volume ratio."
  },
  {
    id: "dust-explosion",
    title: "Dust Explosion",
    badge: "core",
    type: "interactive",
    unit: "Unit 7 — Fuels & Combustion",
    formula: "C\u2086H\u2081\u2080O\u2085 + O\u2082 \u2192 CO\u2082 + H\u2082O",
    interactive: true,
    file: "experiments/dust-explosion.html",
    summary: "Demonstrate how finely-divided flour ignites explosively in a sealed can."
  },
  {
    id: "co-reduces-fe2o3",
    title: "Reduction of Iron(III) Oxide by Carbon Monoxide",
    badge: "core",
    type: "inquiry",
    unit: "Unit 8 — Metals & Their Compounds",
    formula: "3 CO + Fe\u2082O\u2083 \u2192 2 Fe + 3 CO\u2082",
    interactive: false,
    file: "experiments/co-reduces-fe2o3.html",
    summary: "Heat Fe₂O₃ in a stream of CO to smelt elemental iron."
  },
  {
    id: "golden-rain",
    title: "Golden Rain (Lead(II) Iodide Crystals)",
    badge: "fun",
    type: "interactive",
    unit: "Demo — Crystallization",
    formula: "Pb(NO\u2083)\u2082 + 2 KI \u2192 PbI\u2082\u2193 + 2 KNO\u2083",
    interactive: true,
    file: "experiments/golden-rain.html",
    summary: "Watch shimmering gold flakes of PbI₂ rain through a cooling solution."
  },
  {
    id: "elements-battle",
    title: "Periodic Table — Elements Quiz",
    badge: "theory",
    type: "interactive",
    unit: "Unit 3 — Matter & Composition",
    formula: "118 elements",
    interactive: true,
    file: "experiments/elements-battle.html",
    summary: "Practice element symbols, atomic numbers, and groups with a quick quiz."
  },
  {
    id: "pharaoh-serpent",
    title: "Pharaoh's Serpent (Decomposition of HgSCN)",
    badge: "fun",
    type: "demo",
    unit: "Demo — Decomposition",
    formula: "2 Hg(SCN)\u2082 \u2192 2 HgS + CS\u2082 + C\u2083N\u2084 (simplified)",
    interactive: false,
    file: "experiments/pharaoh-serpent.html",
    summary: "A snake-like solid grows from a tiny pellet of mercury(II) thiocyanate."
  },
  {
    id: "oxygen-in-air",
    title: "Measuring the Oxygen Content of Air",
    badge: "core",
    type: "inquiry",
    unit: "Unit 2 — Air & Oxygen",
    formula: "4 P + 5 O\u2082 \u2192 2 P\u2082O\u2085",
    interactive: true,
    file: "experiments/oxygen-in-air.html",
    summary: "Burn red phosphorus in a sealed bell-jar to show that O₂ is ~1/5 of air."
  },
  {
    id: "fountain-nh3",
    title: "Ammonia Fountain Experiment",
    badge: "ext",
    type: "interactive",
    unit: "Extension — Solubility",
    formula: "NH\u2083 + H\u2082O \u2192 NH\u2083\u00B7H\u2082O",
    interactive: true,
    file: "experiments/fountain-nh3.html",
    summary: "Highly soluble NH₃ drives a vivid pink fountain into a flask of phenolphthalein water."
  },
  {
    id: "water-drop-smoke",
    title: "Dripping Water Lights Smoke",
    badge: "fun",
    type: "demo",
    unit: "Demo — Exothermic Reaction",
    formula: "Zn + Na\u2082O\u2082 + H\u2082O \u2192 ...",
    interactive: false,
    file: "experiments/water-drop-smoke.html",
    summary: "A single drop of water ignites a mixture that releases smoke."
  },
  {
    id: "co2-prep",
    title: "Laboratory Preparation & Properties of CO₂",
    badge: "core",
    type: "inquiry",
    unit: "Unit 6 — Carbon",
    formula: "CaCO\u2083 + 2 HCl \u2192 CaCl\u2082 + H\u2082O + CO\u2082\u2191",
    interactive: true,
    file: "experiments/co2-prep.html",
    summary: "Generate CO₂ from marble and dilute HCl, then test density, water and lime-water reactions."
  },
  {
    id: "copper-oxygen-mass",
    title: "Mass of Copper Before & After Reacting with Oxygen",
    badge: "core",
    type: "inquiry",
    unit: "Unit 5 — Conservation of Mass",
    formula: "2 Cu + O\u2082 \u2192 2 CuO",
    interactive: true,
    file: "experiments/copper-oxygen-mass.html",
    summary: "Show that copper gains mass when heated in air — and explain why."
  },
  {
    id: "fire-extinguisher",
    title: "Build a Simple Fire Extinguisher",
    badge: "ext",
    type: "interactive",
    unit: "Unit 7 — Fuels & Combustion",
    formula: "NaHCO\u2083 + HCl \u2192 NaCl + H\u2082O + CO\u2082\u2191",
    interactive: true,
    file: "experiments/fire-extinguisher.html",
    summary: "Combine baking soda with vinegar/HCl inside a sealed bottle to produce CO₂ foam."
  },
  {
    id: "atomic-structure",
    title: "Structure of the Atom",
    badge: "theory",
    type: "interactive",
    unit: "Unit 3 — Matter & Composition",
    formula: "Z = protons,  A = p + n",
    interactive: true,
    file: "experiments/atomic-structure.html",
    summary: "Interactive Bohr-style model of the first 20 elements."
  },
  {
    id: "balance-equations",
    title: "Balancing Chemical Equations",
    badge: "theory",
    type: "interactive",
    unit: "Unit 5 — Conservation of Mass",
    formula: "a A + b B \u2192 c C + d D",
    interactive: true,
    file: "experiments/balance-equations.html",
    summary: "Drag stoichiometric coefficients to balance common reactions."
  },
  {
    id: "paraffin-melt",
    title: "Melting of Paraffin Wax",
    badge: "core",
    type: "theory",
    unit: "Unit 1 — Physical & Chemical Change",
    formula: "Physical change",
    interactive: false,
    file: "experiments/paraffin-melt.html",
    summary: "Distinguish physical change (melting) from chemical change (burning)."
  },
  {
    id: "ca-oh-2-decay",
    title: "Has the Ca(OH)₂ Gone Bad?",
    badge: "ext",
    type: "inquiry",
    unit: "Unit 10 — Acids, Bases & Salts",
    formula: "Ca(OH)\u2082 + CO\u2082 \u2192 CaCO\u2083\u2193 + H\u2082O",
    interactive: false,
    file: "experiments/ca-oh-2-decay.html",
    summary: "Design tests to detect carbonate impurity in slaked lime."
  },
  {
    id: "iodine-sublimation",
    title: "Sublimation of Iodine",
    badge: "ext",
    type: "demo",
    unit: "Extension — Phase Change",
    formula: "I\u2082(s) \u2192 I\u2082(g)",
    interactive: false,
    file: "experiments/iodine-sublimation.html",
    summary: "Heat solid iodine and observe direct conversion to violet vapor."
  },
  {
    id: "naoh-decay",
    title: "Has the NaOH Gone Bad?",
    badge: "ext",
    type: "inquiry",
    unit: "Unit 10 — Acids, Bases & Salts",
    formula: "2 NaOH + CO\u2082 \u2192 Na\u2082CO\u2083 + H\u2082O",
    interactive: false,
    file: "experiments/naoh-decay.html",
    summary: "Identify Na₂CO₃ impurity in solid NaOH that was exposed to air."
  },
  {
    id: "alcohol-flame",
    title: "The Three Zones of an Alcohol Lamp Flame",
    badge: "core",
    type: "theory",
    unit: "Unit 1 — Lab Techniques",
    formula: "Outer / Inner / Core zones",
    interactive: false,
    file: "experiments/alcohol-flame.html",
    summary: "Locate the hottest part of an alcohol flame using a match."
  },
  {
    id: "h2so4-dilute",
    title: "Diluting Concentrated Sulfuric Acid Safely",
    badge: "core",
    type: "theory",
    unit: "Unit 10 — Acids, Bases & Salts",
    formula: "Add acid TO water — never the reverse",
    interactive: false,
    file: "experiments/h2so4-dilute.html",
    summary: "Step-by-step safe procedure with explanation of the exothermic dissolution."
  },
  {
    id: "charcoal-burn",
    title: "Burning Charcoal in Air vs. in Pure Oxygen",
    badge: "core",
    type: "inquiry",
    unit: "Unit 2 — Air & Oxygen",
    formula: "C + O\u2082 \u2192 CO\u2082",
    interactive: false,
    file: "experiments/charcoal-burn.html",
    summary: "Compare the dim glow in air with the bright white flame in pure O₂."
  },
  {
    id: "gold-foil",
    title: "Rutherford's Gold Foil Experiment",
    badge: "theory",
    type: "interactive",
    unit: "Unit 3 — Atomic Theory",
    formula: "Discovery of the nucleus (1911)",
    interactive: true,
    file: "experiments/gold-foil.html",
    summary: "Fire alpha particles at a thin gold foil and discover the nuclear atom."
  },
  {
    id: "leak-test",
    title: "Checking Apparatus Air-Tightness",
    badge: "core",
    type: "theory",
    unit: "Unit 1 — Lab Techniques",
    formula: "Bubble test",
    interactive: false,
    file: "experiments/leak-test.html",
    summary: "Use warm hands and a beaker of water to test whether a setup leaks gas."
  },
  {
    id: "kclo3-prep",
    title: "Preparing Oxygen from Potassium Chlorate + MnO₂",
    badge: "core",
    type: "inquiry",
    unit: "Unit 2 — Air & Oxygen",
    formula: "2 KClO\u2083 \u2192 2 KCl + 3 O\u2082\u2191  (MnO\u2082 cat.)",
    interactive: false,
    file: "experiments/kclo3-prep.html",
    summary: "Use manganese dioxide as a catalyst to accelerate O₂ release."
  },
  {
    id: "candle-observe",
    title: "Observing a Burning Candle",
    badge: "core",
    type: "inquiry",
    unit: "Unit 1 — Lab Techniques",
    formula: "Paraffin + O\u2082 \u2192 CO\u2082 + H\u2082O",
    interactive: true,
    file: "experiments/candle-observe.html",
    summary: "Record observations of the wax, wick, flame, and combustion products."
  },
  {
    id: "acid-base-salt",
    title: "Composition of Acids, Bases & Salts",
    badge: "theory",
    type: "theory",
    unit: "Unit 10 — Acids, Bases & Salts",
    formula: "H\u207A / OH\u207B / cation+anion",
    interactive: false,
    file: "experiments/acid-base-salt.html",
    summary: "Classify common substances and predict their ionic species."
  },
  {
    id: "mass-conservation",
    title: "Law of Conservation of Mass",
    badge: "core",
    type: "inquiry",
    unit: "Unit 5 — Conservation of Mass",
    formula: "\u03A3 m(reactants) = \u03A3 m(products)",
    interactive: true,
    file: "experiments/mass-conservation.html",
    summary: "Weigh a sealed flask before and after a reaction to confirm Lavoisier's law."
  },
  {
    id: "metal-activity",
    title: "Activity Series of Metals",
    badge: "core",
    type: "interactive",
    unit: "Unit 8 — Metals & Their Compounds",
    formula: "K > Ca > Na > Mg > Al > Zn > Fe > (H) > Cu > Ag > Au",
    interactive: true,
    file: "experiments/metal-activity.html",
    summary: "Drop metals into acids or salt solutions and rank their reactivity."
  },
  {
    id: "sulfur-burn",
    title: "Burning Sulfur in Air and in Oxygen",
    badge: "core",
    type: "demo",
    unit: "Unit 2 — Air & Oxygen",
    formula: "S + O\u2082 \u2192 SO\u2082",
    interactive: false,
    file: "experiments/sulfur-burn.html",
    summary: "Compare the pale blue flame in air with the bright violet flame in O₂."
  },
  {
    id: "h2o2-decompose",
    title: "Decomposition of Hydrogen Peroxide",
    badge: "core",
    type: "inquiry",
    unit: "Unit 2 — Air & Oxygen",
    formula: "2 H\u2082O\u2082 \u2192 2 H\u2082O + O\u2082\u2191  (MnO\u2082 cat.)",
    interactive: false,
    file: "experiments/h2o2-decompose.html",
    summary: "Use MnO₂ as a catalyst to release O₂ from peroxide at room temperature."
  },
  {
    id: "soft-hard-water",
    title: "Telling Soft & Hard Water Apart with Soap",
    badge: "core",
    type: "theory",
    unit: "Unit 4 — Natural Resources",
    formula: "Ca\u00B2\u207A / Mg\u00B2\u207A in water",
    interactive: false,
    file: "experiments/soft-hard-water.html",
    summary: "Compare lather behavior; hard water gives scum, soft water gives foam."
  },
  {
    id: "simple-distillation",
    title: "Simple Laboratory Distillation",
    badge: "core",
    type: "theory",
    unit: "Unit 4 — Natural Resources",
    formula: "Boil + condense to purify",
    interactive: false,
    file: "experiments/simple-distillation.html",
    summary: "Walk through a labeled apparatus diagram for water distillation."
  }
];
