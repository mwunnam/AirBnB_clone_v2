#!/usr/bin/python3
'''Script that print something'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_1():
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def display_2():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', defaults={'text': 'is cool'},
           strict_slashes=False)
def display(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
