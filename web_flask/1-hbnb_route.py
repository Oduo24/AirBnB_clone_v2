#!/usr/bin/python3
"""Runs a flask with two routes"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """Displays 'Hello HBNB' upon visiting the root domain
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB upon visiting /hbnb
    """
    return 'HBNB'


if __name__ == '__main__':
    """Main File"""
    app.run(host='0.0.0.0', port=5000)
