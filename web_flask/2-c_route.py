#!/usr/bin/python3
'''Script that start  flask web application '''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_1():
    """ Function displays a text """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_2():
    """ Function displays a text """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Displays "C" and the content of <text>"""
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
