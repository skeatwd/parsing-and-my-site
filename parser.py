import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin
import csv
from datetime import datetime
import os


def return_news():
	time.sleep(random.uniform(0.5, 1.5))
	response = requests.get('https://lenta.ru').text
	soup = BeautifulSoup(response, 'html.parser')

	div_topnews_column = soup.find_all('div', class_='topnews__column')

	news = []   # ["описание", "время", "ссылка"]

	for column in div_topnews_column:
		all_a = column.find_all('a')    # type: ignore
		for a in all_a:
			href = a.get('href')    # type: ignore
			if href:
				href = urljoin('https://lenta.ru', href)    # type: ignore

			time_tag = a.find('time')    # type: ignore
			time_news = time_tag.text if time_tag else 'None'    # type: ignore

			for t in a.find_all('time'):    # type: ignore
				t.decompose()

			description = a.text.strip()

			news.append([description, time_news, datetime.now().date() ,href])

	return news[:-1]


def write_to_file(news):
	links = []
	empty_file = True if os.path.getsize('data.csv') == 0 else False

	if not empty_file:
		with open('data.csv', 'r', encoding='utf-8') as file_read:
			data_for_file = list(csv.reader(file_read))
			for item in data_for_file:
				links.append(item[3])

	with open('data.csv', 'a', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		for row in news:
			if row[3] not in links:
				writer.writerow(row)


n = return_news()
write_to_file(n)
