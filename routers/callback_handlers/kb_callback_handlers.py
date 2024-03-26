import json
from pathlib import Path
from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.chat_action import ChatActionSender
import requests

from keyboards.inline_keyboards.inline_keyboards import (
    category_cb_data,
    build_group_kb,
    group_cb_data
)

router = Router(name=__name__)


path_project = str(Path('__file__').absolute().parent)
path_data = f'{path_project}/Data'

with open(f'{path_data}/category_group.json', 'r', encoding='UTF-8') as json_file:
    category_group=json.load(json_file)


@router.callback_query(F.data.in_(category_cb_data))
async def category_kb_callback(callback_query: CallbackQuery):
    if isinstance(category_group[callback_query.data], dict):
        await callback_query.message.edit_text(
            text=f'Выберите интересующую группу:',
            reply_markup=build_group_kb(callback_query.data)
        )
    else:
        empji_dict = requests.get(f'https://emojihub.yurace.pro/api/all/category/{callback_query.data}').json()
        text = ''.join(emoji['htmlCode'][0] for emoji in empji_dict)
        await callback_query.message.edit_text(
            text=text
        )


@router.callback_query(F.data.in_(group_cb_data))
async def group_kb_callback(callback_query: CallbackQuery):
    empji_dict = requests.get(f'https://emojihub.yurace.pro/api/all/group/{callback_query.data}').json()
    text = ''.join(emoji['htmlCode'][0] for emoji in empji_dict)
    await callback_query.message.edit_text(
        text=text
    )
