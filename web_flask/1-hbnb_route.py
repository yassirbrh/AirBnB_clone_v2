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


if __name__ == '__main__':
    app.run()
