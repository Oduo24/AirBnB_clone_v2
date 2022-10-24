#!/usr/bin/python3
"""List of States"""

from flask import Flask, render_template
from models.state import State
from models.storage import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """Query the db for the list of states
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """Removes the current mysql session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
