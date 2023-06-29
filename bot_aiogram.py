import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.types import Message, Contact, InputContactMessageContent
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.enums.content_type import ContentType

import config

logging.basicConfig(level=logging.INFO)
bot = Bot(config.token, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command('start'))
async def handle_start(message: types.Message):
    # builder = InlineKeyboardBuilder()
    # builder.row(types.InlineKeyboardButton(text="Access phone", callback_data="access_phone", contact_request=True),
    #             types.InlineKeyboardButton(text="Denied", callback_data="denied"), )
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Access phone", contact_request=True, resize_keyboard=True))
    await message.answer("Pleas take access for your phone number", reply_markup=builder.as_markup())


@dp.message(ContentType('contact'))
async def handle_contact(message: Message):
    print(message.contact)


@dp.callback_query(Text('access_phone'))
async def handle_button_access(callback: types.CallbackQuery):
    message = callback.message
    print(message)
    # await handle_callback_contact(message)


@dp.callback_query(Text("denied"))
async def handle_button_denied(callback: types.CallbackQuery):
    await callback.answer("Button 2 was clicked!")


async def handle_callback_contact(message: Message):
    print("Start serialize contact")
    contact = message.contact
    phone_number = contact.phone_number[-9:]
    first_name = contact.first_name
    last_name = contact.last_name
    print(contact, phone_number, first_name, last_name)
    kb = [[types.KeyboardButton(text="Menu"), ], ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Great, thanks for a number!", reply_markup=keyboard)
    await message.answer(f"First name: {first_name}\n"
                         f"Last name: {last_name}\n"
                         f"Phone number: {phone_number}")


async def handle_callback_contact_denied(message: Message):
    kb = [[types.KeyboardButton(text="Accept", request_contact=True), ], ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("We can't get the full functionality because we haven't logged in", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
