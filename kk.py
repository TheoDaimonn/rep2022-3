import telebot
from telebot import types
import random
import json
bot = telebot.TeleBot('6039776212:AAGsO2nXYGlibW46ja0kIGlHJk14-4J-bQU')
@bot.message_handler(content_types=['text'])
def massage(msg):
    with open('database.json', 'r+') as database:
        database = json.load(database)
        print(database)
    u_id = str(msg.from_user.id)
    print(u_id)
    database.setdefault(u_id,0)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    markup.add(btn1)
    markup.add(btn2)
    if msg.text == '/start':
        bot.send_message(msg.from_user.id, "aaaaa", reply_markup=markup)
    elif msg.text == '1':
        bot.send_photo(msg.chat.id, photo= open(random.choice(['image1.png']), 'rb'), reply_markup=markup)

    elif msg.text == '2':
        bot.send_message(msg.chat.id, str(msg.chat.id))

    database[u_id] += 1
    bot.send_message(msg.chat.id, str(database[u_id]))
    with open('database.json', 'w') as f:
        json.dump(database, f)


def main(msg):
    bot.register_next_step_handler(msg, main)

bot.infinity_polling()