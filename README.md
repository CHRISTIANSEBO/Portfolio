# Christian Sebo — Portfolio

Personal portfolio site for **Christian Sebo**, an IBM-Certified AI Engineer
building practical, reliable generative AI systems with Python, LangChain,
LangGraph, and the Anthropic Claude API.

🔗 **Live:** _enable GitHub Pages to publish (see below)_

## Stack

A static front end served by a small **Flask** app:

- **HTML5** — semantic, single-page layout
- **CSS3** — custom properties, grid/flexbox, responsive, reduced-motion aware
- **Vanilla JS** — scroll reveals, sticky nav, mobile menu, pointer-tracking cards
- **Flask + gunicorn** — lightweight host that serves the page and exposes a
  `/health` endpoint for platform health checks

## Run locally

```bash
pip install -r requirements.txt

# development server
python app.py            # → http://localhost:3000

# production server (same as Railway uses)
gunicorn app:app --bind 0.0.0.0:3000
```

You can also open `index.html` directly in a browser for a quick look, but the
Flask server is what runs in production.

## Structure

```
.
├── app.py             # Flask server (serves the site + /health)
├── requirements.txt   # Flask, gunicorn
├── Procfile           # web: gunicorn app:app --bind 0.0.0.0:$PORT
├── railway.json       # Railway build/deploy config
├── index.html         # markup & content
├── styles.css         # all styling + responsive rules
├── script.js          # interactions
└── README.md
```

## Deploy with Railway

This repo is Railway-ready. The `railway.json` pins the build/start config and
the Flask app binds to Railway's `$PORT`.

1. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**.
2. Select this repository and authorize Railway if prompted.
3. Railway auto-detects Python (Nixpacks), runs `pip install -r requirements.txt`,
   then `gunicorn app:app --bind 0.0.0.0:$PORT`. Health checks hit `/health`.
4. Open the service → **Settings → Networking → Generate Domain** (or attach a
   custom one). Name the service `christiansebo` to land on
   `https://christiansebo.up.railway.app`.

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
