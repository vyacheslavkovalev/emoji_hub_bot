from aiogram import Router
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender


router = Router(name=__name__)


@router.message()
async def any_handler(message: Message) -> None:
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        await message.reply(f'К сожалению я не обрабатываю входящие сообщения. Для информации о работе бота воспользуйся инструкцией /help.')
