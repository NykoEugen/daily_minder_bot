from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from func.regex_id_reminder import regex_id_reminder
from func.reminders_today_list import reminder_list
from func.valid_int import valid_int
from handlers.db_handler import edit_reminder_stat, delete_reminder_from_db
from handlers.set_reminder_handlers import MyState
from keyboards.inline_keyboard import inline_keyboard, main_menu_buttons

router = Router()


@router.callback_query(Text('reminder_list'))
async def show_reminder_list(callback: CallbackQuery):
    kb = inline_keyboard(remove_reminder="Delete", back="Back")
    valid_user_pk = callback.from_user.id
    event_str = ""
    lst = reminder_list(valid_user_pk)
    if len(lst) == 0:
        event_str += "You don't have events"
    elif len(lst) >= 0:
        for item in lst:
            reminder_id = item['reminder_id']
            description = item['description']
            event_time = item['time']
            str_look = f"Event id: {reminder_id}\nDescription: {description}\nTime: {event_time} \n\n"
            event_str += str_look
    await callback.message.answer(event_str, reply_markup=kb)


@router.callback_query(Text('confirm_event'))
async def confirmed_alert(callback: CallbackQuery):
    data_alert = callback.message.text
    reminder_id = regex_id_reminder(data_alert)
    valid_user_pk = callback.from_user.id
    print(valid_user_pk)
    edit_reminder_stat(reminder_id, valid_user_pk)
    kb = main_menu_buttons()
    await callback.message.answer("Reminder is done", reply_markup=kb)


@router.callback_query(Text('remove_reminder'))
async def delete_reminder(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MyState.remove)
    await callback.message.reply("Type reminder id to remove")


@router.callback_query(Text('back'))
async def back_to_menu(callback: CallbackQuery):
    kb = main_menu_buttons()
    await callback.message.answer("Reminder menu", reply_markup=kb)


@router.message(MyState.remove)
async def remove_reminder(message: Message, state: FSMContext):
    data = message.text
    kb = main_menu_buttons()
    int_val = valid_int(data)
    valid_user_pk = message.from_user.id
    if int_val:
        delete_reminder_from_db(int_val, valid_user_pk)
        await message.answer("Reminder was deleted successful", reply_markup=kb)
    else:
        await message.reply("Incorrect value, pleas check")

    await state.clear()

