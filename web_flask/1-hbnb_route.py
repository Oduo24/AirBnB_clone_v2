#!/usr/bin/python3
"""Runs a flask with two routes"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_bnb():
    """Reurns 'Hello HBNB on the root domain'
    """
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
