import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin
import csv
from datetime import datetime, date
import os

class ParseData:

    def __init__(self) -> None:
        self.filename = 'data.csv'

    def get_list_news(self):
        time.sleep(random.uniform(0.5, 1.5))

        response = requests.get('https://lenta.ru').text
        soup = BeautifulSoup(response, 'html.parser')
        div_topnews_columns = soup.find_all('div', class_='topnews__column')

        news = []

        for column in div_topnews_columns:
            all_a = column.find_all('a')    # type: ignore

            for a in all_a:
                href = a.get('href')    # type: ignore
                if href:
                    href = urljoin('https://lenta.ru', href)   # type: ignore

                time_tag = a.find('time')   # type: ignore
                time_news = time_tag.text if time_tag else 'None'   # type: ignore

                for t in a.find_all('time'):    # type: ignore
                    t.decompose()

                description = a.text.strip()

                news.append([description, time_news, str(datetime.now().date()) ,href])
                
        return news[:-1]   
    
    def write_to_file(self, news):
        links = []
        empty_file = True if os.path.getsize(self.filename) == 0 else False

        if not empty_file:
            with open(self.filename, 'r', encoding='utf-8') as file_read:
                data_for_file = list(csv.reader(file_read))
                for item in data_for_file:
                    links.append(item[3])
        
        with open(self.filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in news:
                if row[3] not in links:
                    writer.writerow(row)
    
    def get_news_from_date(self, date):
        result = []
        date = str(date)

        if os.path.getsize(self.filename) > 0 and date != datetime.now().date():
            with open(self.filename, 'r', encoding='utf-8') as file_read:
                reader = list(csv.reader(file_read))

                for row in reader:
                    if row[2] == date:
                        result.append(row)
            
        else:
            news = self.get_list_news()
            self.write_to_file(news)

            for row in news:
                if row[2] == date:
                    result.append(row)


        result_sorted = sorted(result, key=lambda news: news[1], reverse=True)

        return result_sorted
    
    def delete_news(self):
        date_now = date.today()
        fresh_news = []

        with open(self.filename, 'r', encoding='utf-8') as file_read:
            reader = csv.reader(file_read)

            for row in reader:
                date_from_row = datetime.strptime(row[2], '%Y-%m-%d').date()
                difference = (date_now - date_from_row).days
                if difference < 7:
                    fresh_news.append(row)

        with open(self.filename, 'w', encoding='utf-8', newline='') as file_write:
            writer = csv.writer(file_write)
            writer.writerows(fresh_news)