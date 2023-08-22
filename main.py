import logging
import threading

import uvicorn
from aiogram.fsm.storage.memory import MemoryStorage
from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot

from config import BOT_TOKEN, NGROK_TUNNEL_URL
from func import schedule_action
from func.schedule_action import execute
from handlers import handlers_menu, set_reminder_handlers, db_handler, show_reminders_handler


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format=u'%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)

storage = MemoryStorage()

WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{NGROK_TUNNEL_URL}{WEBHOOK_PATH}"

app = FastAPI()
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    logger.info("App started")
    dp.include_routers(handlers_menu.router, set_reminder_handlers.router,
                       db_handler.router, show_reminders_handler.router, schedule_action.router)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    logger.info("App stopped")


if __name__ == "__main__":
    thread = threading.Thread(target=execute)
    thread.start()
    uvicorn.run(app, host="localhost", port=8000)
