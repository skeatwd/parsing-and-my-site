import sqlite3
from parser_class import ParseData
from datetime import datetime

news = ParseData().get_list_news()

'''
def create_table(news):
    """В бд можно объединить время, которое берется с сайта с датой,
    которая создается в get_list_news(). Можно сделать так,
    а можно так и добавлять отдельно дату и время и просто если 
    новостям болешь недели удалять"""
    '''
class DatabaseManager():

    def __init__(self, news_list) -> None:
        self.news_list = news_list

    def create_table(self):
        conn = sqlite3.connect(r'data/database.db')
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS News (
                    id INTEGER PRIMARY KEY,
                    description TEXT NOT NULL,
                    time TEXT NOT NULL,
                    date TEXT NOT NULL,
                    href TEXT NOT NULL)""")
        
        conn.commit()
        conn.close()

    def delete_data(self):
        pass

    def append_data(self):
        conn = sqlite3.connect(r'data/database.db')
        cur = conn.cursor()
        for news in self.news_list:
            description = news[0]
            time_news = news[1]
            date = news[2].strftime('%Y-%m-%d')
            href = news[3]
            conn.execute('INSERT INTO News (description, time, date, href) VALUES (?, ?, ?, ?)', (description, time_news, date, href))

        conn.commit()
        conn.close()

    def get_data(self):
        pass


d = DatabaseManager(news)
d.create_table()
d.append_data()