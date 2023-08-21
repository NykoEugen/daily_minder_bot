import asyncio
import logging
import threading

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from func import schedule_action
from func.schedule_action import execute

from handlers import handlers_menu, set_reminder_handlers, db_handler, show_reminders_handler


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(handlers_menu.router, set_reminder_handlers.router,
                       db_handler.router, show_reminders_handler.router, schedule_action.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    thread = threading.Thread(target=execute)
    thread.start()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


