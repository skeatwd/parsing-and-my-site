from flask import Flask, render_template
from parser_class import ParseData
from datetime import datetime

app = Flask(__name__)
parse_date = ParseData()


def return_date():
	pass


@app.route('/')
@app.route('/ index.html')
def print_news():
	date = datetime.now().date().strftime('%d.%m.%Y')
	news = parse_date.get_news_from_date(date)
	return render_template('index.html', news=news, currentdate=date)

@app.route('/monday.html')
def monday():
	return render_template('monday.html')

@app.route('/tuesday.html')
def tuesday():
	return render_template('tuesday.html')

@app.route('/wednesday.html')
def wednesday():
	return render_template('wednesday.html')

@app.route('/thursday.html')
def thursday():
	return render_template('thursday.html')

@app.route('/friday.html')
def friday():
	return render_template('friday.html')

@app.route('/saturday.html')
def saturday():
	return render_template('saturday.html')

@app.route('/sunday.html')
def sunday():
	return render_template('sunday.html')


if __name__ == '__main__':
	app.run(debug=True)