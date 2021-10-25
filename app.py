from flask import Flask, Response, render_template, request, flash, get_flashed_messages
from flask_session.__init__ import Session
from threading import Thread 
from api import *
from util import *
import os

 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['GET', 'POST'])
def user_input():
    text = request.form['text'].upper()
    state = get_state_name(text)
    body = park_total(text)
    parks = state_search(text)
    for park in parks:
        '''flash('{}\r'.format(park['name']))
        flash('{}\r'.format(park['code']))
        flash('{}\r'.format(park['desc']))
        acts = park['act']
        for act in acts:
            flash(act['name'])'''
        flash('<div class=\"container\"><p class=\"name\"> {} </p></div>)'.format(park))
        flash('\r\n')
    
    #return '<html><head>  <title> Easy Parks </title></head><body><h1> {} </h1><h3> {} </h3></body></html>'.format(park_total(text), get_flashed_messages()) 
    return render_template('search.html', parks=parks)

@app.route('/park', methods=['GET', 'POST'])
def park_page():
    park_code = request.query_string.decode()
    park = park_search(park_code)
    return render_template('park.html', park=park)

app.config.update(SECRET_KEY=os.urandom(24))
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
