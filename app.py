from flask import Flask, render_template
from parser import return_news

app = Flask(__name__)


@app.route('/')
def print_news():
	news = return_news()
	return render_template('index.html', news=news)


if __name__ == '__main__':
	app.run(debug=True)