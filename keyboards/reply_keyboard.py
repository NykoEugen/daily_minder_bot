from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_keyboard(*args) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in args:
        kb.button(text=i)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
