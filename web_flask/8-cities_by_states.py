"""Cities by states"""
#!/usr/bin/python3

from flask import FLask
from models import storage
from sqlalchemy import render_template
from models.state import State

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Retrieves all the cities for every state
    """
    states = storage.all(State).values()
    my_cities = list()

    for state in states:
        for city in state.cities:
            my_cities.append(city)

    return render_template('8-cities_by_states.html',my_state=states, my_cities=my_cities)

@app.teardown_appcontext
def close_session():
    """Closses the current session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
