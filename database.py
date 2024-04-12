import sqlite3
import uuid


class database:
    def __init__(self, name="url.db"):
        self.name = name
        conn = sqlite3.connect(name)
        cursor = conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS urls (
                           id TEXT PRIMARY KEY,
                           url TEXT NOT NULL
                           )''')
        conn.commit()
        conn.close()

    def store_url(self, url):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()
        url_id = str(uuid.uuid4())
        cursor.execute("INSERT INTO urls (id, url) VALUES (?, ?) ", (url_id, url))
        conn.commit()
        conn.close()
        return url_id

    def get_url(self, url):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM urls WHERE ID = ?", url)
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return None
