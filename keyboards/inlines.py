from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Скачивание видео\nиз соц сетей (instagram, youtube, tik-tok)", callback_data="start")
        ],
        [
            InlineKeyboardButton(text="Личный кабинет",
                                 callback_data="lk_user")
        ]
    ]
)


social_web = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="youtube", callback_data="youtube")
        ],
        [
            InlineKeyboardButton(text="tik-tok",
                                 callback_data="tik-tok")
        ],
        [
            InlineKeyboardButton(text="instagram",
                                 callback_data="instagram")
        ]
    ]
)


cancel_one = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="отмена", callback_data="cancel_one")
        ],
    ]
)

video_and_audio = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="максимальное качество видео", callback_data="full_hd")
        ],
        [
            InlineKeyboardButton(text="сруднее качество видео", callback_data="hd")
        ],
        [
            InlineKeyboardButton(text="аудио", callback_data="sound")
        ],
    ]
)