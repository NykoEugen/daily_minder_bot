import time

from telebot import types

import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def handel_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('/Configuration')
    button2 = types.KeyboardButton('/About')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, "Hi, I'm Daily Minder and I help you simplify your daily routine", reply_markup=keyboard)


@bot.message_handler(commands=["Configuration"])
def handle_configuration(message):
    bot.send_message(message.chat.id, "Config your personal templates")


@bot.message_handler(commands=["About"])
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
