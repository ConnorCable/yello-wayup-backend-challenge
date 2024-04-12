import sqlite3
import uuid


class database:
    def __init__(self):
        self.conn = sqlite3.connect('url.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS urls (
                           id INTEGER PRIMARY KEY,
                           url TEXT NOT NULL,
                           )''')

    def store_url(self, url):
        url_id = str(uuid.uuid4())
        self.cursor.execute("INSERT INTO urls (id, url) VALUES (?, ?) ", (url_id, url))

    def get_url(self, url):
        self.cursor.execute("SELECT url FROM urls WHERE ID = ?", url)
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return "No such url"
