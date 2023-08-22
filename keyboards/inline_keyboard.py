from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config


def inline_keyboard(button_in_line=2, **kwargs) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for k, v in kwargs.items():
        kb.button(text=v, callback_data=k)
    kb.adjust(button_in_line)
    return kb.as_markup(resize_keyboard=True)


def main_menu_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(text='Reminder', callback_data='reminder'))
    kb.add(types.InlineKeyboardButton(text='About', url=config.WEB_SITE))
    reply_markup = kb.as_markup()
    return reply_markup
