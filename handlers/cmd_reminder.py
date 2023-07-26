import re

from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery
from regex import regex

from keyboards.inline_keyboard import inline_keyboard

router = Router()


@router.callback_query(Text('set_reminder'))
async def handle_set_reminder(callback: CallbackQuery):
    kb = inline_keyboard(Set_date='Set date', Set_time='Set time')
    await callback.message.answer('Please select a date and time for the reminder.',
                                  reply_markup=kb)


@router.callback_query(Text('set_date', ignore_case=True))
async def handle_set_date(callback: CallbackQuery):
    await callback.message.answer("Please enter the date (format: yyyy-mm-dd)")


@router.message()
async def input_date(message: Message):
    in_date = message.text
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    date = re.findall(pattern, in_date)
    await message.reply(f'Date: {date}, select time', reply_markup=inline_keyboard(button_in_line=1, set_time='Set time'))


@router.callback_query(Text('set_time', ignore_case=True))
async def handle_set_date(callback: CallbackQuery):
    await callback.message.answer("Please enter the time (format: hh:mm)")


@router.message()
async def input_time(message: Message):
    in_time = message.text
    pattern = r"^\d{2}:\d{2}$"
    time = re.findall(pattern, in_time)
    print(time)
    await message.answer("Enter description of notification")


@router.message()
async def input_description(message: Message):
    description = message.text
    print(description)
    await message.answer("Notification was saved", reply_markup=inline_keyboard(menu="Menu", settings="Settings"))
