import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin


def return_news():
	time.sleep(random.uniform(0.5, 1.5))
	response = requests.get('https://lenta.ru').text
	soup = BeautifulSoup(response, 'html.parser')

	div_topnews_column = soup.find_all('div', class_='topnews__column')

	news = []   # ["описание", "время", "ссылка"]

	for column in div_topnews_column:
		all_a = column.find_all('a')
		for a in all_a:
			href = a.get('href')
			if href:
				href = urljoin('https://lenta.ru', href)

			time_tag = a.find('time')
			time_news = time_tag.text if time_tag else 'None'

			for t in a.find_all('time'):
				t.decompose()

			description = a.text.strip()

			news.append([description, time_news, href])

	return news
