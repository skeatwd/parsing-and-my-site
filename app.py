from flask import Flask, render_template
from parser import return_news

app = Flask(__name__)
news = return_news()


@app.route('/')
def print_news():
	return render_template('index.html', news=news)


