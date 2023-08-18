import asyncio
from datetime import datetime

from aiogram import Bot

import config
from handlers.db_handler import get_reminders_to_show


async def check_remind():
    while True:
        current_datetime = datetime.now()
        reminders_to_show = get_reminders_to_show(current_datetime)
        print(current_datetime)
        print(reminders_to_show)
        for remind in reminders_to_show:
            remind_text = remind[1]
            user_id = remind[3]
            await send_reminder(remind_text, user_id)
        await asyncio.sleep(60)


async def send_reminder(text, user_id):
    bot = Bot(token=config.token)
    await bot.send_message(chat_id=user_id, text=text)

asyncio.run(check_remind())
# check_remind()