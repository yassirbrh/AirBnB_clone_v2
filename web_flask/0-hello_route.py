#!/usr/bin/python3
'''
	IMPORT Modules.
'''
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hbnb_hello():
	return 'Hello HBNB!'

if __name__ == '__main__':
	app.run()
