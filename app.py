from flask import Flask, Response, render_template, request
from search import read_input

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('home.html')

@app.route('/parse_data', methods=['GET', 'POST'])
def user_input():
    text = request.form['text']
    processed_text = text.upper()
    return (processed_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, threaded=True)
