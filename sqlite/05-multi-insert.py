import sqlite3

# generate a connection with "with" statement

with sqlite3.connect("sqlite/app.db") as conn:
    # cursor is used to execute SQL commands
    cursor = conn.cursor()
    users = [(2, "Ana"), (3, "Luis")]
    cursor.executemany(
        "INSERT INTO users (id, name) VALUES (? , ?);", users)
