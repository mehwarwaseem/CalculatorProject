import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("history.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT,
            result TEXT
        )
        """)
        self.conn.commit()

    def save(self, expression, result):
        self.cursor.execute(
            "INSERT INTO history (expression, result) VALUES (?, ?)",
            (expression, str(result))
        )
        self.conn.commit()
