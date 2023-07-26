from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(Text('menu', ignore_case=True))
async def answer_menu(callback: CallbackQuery):
    await callback.message.answer('In menu')
    await callback.answer()
