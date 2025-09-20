import requests
from bs4 import BeautifulSoup
import time
import random


time.sleep(random.uniform(0.5, 1.5))
response = requests.get('https://lenta.ru').text
soup = BeautifulSoup(response, 'html.parser')

div_topnews_column = soup.find_all('div', class_='topnews__column')


def return_news():
	news = []   # ["описание", "время", "ссылка"]

	for column in div_topnews_column:
		all_a = column.find_all('a')
		for a in all_a:
			href = a['href']
			time_news = a.find('time').text
			for t in a.find_all('time'):
				t.decompose()
			description = a.text

			news.append([description, time_news, href])

	return news[:-1]


print(return_news())