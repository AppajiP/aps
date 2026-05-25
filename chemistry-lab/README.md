# Virtual Chemistry Lab

A self-contained, browser-based **virtual chemistry lab** with a searchable
resource gallery and 34 interactive experiment pages — built with plain HTML,
CSS and JavaScript. No build step, no dependencies, no server required.

## Quick start

Open `index.html` in any modern browser (Chrome, Firefox, Edge, Safari ≥ 14).
Every experiment is just an `.html` file that links back to the gallery, so
the entire lab works offline from the file system.

If you prefer to serve it over HTTP for a friendlier URL bar:

```bash
cd chemistry-lab
python3 -m http.server 8000
# open http://localhost:8000
```

## Layout

```
chemistry-lab/
├── index.html              # resource gallery / home page
├── styles/
│   └── main.css            # shared stylesheet (dark theme)
├── scripts/
│   ├── experiments.js      # master registry of all experiments
│   ├── main.js             # gallery rendering + search/filter
│   ├── exp-utils.js        # canvas / animation helpers
│   └── theory-page.js      # shared template for static notes pages
├── experiments/            # 34 individual experiment pages
│   ├── kmno4-decomposition.html   (interactive)
│   ├── iron-in-oxygen.html        (interactive)
│   ├── electrolysis-water.html    (interactive)
│   ├── oxygen-in-air.html         (interactive)
│   ├── fountain-nh3.html          (interactive)
│   ├── gold-foil.html             (interactive)
│   ├── atomic-structure.html      (interactive)
│   ├── balance-equations.html     (interactive)
│   ├── co2-prep.html              (interactive)
│   ├── mass-conservation.html     (interactive)
│   ├── metal-activity.html        (interactive)
│   ├── elements-battle.html       (interactive quiz)
│   ├── candle-observe.html        (interactive)
│   ├── copper-oxygen-mass.html    (interactive)
│   ├── fire-extinguisher.html     (interactive)
│   ├── dust-explosion.html        (interactive)
│   ├── golden-rain.html           (interactive)
│   └── ... + 17 illustrated theory / study-notes pages
└── assets/                 # reserved for future images
```

## Resource gallery features

- **Card grid** with auto-generated SVG thumbnails — no image assets needed.
- **Full-text search** over titles, formulas and units.
- **Filter chips:** All / Inquiry / Interactive / 3D-Model / Demo / Notes.
- **Counters** for total, interactive and currently-shown experiments.
- **Responsive layout** that collapses to a single column on mobile.

## Experiment page features

Every experiment page follows the same template:

- Breadcrumb back to the library.
- Left column: an interactive `<canvas>` *stage*, controls and a live
  observations panel.
- Right column: theory notes, balanced equations, safety information and
  follow-up questions.

For experiments that are difficult to simulate accurately (e.g. Pharaoh's
serpent or a real flame), an annotated SVG diagram replaces the canvas.

## Topic coverage (Maharashtra / NCERT-style middle-school chemistry)

- Air and oxygen: KMnO₄, KClO₃ + MnO₂, H₂O₂ + MnO₂, oxygen in air, charcoal,
  sulfur and iron burning.
- Water: composition by electrolysis, hardness, distillation.
- Atomic theory: Bohr model, Rutherford's gold foil, periodic-table quiz.
- Conservation of mass: sealed-flask weigh-in, Cu + O₂ mass test, equation
  balancer.
- Carbon: CO₂ preparation and properties, CO reduction of Fe₂O₃,
  candle-flame observations.
- Metals: activity series, fire extinguisher, dust explosion.
- Acids, bases and salts: composition, NaOH/Ca(OH)₂ ageing, H₂SO₄ dilution.
- Demos: golden rain, Pharaoh's serpent, water-drop smoke, iodine
  sublimation, ammonia fountain.

## Adding a new experiment

1. Drop a new file under `experiments/` — copy any existing file as a
   starting point.
2. Add a record at the bottom of `scripts/experiments.js`:

```js
{
  id: "my-new-experiment",
  title: "My new experiment",
  badge: "core",       // or "fun", "ext", "theory"
  type: "inquiry",     // or "interactive", "3d", "demo", "theory"
  unit: "Unit X — Section",
  formula: "A + B → C",
  interactive: true,
  file: "experiments/my-new-experiment.html",
  summary: "One-sentence description."
}
```

The gallery picks it up automatically on next page load.

## Tested in

- Chrome 124, Firefox 125, Safari 17, Edge 124.
- Works opened directly via `file://` — no CORS issues because nothing is
  fetched at runtime.

## License

All code is original and released under the MIT licence.
