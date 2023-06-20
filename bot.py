import re
import sqlite3
import time

from telebot import types

import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.add(types.KeyboardButton('Send phone number', request_contact=True))
    keyboard.add(types.KeyboardButton('Denied', request_contact=None))
    bot.send_message(message.chat.id, "Hi, I'm Daily Minder and I help you simplify your daily routine."
                                      "We need your phone number for authorization.", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_contact_validation)

# @bot.message_handler(content_types=['text'])
# def handle_denied(message):
#     if message.text == 'Denied':
#         bot.send_message(message.chat.id, "We can't get the full functionality because we haven't logged in")


@bot.message_handler(content_types=['contact'])
def handle_contact_validation(message):
    if message.contact is not None:
        contact = message.contact
        phone_number = contact.phone_number
        user_phone = phone_number[-9:]
        insert_phone_to_db(user_phone)
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton("Menu"))
        bot.send_message(message.chat.id, "Great, thanks for a number!", reply_markup=keyboard)
        bot.register_next_step_handler(message, handle_menu)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton('Send phone number', request_contact=True))
        bot.send_message(message.chat.id, "We can't get the full functionality because we haven't logged in",
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, handle_menu)


def validate_phone_number(phone_number):
    pattern = r'^(?:\+380|380|0)\d{9}$'
    if re.match(pattern, phone_number):
        return True
    return False


def insert_phone_to_db(data):
    conn = sqlite3.connect('users.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_number) VALUES (?)", (data,))
    conn.commit()
    conn.close()


@bot.message_handler(commands=["menu"])
def handle_menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Configuration')
    button2 = types.KeyboardButton('About')
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Hi, I'm Daily Minder and I help you simplify your daily routine",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Configuration')
def handle_configuration(message):
    bot.send_message(message.chat.id, "Config your personal templates")


@bot.message_handler(func=lambda message: message.text == 'About')
def handle_about(message):
    bot.send_message(message.chat.id, "What can I do? Answer is simple many tiny things: note, notification, "
                                      "daily time-advice")

    time.sleep(1)

    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton("Web-site", callback_data="button_pressed",
                                                 url=config.web_site)
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Or you can visit our web site", reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
