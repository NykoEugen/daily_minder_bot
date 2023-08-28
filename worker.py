import asyncio
import os


from aiogram import Bot
from aiogram.enums import ParseMode
from celery import Celery, shared_task
from celery.schedules import crontab

import config
from func.reminders_today_list import alert_lst
from keyboards.inline_keyboard import inline_keyboard


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")


celery.conf.beat_schedule = {
    "run_every_minute": {
        "task": "worker.celery_task",
        "schedule": crontab()
    },
}


async def bot_send_message(item):
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    str_text = (f"Reminder id: {item['id']}. \n"
                f"Description: {item['description']}.")
    kb = inline_keyboard(confirm_event="Confirm event")
    await bot.send_message(text=str_text, chat_id=item['user_id'], reply_markup=kb)
    await bot.session.close()


@shared_task
def celery_task():
    data = alert_lst()

    if data is not None:
        for item in data:
            asyncio.run(bot_send_message(item))
