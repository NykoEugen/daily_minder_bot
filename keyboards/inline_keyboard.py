from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_keyboard(**kwargs) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for k, v in kwargs.items():
        kb.button(text=k, callback_data=v)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
