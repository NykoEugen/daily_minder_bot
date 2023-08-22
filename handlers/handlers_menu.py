from aiogram import Router, types
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config
from func.schedule_action import execute
from handlers.db_handler import create_user, insert_user
from keyboards.inline_keyboard import inline_keyboard, main_menu_buttons

router = Router()


@router.message(Command('start'))
async def start_handler(message: Message):
    kb = main_menu_buttons()

    await message.answer('Hello in Minder Bot', reply_markup=kb)

    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    create_user()
    insert_user(user_id, username, first_name, last_name)


# @router.callback_query(Text('main_menu'))
# async def handle_main_menu(callback: CallbackQuery):
#     kb = inline_keyboard(reminder='Reminders', notes='Notes', settings='Settings')
#     await callback.message.answer('Main menu', reply_markup=kb)
#     await callback.answer()


@router.callback_query(Text('reminder', ignore_case=True))
async def handle_reminder(callback: CallbackQuery):
    kb = inline_keyboard(reminder_list='List of reminds', set_remind='Set remind',
                         remove_remind='Remove remind')
    await callback.message.answer('Reminder Menu', reply_markup=kb)
    await callback.answer()


# @router.callback_query(Text('notes', ignore_case=True))
# async def handle_reminder(callback: CallbackQuery):
#     kb = inline_keyboard(note_list='List of notes', add_note='Add note',
#                          remove_note='Remove note')
#     await callback.message.answer('Note Menu, in progres', reply_markup=kb)
#     await callback.answer()


# @router.callback_query(Text('setting', ignore_case=True))
# async def handle_reminder(callback: CallbackQuery):
#     kb = inline_keyboard(notification_time='Notification time')
#     await callback.message.answer('Settings Menu, in progres', reply_markup=kb)
#     await callback.answer()



