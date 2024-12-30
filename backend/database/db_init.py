import sqlite3

from common.constants.database import DATABASE_NAME

# create required table if table doesn;t exists
def db_init():
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            slot TEXT NOT NULL
        )
        """)
        cursor.close()
        conn.commit()
        conn.close()