from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from func.regex_id_reminder import regex_id_reminder
from func.reminders_today_list import reminder_list
from handlers.db_handler import edit_reminder_stat
from keyboards.inline_keyboard import inline_keyboard

router = Router()


@router.callback_query(Text('reminder_list'))
async def show_reminder_list(callback: CallbackQuery):
    kb = inline_keyboard(reminder='Reminders', notes='Notes', settings='Settings')
    event_str = ""
    lst = reminder_list()
    if len(lst) == 0:
        event_str += "You don't have events"
    elif len(lst) >= 0:
        for item in lst:
            description = item['description']
            event_time = item['time']
            str_look = f"Description: {description}, time: {event_time} \n"
            event_str += str_look
    await callback.message.answer(event_str, reply_markup=kb)


@router.callback_query(Text('confirm_event'))
async def confirmed_alert(callback: CallbackQuery):
    data_alert = callback.message.text
    reminder_id = regex_id_reminder(data_alert)
    edit_reminder_stat(reminder_id)
    kb = inline_keyboard(reminder='Reminders', notes='Notes', settings='Settings')
    await callback.message.answer("Reminder is done", reply_markup=kb)
