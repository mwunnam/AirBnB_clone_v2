#!/usr/bin/python3
'''This is a script that displays text'''


from flask import Flask


@app.route('/', strict_slashes=False)
def display_1():
    '''
    Function to display "HBNH"
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_2():
    '''
    Function to display "HBNH"
    '''
    return "HBNH"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)