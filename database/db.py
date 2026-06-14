import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("history.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result TEXT NOT NULL
        )
        """)

        self.conn.commit()

    def save(self, expression, result):
        self.cursor.execute(
            "INSERT INTO history (expression, result) VALUES (?, ?)",
            (expression, str(result))
        )
        self.conn.commit()

    def get_history(self):
        self.cursor.execute("""
            SELECT expression, result
            FROM history
            ORDER BY id DESC
        """)
        return self.cursor.fetchall()

    def clear_history(self):
        self.cursor.execute("DELETE FROM history")
        self.conn.commit()

    def close(self):
        self.conn.close()