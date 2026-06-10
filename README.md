# Christian Sebo — Portfolio

Personal portfolio site for **Christian Sebo**, an IBM-Certified AI Engineer
building practical, reliable generative AI systems with Python, LangChain,
LangGraph, and the Anthropic Claude API.

🔗 **Live:** _enable GitHub Pages to publish (see below)_

## Stack

A fast, dependency-free static site:

- **HTML5** — semantic, single-page layout
- **CSS3** — custom properties, grid/flexbox, responsive, reduced-motion aware
- **Vanilla JS** — scroll reveals, sticky nav, mobile menu, pointer-tracking cards

No build step, no frameworks — just open `index.html`.

## Run locally

```bash
# any static server works; for example:
python3 -m http.server 8000
# then visit http://localhost:8000
```

Or simply open `index.html` in a browser.

## Structure

```
.
├── index.html   # markup & content
├── styles.css   # all styling + responsive rules
├── script.js    # interactions
└── README.md
```

## Deploy with Railway

This repo is Railway-ready. It ships a `package.json` (serves the static site via
[`serve`](https://www.npmjs.com/package/serve) on Railway's `$PORT`) and a
`railway.json` that pins the build/start config.

1. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**.
2. Select this repository and authorize Railway if prompted.
3. Railway auto-detects Node (Nixpacks), runs `npm install`, then `serve -s . -l $PORT`.
4. Open the service → **Settings → Networking → Generate Domain** (or attach a
   custom one). Your site is served at e.g. `https://christiansebo.up.railway.app`.

Local production check:

```bash
npm install
PORT=4173 npm start   # → http://localhost:4173
```

## Deploy with GitHub Pages

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`.
4. Choose the branch and `/ (root)` folder, then **Save**.
5. Your site goes live at `https://<username>.github.io/<repo>/`.

## Customize

- **Content:** edit the sections in `index.html`.
- **Colors:** tweak the CSS custom properties in `:root` at the top of `styles.css`.
- **Projects:** duplicate a `.project` article block to add more.

---

© Christian Sebo · Manchester, NH
