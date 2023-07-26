import asyncio

from aiogram import Bot, Dispatcher

import config
from handlers import cmd_start, cmd_menu, cmd_settings


async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_routers(cmd_start.router,
                       cmd_menu.router,
                       cmd_settings.router, )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
