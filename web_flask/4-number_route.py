#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask

app = Flask(__name__)
"""Craetes an instance of flask."""

app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Returns Hello HBNB! on the home page"""

    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays HBNB on the hbnb page"""

    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """
    The c page, displays "C" followed by the value
    of the text variable(replace underscore _ symbol
    with space )
    """
    new_text = text.replace('_', ' ')

    return "C {}".format(new_text)


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """
    The python page, displays Python followed by the
    value of the text variable (replace underscore _ symbols
    with a space )
    """
    new_text = text.replace('_', ' ')

    return "Python {}".format(new_text)


@app.route('/number/<int:n>')
def number(n):
    """The number page."""

    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
