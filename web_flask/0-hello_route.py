#!/usr/bin/python3
"""Starts a basic flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Defines root route response
    """
    return 'Hello HBNB!'

if __name__ = '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
