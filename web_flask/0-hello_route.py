#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask

app = Flask(__name__)
"""An instance of Flask."""


@app.route('/', strict_slashes=False)
def index():
    """This function returns Hello HBNB! in the index/home page."""

    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
