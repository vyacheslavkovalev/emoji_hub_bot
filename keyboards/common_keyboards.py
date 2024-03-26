from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonText:
    DAVAI = 'Давай!'


def get_on_start_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=ButtonText.DAVAI)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
