import sqlite3

# generate a connection with "with" statement

with sqlite3.connect("sqlite/app.db") as conn:
    # cursor is used to execute SQL commands
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (id, name) VALUES (? , ?);", (1, "Carlos"))
    # passing parameters is important to avoid SQL injection

    # with this __exit__ method is called automatically
    # it is not necessary to commit the changes manually and close the connection
