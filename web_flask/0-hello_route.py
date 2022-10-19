#!/usr/bin/python3
"""Starts a basic flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def HelloHBNB():
    """Defines root route response
    """
    return 'Hello HBNB!'
