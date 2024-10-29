import telebot
from telebot import types
from gpt_cls import YandexGPT


token = ''
bot = telebot.TeleBot(token)

user_state = ''
text_to_translate = ''

y_token = ''
y_catalog = ''

yandex_bot = YandexGPT(y_token, y_catalog)


@bot.message_handler(commands=['start'])
def start(message):
    global user_state

    user_state = 'start'
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\nЯ бот-переводчик. Введи текст для перевода")
    bot.register_next_step_handler(message, translation)


def translation(message):
    global text_to_translate
    text_to_translate = message.text.strip()

    markup = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton('испанский', callback_data='es')
    btn2 = types.InlineKeyboardButton('итальянский', callback_data='it')
    btn3 = types.InlineKeyboardButton('английский', callback_data='en')
    btn4 = types.InlineKeyboardButton('немецкий', callback_data='de')
    btn5 = types.InlineKeyboardButton('французский', callback_data='fr')
    btn6 = types.InlineKeyboardButton('китайский', callback_data='zh')
    btn7 = types.InlineKeyboardButton('японский', callback_data='ja')
    btn8 = types.InlineKeyboardButton('эсперанто', callback_data='eo')
    btn9 = types.InlineKeyboardButton('шведский', callback_data='sv')
    btn10 = types.InlineKeyboardButton('Выход', callback_data='exit')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)

    bot.send_message(message.chat.id, 'Выбери язык для перевода\nДля выхода нажми кнопку "Выход"', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global user_state

    if call.data != 'exit' and user_state != '':
        languade = call.data
        response = yandex_bot.send_request(text_to_translate, languade)
        bot.send_message(call.message.chat.id, f"Перевод: {response}.\nМожешь заново написать текст для перевода")
        bot.register_next_step_handler(call.message, translation)
    else:
        user_state = ''
        bot.send_message(call.message.chat.id, 'Пока-пока, заходи еще 🙌')


bot.infinity_polling()