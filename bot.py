import os, asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.database import async_main
from register_handlers import register_all_handlers

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()


register_all_handlers(dp)


async def main():
    await async_main()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
