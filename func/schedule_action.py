import asyncio
import time
from datetime import datetime

import schedule
from aiogram import Router, Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message

import config
from func.schedule_reminder import RemindersCheck
from handlers.db_handler import get_reminders_to_show
from keyboards.inline_keyboard import inline_keyboard


def execute():
    while True:
        def cron_routine():
            print('cron works')
            now = datetime.now().replace(second=0, microsecond=0)
            datetime_str = now.strftime("%Y-%m-%d %H:%M")
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            reminders = get_reminders_to_show(datetime_obj)
            scheduler = RemindersCheck(reminders)
            scheduler.schedule_alert()
            if data := scheduler.schedule_now_lst:
                return data

        async def main():
            bot = Bot(token=config.token, parse_mode=ParseMode.HTML)

            while True:
                data = cron_routine()

                if data is not None:
                    for item in data:
                        kb = inline_keyboard(reminder='Reminders', notes='Notes', settings='Settings')
                        await bot.send_message(text=item['description'], chat_id=item['user_id'], reply_markup=kb)
                await asyncio.sleep(60)

        asyncio.run(main())
