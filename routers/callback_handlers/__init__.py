__all__ = ('router')

from aiogram import Router
from .kb_callback_handlers import router as kb_callback_router

router = Router(name=__name__)

router.include_routers(
    kb_callback_router
)
