import logging
import asyncio
import config
from aiogram import Bot, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(config.TOKEN)  # Bot instance
router = Router()


async def main() -> None:
    slave = Dispatcher()
    slave.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await slave.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    