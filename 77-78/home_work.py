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


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)

    def add_note(self, note, raiting, user_id):
        with self.con as con:
            cur = con.cursor()
            cur.execute('INSERT INTO note (name, raiting, user_id) VALUES (?, ?, ?)', (note, raiting, user_id))
            
    def get_one_note(self, note_id, user_id):
        # with self.con as con:
            cur = self.con.cursor()
            cur.execute('SELECT name, raiting FROM note WHERE ID = ? AND user_id = ?', (note_id, user_id))
            row = cur.fetchall()
            return row

    def get_all_notes(self, user_id):
        # with self.con as con:
            cur = self.con.cursor()
            cur.execute('SELECT * FROM note WHERE user_id = ?', (user_id,))
            rows = cur.fetchall()
            return rows

    def get_most_popular_notes(self, user_id):
        # with self.con as con:
            cur = self.con.cursor()
            cur.execute('SELECT name FROM note WHERE raiting > 3 and user_id = ?', (user_id,))
            rows = cur.fetchall()
            return rows

    def delete_all_notes(self, user_id):
        with self.con as con:
            cur = con.cursor()
            cur.execute('DELETE FROM note WHERE user_id = ?', (user_id,))

    def __del__(self):
        print('Соединение закрыто')
        self.con.close()


db = Database('notes.db')

name = input('Введи имя для авторизации: ')
password = input('Введи пароль: ')

db_name = 'notes.db'

auth = False
with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    row = cur.execute('SELECT * FROM users WHERE name = ? and password = ?', (name, password))
    res = row.fetchone()

    if res:
        auth = True
        user_id = res[0]
        print('Вы авторизированы')
    else:
        print('Неверный логин или пароль')

while True and auth:
    print('Что хотите сделать?')
    print('1 - прочитать все заметки')
    print('2 - прочитать одну заметку')
    print('3 - добавить заметку')
    print('4 - прочитать самые популярные заметки')
    print('5 - удалить все заметки')
    print('q - выход')

    res = input('Введи номер ')

    if res == '1':
        rows = db.get_all_notes(user_id)
        print('Вот все заметки 👁️')
        for row in rows:
            print(f"Название: {row[1]}, Рейтинг: {row[2]}")

    if res == '2':
        note_id = input('Введите id заметки ')
        print('Вот ваша заметка 😎')
        result = db.get_one_note(note_id, user_id)
        print(f"Название: {result[0][0]}, Рейтинг: {result[0][1]}")

    if res == '3':
        text_note = input('Введи текст заметки ')
        rating_note = input('Введи рейтинг заметки ')
        db.add_note(text_note, rating_note, user_id)
        print('Заметка добавлена 🌞')

    if res == '4':
        notes = db.get_most_popular_notes(user_id)
        print('Вот самые популярные заметки ➡️')
        for note in notes:
            print(*note)

    if res == '5':
        db.delete_all_notes(user_id)
        print('Вы всё удалили 😢')

    if res == 'q':
        break
