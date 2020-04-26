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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>')
def main(id=None):
    """ Method to display a HTML page """
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
