import sqlite3

with sqlite3.connect('notes.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         password TEXT
         )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS note (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         raiting INTEGER DEFAULT 0,
         user_id INTEGER NOT NULL,
         CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES users (ID)
         )""")

    cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', ('Алла', 123))
    cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', ('Татьяна', 1234))
    cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', ('Николай', 12345))
