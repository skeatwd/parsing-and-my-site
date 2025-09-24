from flask import Flask, render_template
from parser_class import ParseData
from datetime import datetime, timedelta

app = Flask(__name__)
parse_date = ParseData()



@app.route('/')
@app.route('/index.html')
def print_news():
	date = datetime.now().date()
	news = parse_date.get_news_from_date(date)

	return render_template('index.html', news=news, date=date.strftime('%d.%m.%Y'))

@app.route('/monday.html')
def monday():
	date = datetime.now().date()
	date_one = date - timedelta(days=7)
	news = parse_date.get_news_from_date(date_one)

	return render_template('monday.html', date=date_one.strftime('%d.%m.%Y'), news=news)

@app.route('/tuesday.html')
def tuesday():
	date = datetime.now().date()
	date_one = date - timedelta(days=6)
	news = parse_date.get_news_from_date(date_one)

	return render_template('tuesday.html', date=date_one.strftime('%d.%m.%Y'), news=news)

@app.route('/wednesday.html')
def wednesday():
	date = datetime.now().date()
	date_one = date - timedelta(days=5)
	news = parse_date.get_news_from_date(date_one)

	return render_template('wednesday.html', date=date_one.strftime('%d.%m.%Y'), news=news)

@app.route('/thursday.html')
def thursday():
	date = datetime.now().date()
	date_one = date - timedelta(days=4)
	news = parse_date.get_news_from_date(date_one)

	return render_template('thursday.html', date=date_one.strftime('%d.%m.%Y'), news=news)

@app.route('/friday.html')
def friday():
	date = datetime.now().date()
	date_one = date - timedelta(days=3)
	news = parse_date.get_news_from_date(date_one)

	return render_template('friday.html', date=date_one.strftime('%d.%m.%Y'), news=news)

@app.route('/saturday.html')
def saturday():
	date = datetime.now().date()
	date_one = date - timedelta(days=2)
	news = parse_date.get_news_from_date(date_one)

	return render_template('saturday.html', date=date_one.strftime('%d.%m.%Y'), news=news)

@app.route('/sunday.html')
def sunday():
	date = datetime.now().date()
	date_one = date - timedelta(days=1)
	news = parse_date.get_news_from_date(date_one)

	return render_template('sunday.html', date=date_one.strftime('%d.%m.%Y'), news=news)


if __name__ == '__main__':
	parse_date.delete_news()
	app.run(debug=True)

# Для h1, nav установить другой шрифт, не наклоненный!