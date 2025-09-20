from flask import Flask, render_template
from parser_class import ParseData

app = Flask(__name__)
parse_date = ParseData()


@app.route('/')
def print_news():
	news = parse_date.return_news_from_file()
	return render_template('index.html', news=news)


if __name__ == '__main__':
	app.run(debug=True)