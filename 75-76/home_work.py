import sqlite3

with sqlite3.connect('notes.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS note (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        raiting INTEGER DEFAULT 0
        )""")

def add_note(note, raiting):
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute('INSERT INTO note (name, raiting) VALUES (?, ?)', (note, raiting))
    con.commit()
    con.close()

def get_one_note(note_id):
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute('SELECT name, raiting FROM note WHERE ID = ?', (note_id, ))
    row = cur.fetchall()
    con.close()
    return row

def get_all_notes():
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM note')
    rows = cur.fetchall()
    con.close()
    return rows

def get_most_popular_notes():
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute('SELECT name FROM note WHERE raiting > 3')
    rows = cur.fetchall()
    con.close()
    return rows

# def delete_all_notes():
#     con = sqlite3.connect('notes.db')
#     cur = con.cursor()
#     cur.execute('DELETE FROM note')
#     con.commit()
#     con.close()

while True:
    print('Что хотите сделать?')
    print('1 - прочитать все заметки')
    print('2 - прочитать одну заметку')
    print('3 - добавить заметку')
    print('4 - прочитать самые популярные заметки')
    # print('5 - удалить все заметки')
    print('q - выход')

    res = input('Введи номер ')

    if res == '1':
        rows = get_all_notes()
        print('Вот все заметки 👁️')
        for row in rows:
           print(f"Название: {row[1]}, Рейтинг: {row[2]}")

    if res == '2':
        note_id = input('Введите id заметки ')
        print('Вот ваша заметка 😎')
        result = get_one_note(note_id)
        print(f"Название: {result[0][0]}, Рейтинг: {result[0][1]}")

    if res == '3':
        text_note = input('Введи текст заметки ')
        rating_note = input('Введи рейтинг заметки ')
        add_note(text_note, rating_note)
        print('Заметка добавлена 🌞')

    if res == '4':
        notes = get_most_popular_notes()
        print('Вот самые популярные заметки ➡️')
        for note in notes:
            print(*note)

    # if res == '5':
    #     delete_all_notes()
    #     print('Вы всё удалили 😢')

    if res == 'q':
        break