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
        response = []
        lines = srt.readlines()
        ex_en_lines = []
        for l in lines:
            #exclude English lines
            ex_en_lines.append("\n") if ts.check_contain_english(l) else ex_en_lines.append(l)
        
        in_en_str = " ".join(lines)
        ex_en_str = " ".join(ex_en_lines)
        
        response.extend((in_en_str, ex_en_str))
        print jsonify(response)
    return jsonify(response)


@app.route('/translate/<file_name>')
def translate(file_name):
    return ts.translate(file_name)


if __name__ == "__main__":
    port=int(os.getenv('PORT'))
    host=os.getenv('IP')
    app.run(port=port, host=host, debug=True)
