from multiprocessing import Process

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv
import os
import asyncio
import logging
from handlers.start_hand import router as start_handler
from fastapi import FastAPI
from database import init, destroy, init_not_manager
from utilites.my_exp import queue
import logging
import asyncio
from datetime import datetime, timedelta
from typing import Dict, Any, List

import uvicorn
from fastapi import FastAPI, Form, Depends, HTTPException, status
import sys
from icecream import ic
from models.users import User
from shemas.user import UserOut
from handlers.fast_api_handler import router as rout_users


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'default',
            'level': 'INFO'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'default',
            'level': 'DEBUG'
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG'
    }
}


load_dotenv()
bot_token = os.getenv('TOKEN')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


async def start_bot():
    async with init():
        bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        queue.start_worker(num_workers=2)
        logging.basicConfig(level=logging.INFO)
        dp.include_router(start_handler)

        # await bot.send_message(453994951, 'Бот запущен', reply_markup=types.ReplyKeyboardRemove())
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        await asyncio.sleep(5)
        await queue.stop_workers()


async def main():
    await asyncio.create_task(start_bot())


if __name__ == '__main__':
    asyncio.run(main())