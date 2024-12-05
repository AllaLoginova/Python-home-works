import sqlite3

with sqlite3.connect('bot_todo.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         telegram_id INTEGER
         )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS task (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT,
         user_id INTEGER NOT NULL,
         FOREIGN KEY (user_id) REFERENCES user (telegram_id) ON DELETE CASCADE
         )""")