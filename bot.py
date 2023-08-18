import asyncio
import logging
import threading

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from func import schedule_action
from func.schedule_action import execute

from handlers import handlers, reminder_handlers, db_handler


async def main():
    bot = Bot(token=config.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(handlers.router, reminder_handlers.router,
                       db_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    thread = threading.Thread(target=execute)
    thread.start()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


