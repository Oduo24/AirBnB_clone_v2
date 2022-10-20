#!/usr/bin/python3
"""2-c_route Module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_page():
    """Displays 'Hello HBNB!' upon visiting root page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Displays 'HBNB' upon visiting /hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_page(text):
    """Displays 'C (text variable with spaces instead of _'s)'
        upon visiting /c/<text> page
        (text is optional)"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    """Displays Python followed by the value of the text variable
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route('/number/<n>', strict_slashes=False)
def is_integer(n):
    """Determines if n is an integer
    """
    if isdigit(n):
        return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
