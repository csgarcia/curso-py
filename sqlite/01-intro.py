import sqlite3

# generate a connection
# if file does not exist, it will be created
conn = sqlite3.connect("sqlite/app.db")


# remember always to close the connection
conn.close()
