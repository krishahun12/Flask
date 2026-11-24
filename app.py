"""Minimal Flask web application returning a greeting at the root endpoint."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a plain text greeting for the root route."""
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
