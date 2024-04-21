#!/usr/bin/python3
'''Script that print something'''
from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_1():
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def display_2():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_3(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_4(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_5(n):
    return f"{n} is a number"


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_6(n):
    if ((n % 2) == 0):
        message = f'{n} is even'
        return render_template('6-number_odd_or_even.html', message=message)
    else:
        message = f'{n} is odd'
        return render_template('6-number_odd_or_even.html', message=message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
