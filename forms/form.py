from aiogram.fsm.state import State, StatesGroup


class UrlUser(StatesGroup):
    one = State()
    url_user = State()
    load_video = State()