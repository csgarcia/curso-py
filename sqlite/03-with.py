import sqlite3

# generate a connection with "with" statement

with sqlite3.connect("sqlite/app.db") as conn:
    # cursor is used to execute SQL commands
    cursor = conn.cursor()

    cursor.execute("""
               CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, name VARCHAR(100));
               """)

    # with this __exit__ method is called automatically 
    # the changes are committed automatically and the connection is closed
