import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:
    # cursor is used to execute SQL commands
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users ")
    users = cursor.fetchall()
    print(users)
