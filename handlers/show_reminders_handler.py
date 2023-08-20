from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from func.reminders_today_list import reminder_list
from keyboards.inline_keyboard import inline_keyboard

router = Router()


@router.callback_query(Text('reminder_list'))
async def show_reminder_list(callback: CallbackQuery):
    kb = inline_keyboard(reminder='Reminders', notes='Notes', settings='Settings')
    event_str = ""
    lst = reminder_list()

    if lst is None:
        await callback.message.answer("Sorry you don't have events")
    elif lst:
        for item in lst:
            description = item['description']
            event_time = item['time']
            str_look = f"Description: {description}, time: {event_time} \n"
            event_str += str_look
        await callback.message.answer(event_str, reply_markup=kb)
