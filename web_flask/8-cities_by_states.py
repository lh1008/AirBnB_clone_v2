#!/usr/bin/python3
""" Module script that startsa Flask web application """
from flask import Flask, escape, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def clo_se(e):
    """ Method to remove the current SQLAlchemy Session """
    return storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def main():
    """ Method to display a HTML page """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
