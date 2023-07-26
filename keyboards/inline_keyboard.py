from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline_keyboard(button_in_line=2, **kwargs) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for k, v in kwargs.items():
        kb.button(text=v, callback_data=k)
    kb.adjust(button_in_line)
    return kb.as_markup(resize_keyboard=True)
