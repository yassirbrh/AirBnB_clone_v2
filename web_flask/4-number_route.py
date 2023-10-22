#!/usr/bin/python3
# Script that launches Flask web application
'''
    IMPORT Modules.
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.run()
