"""
Christian Sebo — Portfolio
A minimal Flask server that hosts the static portfolio site.

Run locally:
    pip install -r requirements.txt
    python app.py            # → http://localhost:3000

Production (Railway / gunicorn):
    gunicorn app:app --bind 0.0.0.0:$PORT
"""
import os

from flask import Flask, send_from_directory

# static_folder=None disables Flask's blanket static handler so that only the
# files in PUBLIC_FILES below (and whitelisted assets) are ever served.
app = Flask(__name__, static_folder=None)

# Exact files exposed at the site root; everything else returns 404.
PUBLIC_FILES = {
    "index.html",
    "styles.css",
    "script.js",
    "README.md",
    "favicon.svg",
    "og-image.png",
    "jean-demo.html",
    "Christian-Sebo-Resume.pdf",
}

# Project media (screenshots / GIFs) live in ./assets and are served read-only.
ASSETS_DIR = "assets"
ALLOWED_ASSET_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/assets/<path:filename>")
def asset(filename):
    # Flat directory only; reject traversal and disallowed types.
    if "/" in filename or filename.startswith("."):
        return _not_found()
    if os.path.splitext(filename)[1].lower() not in ALLOWED_ASSET_EXT:
        return _not_found()
    try:
        return send_from_directory(ASSETS_DIR, filename)
    except Exception:
        return _not_found()


@app.route("/<path:filename>")
def root_file(filename):
    if filename in PUBLIC_FILES:
        return send_from_directory(".", filename)
    return _not_found()


@app.route("/health")
def health():
    return {"status": "ok"}, 200


def _not_found():
    return NOT_FOUND_HTML, 404


@app.errorhandler(404)
def handle_404(_e):
    return NOT_FOUND_HTML, 404


NOT_FOUND_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>404 — Page not found · Christian Sebo</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<style>
  :root { color-scheme: dark; }
  * { margin: 0; box-sizing: border-box; }
  body {
    min-height: 100vh; display: grid; place-items: center; text-align: center;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: #0a0b10; color: #e7e9f2; padding: 24px;
    background-image:
      radial-gradient(circle at 30% 30%, rgba(124,123,255,.18), transparent 55%),
      radial-gradient(circle at 70% 40%, rgba(56,232,200,.12), transparent 50%);
  }
  .code {
    font-size: clamp(4rem, 18vw, 9rem); font-weight: 800; line-height: 1;
    background: linear-gradient(120deg, #7c7bff, #38e8c8 50%, #ff7ad9);
    -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
  }
  h1 { font-size: 1.4rem; margin: 18px 0 8px; }
  p { color: #9aa0b5; max-width: 42ch; margin: 0 auto 28px; }
  a {
    display: inline-block; padding: 12px 24px; border-radius: 10px; font-weight: 600;
    color: #06070b; text-decoration: none;
    background: linear-gradient(120deg, #7c7bff, #38e8c8 50%, #ff7ad9);
  }
</style>
</head>
<body>
  <main>
    <div class="code">404</div>
    <h1>This page wandered off.</h1>
    <p>The link may be broken or the page may have moved.</p>
    <a href="/">← Back to home</a>
  </main>
</body>
</html>"""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
