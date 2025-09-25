from flask import Flask, render_template
from parser_class import ParseData
from datetime import datetime, timedelta

app = Flask(__name__)
parse_date = ParseData()


def return_date():
	date_now = datetime.now().date()
	dates = []
	for i in range(1, 8):
		date = date_now - timedelta(days=i)
		dates.append(date.strftime('%d.%m.%Y'))

	return dates


@app.route('/')
@app.route('/index.html')
def print_news():
	date = datetime.now().date()
	dates = return_date()
	news = parse_date.get_news_from_date(date)

	return render_template('index.html', news=news, date=date.strftime('%d.%m.%Y'), dates=dates)

@app.route('/monday.html')
def monday():
	dates = return_date()
	date = str(datetime.strptime(dates[0], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)

	return render_template('monday.html', dates=dates, news=news)

@app.route('/tuesday.html')
def tuesday():
	dates = return_date()
	date = str(datetime.strptime(dates[1], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)

	return render_template('tuesday.html', dates=dates, news=news)

@app.route('/wednesday.html')
def wednesday():
	dates = return_date()
	date = str(datetime.strptime(dates[2], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)

	return render_template('wednesday.html', dates=dates, news=news)

@app.route('/thursday.html')
def thursday():
	dates = return_date()
	date = str(datetime.strptime(dates[3], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)

	return render_template('thursday.html', dates=dates, news=news)

@app.route('/friday.html')
def friday():
	dates = return_date()
	date = str(datetime.strptime(dates[4], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)

	return render_template('friday.html', dates=dates, news=news)

@app.route('/saturday.html')
def saturday():
	dates = return_date()
	date = str(datetime.strptime(dates[5], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)
	return render_template('saturday.html', dates=dates, news=news)

@app.route('/sunday.html')
def sunday():
	dates = return_date()
	date = str(datetime.strptime(dates[6], '%d.%m.%Y').date())
	news = parse_date.get_news_from_date(date)

	return render_template('sunday.html', dates=dates, news=news)


if __name__ == '__main__':
	parse_date.delete_news()
	app.run(debug=True)