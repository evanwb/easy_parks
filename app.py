from flask import Flask, Response, render_template, request, flash, get_flashed_messages
from flask_session.__init__ import Session
from threading import Thread 
from api import *
from util import *
import os

 
app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Search Page
@app.route('/data', methods=['GET', 'POST'])
def user_input():
    url = request.remote_addr
	
    text = request.form['text']
    if text.isdigit():
        text = zip_to_state(text)
    state = get_state_name(text)
    total = park_total(text)
    parks = state_search(text)
    return render_template('search.html', total=total, parks=parks)


# Park Page
@app.route('/park', methods=['GET', 'POST'])
def park_page():
    park_code = request.query_string.decode()
    park = park_search(park_code)
    return render_template('park.html', park=park)


# Activity Picker
@app.route('/activites', methods=['GET', 'POST'])
def show_acts():
    acts = get_acts()
    return render_template('acts.html', acts=acts)

# Activity Page
@app.route('/act', methods=['GET', 'POST'])
def act_page():
    act_id = request.query_string.decode()
    codes, name = act_search(act_id)
    parks = []
    for code in codes:
        parks.append(park_search(code))

    return render_template('search.html', total='Best parks for {}'.format(name), parks=parks)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
