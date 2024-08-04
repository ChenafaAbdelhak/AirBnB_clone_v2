#!/usr/bin/python3
"""starts flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    function that returns Hello HBNB!.
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """
    function that returns HBNB.
    """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """
    function that returns formatted message.
    """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.url_map.sctict_stashes = False
    app.run(host="0.0.0.0", port=5000)
