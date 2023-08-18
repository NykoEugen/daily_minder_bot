from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_keyboard(kb_in_line=2, *args) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in args:
        kb.button(text=i)
    kb.adjust(kb_in_line)
    return kb.as_markup(resize_keyboard=True)
