from flask import Flask, Response, render_template, request
import api

from threading import Thread  
app = Flask(__name__)
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/data', methods=['GET', 'POST'])
def user_input():
    text = request.form['text'].lower()
    body = api.park_total(text)
    
    return render_template('search.html', term=text.upper(), body=body)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
