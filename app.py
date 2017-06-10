# encoding=utf8 
from flask import Flask, jsonify, render_template
from textblob import TextBlob
import translate as ts
import os


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/search/<file_name>')
def search(file_name):
    with open('static/en-us/' + file_name, 'r') as srt:
        response = srt.readlines()
    return " ".join(response)


@app.route('/translate/<file_name>')
def translate(file_name):
    return ts.translate(file_name)


if __name__ == "__main__":
    port=int(os.getenv('PORT'))
    host=os.getenv('IP')
    app.run(port=port, host=host, debug=True)
