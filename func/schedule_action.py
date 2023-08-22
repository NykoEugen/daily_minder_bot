import asyncio

from aiogram import Bot, Router
from aiogram.enums import ParseMode

import config
from func.reminders_today_list import schedule_alert
from keyboards.inline_keyboard import inline_keyboard

router = Router()


def execute():
    while True:
        def cron_routine():
            print('cron works')
            data = schedule_alert()
            if data:
                return data
            else:
                print("event doesn't exist")

        async def main():
            bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
            while True:
                data = cron_routine()

                if data is not None:
                    for item in data:
                        str_text = (f"Reminder id: {item['id']}. \n"
                                    f"Description: {item['description']}.")
                        kb = inline_keyboard(confirm_event="Confirm event")
                        await bot.send_message(text=str_text, chat_id=item['user_id'], reply_markup=kb)
                        await bot.session.close()
                await asyncio.sleep(60)

        asyncio.run(main())
