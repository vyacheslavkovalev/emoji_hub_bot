import json
from mailbox import Message
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.utils.chat_action import ChatActionSender
from keyboards.common_keyboards import ButtonText

from keyboards.inline_keyboards.inline_keyboards import build_category_kb, build_group_kb


router = Router(name=__name__)


@router.message(F.text==ButtonText.DAVAI)
@router.message(Command('category'))
async def category_handler(message: Message) -> None:
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        await message.answer(
            text=f'Выберите интересующую категорию:',
            reply_markup=build_category_kb()
        )


@router.message(Command('group'))
async def category_handler(message: Message) -> None:
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        await message.answer(
            text=f'Выберите интересующую группу:',
            reply_markup=build_group_kb()
        )
