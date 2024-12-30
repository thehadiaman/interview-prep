from common.constants.database import DATABASE_NAME
import sqlite3

# Execute the sql query in SQLite local database
def execute_query(query: str, params=None):
    if params is None:
        params = []
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)

    rows = cursor.fetchall()

    if len(rows) == 0:
        cursor.close()
        conn.commit()
        conn.close()
        return []

    # Convert the response from database into dictionary
    columns = [description[0] for description in cursor.description]
    result = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.commit()
    conn.close()

    return result
