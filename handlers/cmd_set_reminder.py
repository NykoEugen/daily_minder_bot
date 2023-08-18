import time
from datetime import datetime
from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from handlers.handlers import handler_menu
from keyboards.inline_keyboard import inline_keyboard


router = Router()


@router.callback_query(Text('set_reminder'))
async def handle_set_reminder(callback: CallbackQuery):
    kb = inline_keyboard(Set_date='Set date, time and description')
    await callback.message.answer('There you can add remind for yourself, and we will remain in time.\n'
                                  'Please enter date, time and description for the reminder.',
                                  reply_markup=kb)


@router.callback_query(Text('set_date', ignore_case=True))
async def handle_set_date(callback: CallbackQuery):
    await callback.message.answer("Please enter the date and time (format: yyyy-mm-dd, hh.mm) \n"
                                  "And in newline a description")


@router.message()
async def input_date_and_time(message: Message):
    in_text = message.text
    date_format = '%Y-%m-%d, %H.%M'
    newline_pos = in_text.find('\n')
    date_text = in_text[:newline_pos]
    description = in_text[newline_pos+1:]
    date_time_obj = datetime.strptime(date_text, date_format)
    await message.answer(f'Date: {date_time_obj}')
    await message.answer(f'Description: {description}')
    time.sleep(1)
    await handler_menu(message)

