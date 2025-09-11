import sqlite3

# generate a connection
# if file does not exist, it will be created
conn = sqlite3.connect("sqlite/app.db")

# cursor is used to execute SQL commands
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, name VARCHAR(100));
               """)
# always commit the changes
conn.commit()

# remember always to close the connection
conn.close()
