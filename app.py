from flask import Flask, jsonify, render_template
from textblob import TextBlob

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
    return file_name


@app.route('/api/v1/sentiment/<message>')
def sentiment(message):
    text = TextBlob(message)

    text.polarity = 0.3

    response = {'polarity': text.polarity, 'subjectivity': text.subjectivity}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
