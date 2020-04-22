#!/usr/bin/python3
""" Module script that startsa Flask web application """
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """ Method that returns displayed message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Method routing to hbnb decorator """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ Method that displays C followed by value """
    return 'C %s' % escape(text.replace("_", " "))


@app.route('/python/', defaults={'text': None})
@app.route('/python/<text>')
def py_text(text):
    """ Method that displays Python followed by value """
    if text is None:
        return 'Python %s' % escape("is cool")
    elif text:
        return 'Python %s' % escape(text.replace("_", " "))


@app.route('/number/<int:n>')
def n_int(n):
    """ Method that displays n is an int """
    return '%d is a number' % n


@app.route('/number_template/')
@app.route('/number_template/<int:n>')
def tem_plate(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/')
@app.route('/number_odd_or_even/<int:n>')
def odd_even(n=None):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
