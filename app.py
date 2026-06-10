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
# files in PUBLIC_FILES below are ever served (no source/dotfile exposure).
app = Flask(__name__, static_folder=None)

# Only these files are exposed; everything else returns 404.
PUBLIC_FILES = {
    "index.html",
    "styles.css",
    "script.js",
    "README.md",
    "Christian-Sebo-Resume.pdf",
}


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:filename>")
def assets(filename):
    if filename in PUBLIC_FILES:
        return send_from_directory(".", filename)
    return ("Not Found", 404)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
