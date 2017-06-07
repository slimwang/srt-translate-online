from flask import Flask, jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/search')
def search1():
    return search2('hello')


def search2(test):
    return test


@app.route('/api/v1/sentiment/<message>')
def sentiment(message):
    text = TextBlob(message)

    text.polarity = 0.3

    response = {'polarity': text.polarity, 'subjectivity': text.subjectivity}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
