import sqlite3

import telebot
from telebot import types
import json


class TaskModel:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self._load_from_file()

    def get_tasks(self):
        return self.tasks

    def add_task(self, task):
        """Добавили метод"""
        self.tasks.append(task)
        self._save_to_file()

    def _load_from_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        return tasks

    def _save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f)



class TaskModelSQL:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_tasks(self, user_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory

        cursor = connection.cursor()
        rows = cursor.execute('select * from task where user_id = ?', (user_id, )).fetchall()
        connection.close()

        return rows

    def add_task(self, text, user_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory

        cursor = connection.cursor()
        cursor.execute('insert into task (name, user_id) values (?, ?)', (text, user_id))
        connection.commit()
        connection.close()

    def get_user(self, telegram_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory

        cursor = connection.cursor()
        rows = cursor.execute('select * from user where telegram_id = ?', (telegram_id, )).fetchone()
        connection.close()
        return rows


    def add_user(self, name, telegram_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory

        cursor = connection.cursor()
        cursor.execute('insert into user (name, telegram_id) values (?, ?)', (name, telegram_id))
        connection.commit()
        connection.close()

    def delete_task(self, task_id, user_id):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = self._dict_factory

        cursor = connection.cursor()
        cursor.execute('DELETE FROM task WHERE id = ? and user_id = ?', (task_id, user_id))
        connection.commit()
        connection.close()

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        # cursor = self.connection.cursor()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


token = ''
bot = telebot.TeleBot(token)

user_state = ''
ADD_STATE = 'add'
DEL_DATE = 'del'

db_name = ''
db = TaskModelSQL(db_name)


@bot.message_handler(commands=["start"])
def start(message):
    description = 'Я бот для создания списка дел. Жми кнопку или команду /add для добавления'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('добавить задачу')
    button2 = types.KeyboardButton('посмотреть задачи')
    markup.add(button)
    markup.add(button2)

    telegram_id = message.chat.id
    name = message.from_user.first_name
    user = db.get_user(telegram_id)

    if not user:
        db.add_user(name, telegram_id)
        bot.reply_to(message, 'я вас добавил ')

    bot.send_message(message.chat.id, description, reply_markup=markup)


@bot.message_handler(regexp='добавить задачу')
@bot.message_handler(commands=["add"])
def add(message):
    global user_state
    user_state = ADD_STATE
    bot.reply_to(message, 'Введи текст задачи: ')


@bot.message_handler(regexp='посмотреть задачи')
@bot.message_handler(commands=["tasks"])
def get_task_list(message):
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if not user:
        return bot.reply_to(message, 'вас нет в базе ')

    tasks = db.get_tasks(user['id'])

    if not tasks:
        return bot.reply_to(message, 'у вас нет задач ')

    tasks = [f"{task['name']} (id: {task['id']})" for task in tasks]
    tasks_string = '\n'.join(tasks)

    bot.reply_to(message, f"Вот ваши задачи:\n{tasks_string}")

@bot.message_handler(commands=["del"])
def delete(message):
    global user_state
    user_state = DEL_DATE
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    tasks = db.get_tasks(user['id'])

    tasks = [f"{task['name']} (id: {task['id']})" for task in tasks]
    tasks_string = '\n'.join(tasks)

    bot.reply_to(message, f"Выбирай id задачи:\n{tasks_string}")

@bot.message_handler(commands=["end"])
def end_state(message):
    global user_state
    user_state = ''
    bot.reply_to(message, "Мы вышли из сеанса добавления задачи")


@bot.message_handler(commands=["keyboard"])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('добавить задачу')
    markup.add(button)

    bot.send_message(message.chat.id, 'Какой-то текст', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def get_task(message):
    global user_state
    telegram_id = message.chat.id
    user = db.get_user(telegram_id)
    if user_state == ADD_STATE:
        db.add_task(message.text, user['id'] )
        user_state = ''
        bot.reply_to(message, 'Добавил в базу')

    if user_state == DEL_DATE:
        try:
            task_num = int(message.text)
            # print(task_num)
            telegram_id = message.chat.id
            # print(telegram_id)
            user = db.get_user(telegram_id)
            # print(user)
            tasks = db.get_tasks(user['id'])
            for el in tasks:
                if el['id'] == task_num:
                    print(el)
                    db.delete_task(el['id'], el['user_id'])
            bot.reply_to(message, 'Удалил задачу')


        except Exception:
            bot.reply_to(message, 'Такой задачи нет')
            print('ошибка')
            return

bot.infinity_polling()
