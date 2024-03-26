import json
from pathlib import Path
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


path_project = str(Path('__file__').absolute().parent)
path_data = f'{path_project}/Data'


with open(f'{path_data}/category_group.json', 'r', encoding='UTF-8') as json_file:
    category_group=json.load(json_file)

category_cb_data = list(category_group.keys())
group_cb_data = [group for sublist in [category["groups"].keys() for category in category_group.values() if isinstance(category, dict) and 'groups' in category] for group in sublist]
for category in category_group.keys():
    if not isinstance(category_group[category], dict):
        group_cb_data.append(category)

def build_category_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for category in category_group.keys():
        if isinstance(category_group[category], dict):
            text = category_group[category]['name']
        else:
            text = category_group[category]
        builder.button(
            text=text,
            callback_data=category
        )
        builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def build_group_kb(category: str = None) -> InlineKeyboardMarkup:
    if category:
        builder = InlineKeyboardBuilder()
        for group in category_group[category]['groups']:
            text = category_group[category]['groups'][group]
            builder.button(
                text=text,
                callback_data=group
            )
        builder.adjust(2)
    else:
        builder = InlineKeyboardBuilder()
        for category in category_group.keys():
            if isinstance(category_group[category], dict):
                for group in category_group[category]['groups']:
                    text = category_group[category]['groups'][group]
                    builder.button(
                        text=text,
                        callback_data=group
                    )
            else:
                text = category_group[category]
                builder.button(
                    text=text,
                    callback_data=category
                )
        builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
