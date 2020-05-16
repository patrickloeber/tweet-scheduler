from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    tweets = []
    n_open_tweets = 0
    return render_template('base.html', tweets=tweets, n_open_tweets=n_open_tweets)