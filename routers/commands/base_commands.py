from aiogram import Router

from pathlib import Path
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.markdown import hbold

from keyboards.common_keyboards import get_on_start_kb


router = Router(name=__name__)

path_project = str(Path('__file__').absolute().parent)
path_data = f'{path_project}/Data'

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        photo = FSInputFile(f'{path_data}/photos/emoji.jpg')
        caption = f'Привет, {hbold(message.from_user.first_name)}! Я помогу найти подходящие emoji. Давай попробуем?'
        await message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=get_on_start_kb()
        )


@router.message(Command('help'))
async def help_handler(message: Message) -> None:
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        await message.answer(
            text=f'Чтобы получить нужные emoji можно выбрать интуресующую категорию при помощи команды /category. Если в категории есть подгруппа, будет предложено выбрать группу, если нет - предложу соответсвующие emoji. Также можно выбрать сразу интересующую группу командой /group. Давай попробуем?',
            reply_markup=get_on_start_kb())
