from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db_handler import connection, insert_user
from keyboards.inline_keyboard import inline_keyboard

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer("Hello in Daily Minder Bot",
                         reply_markup=inline_keyboard(Menu='menu', Settings='settings'))
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    connection()
    insert_user(user_id, username, first_name, last_name)
