#!/usr/bin/python3
""" Module script that startsa Flask web application """
from flask import Flask
app = Flask(__name__)



@app.route('/', strict_slashes=False)
def main():
    """ Method that returns displayed message """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
