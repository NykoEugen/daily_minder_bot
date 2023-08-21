import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

import config
from func.reminders_today_list import schedule_alert
from keyboards.inline_keyboard import inline_keyboard


def execute():
    while True:
        def cron_routine():
            print('cron works')
            data = schedule_alert()
            if data:
                return data

        async def main():
            bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

            while True:
                data = cron_routine()

                if data is not None:
                    for item in data:
                        kb = inline_keyboard(reminder='Reminders', notes='Notes', settings='Settings')
                        await bot.send_message(text=item['description'], chat_id=item['user_id'], reply_markup=kb)
                await asyncio.sleep(60)

        asyncio.run(main())
