import json
import os
import subprocess
from typing import Dict, Any

import pytz
import requests
from aiogram import Bot, Dispatcher, types, F
import asyncio
import aiofiles
import io
import logging
import datetime
import time
from asgiref.sync import sync_to_async, async_to_sync
from icecream import ic
from numpy import number
# from models import get_users, init, get_user, create_user, create_conteiner, get_first_conteiner, ImagesConteiner, get_conteiner, StatusConteiner
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message, ContentType, \
    InputMediaPhoto, InputFile, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.fsm.context import FSMContext
# from app.keyboards import main_kb, inspection_kb, completion, data_conteiner, start_kb
# from utilites.utilits_bot import coincidence
from aiogram import Router
from passlib.hash import bcrypt
from yt_dlp import YoutubeDL

from forms.form import UrlUser
from keyboards.inlines import start_menu, social_web, cancel_one, video_and_audio
# import http_rest
# from app.keyboards import users, tech_actions, the_start, auth_inline, user_list_kb, for_start
# from form.forms import Auth
# # from form.forms import Form, Stat
from models.users import User
from tester import load_main, download_tiktok_video, download_tiktok_start

router = Router()
tags = ['2160p', '1440p', '1080', '720', '480', '360', '240', '144']


async def dellete_msg(dict_: Dict[Any, Any]):
    await asyncio.sleep(20)
    await dict_.delete()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext, msg: str = None):
    photo = types.FSInputFile('static/images_for_telega.jpg')
    if msg:
        msgs = msg
    else:
        msgs = f'Привет, {message.from_user.full_name}!'
        bot_message = await message.answer_photo(photo)
    await User.get_or_create(username=message.chat.full_name, id_telegram=message.chat.id)
    await state.set_data({f'{message.chat.id}+1': {'bot_message_id': bot_message.message_id}})
    dict_ = await state.get_data()
    await message.answer(msgs, reply_markup=start_menu, parse_mode="HTML")


async def starting_load(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UrlUser.one)
    await callback.message.edit_text(f'Выберете категорию и отправьте ссылку', reply_markup=social_web)


async def social(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UrlUser.url_user)
    msg_id = await callback.message.edit_text(f'Отправьте ссылку', reply_markup=cancel_one)
    asyncio.create_task(dellete_msg(msg_id))


@router.callback_query()
async def commands(callback: types.CallbackQuery, state: FSMContext):
    dict_ = await state.get_data()
    ic(dict_)
    bot_message_id = dict_[f'{callback.message.chat.id}+1']['bot_message_id']
    try:
        await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=bot_message_id)
    except:
        pass
    lst_social = ['youtube', 'tik-tok', 'instagram']
    actions = {
        'start': lambda: starting_load(callback, state),
        'social': lambda: social(callback, state),
        'cancel_one': lambda: start(callback.message, state),
        'hd': lambda: video_filter(callback, state),
        'full_hd': lambda: video_filter(callback, state),
        'audio': lambda: video_filter(callback, state),
    }
    if callback.data in actions:
        if callback.data == 'cancel_one':
            await state.clear()
        await actions[callback.data]()
    elif callback.data in lst_social:
        await actions['social']()
    elif callback.data in tags:
        await video_filter(callback, state)



async def is_file_downloaded(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) > 0


@router.message(UrlUser.url_user)
async def filter_social(message: types.Message, state: FSMContext):

    if 'youtube' in message.text:
        await message.delete()
        urls, quality, title = await load_main(message.text)
        await state.update_data({message.from_user.id: {
            'urls': urls,
            'quality': quality,
            'title': title
        }
        })
        video_and_audio = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=i, callback_data=i)
                ] for i in quality
            ]
        )
        msg = await message.answer('Выберите качество видео', reply_markup=video_and_audio)
        asyncio.create_task(dellete_msg(msg))
    elif 'tiktok' in message.text:
        await message.delete()
        file_path = await download_tiktok_start(message.text)
        video_file = FSInputFile(file_path)
        await message.answer_video(video_file)
        os.remove(file_path)
        msg = f'Ссылка на видео: {file_path}'
        await start(message, state, msg=msg)
    elif 'instagram' in message.text:
        pass


async def dellete_file(file_path):
    await asyncio.sleep(60)
    if os.path.exists(file_path):
        os.remove(file_path)


@router.callback_query()
async def video_filter(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UrlUser.load_video)
    dict_ = await state.get_data()
    urls = dict_[callback.from_user.id]['urls']
    quality = dict_[callback.from_user.id]['quality']
    title = dict_[callback.from_user.id]['title']
    message = f'<b>Ссылка на видео: {title}</b>'
    if callback.data in quality:
        for i in urls:
            if callback.data == 'audio':
                if i['audio']:
                    message += f'\n<em>{i["url"]}</em>'
                    break
            elif callback.data == i['quality']:
                message += f'\n<em>{i["url"]}</em>'
                break
        await state.clear()
        await start(callback.message, state, message)
