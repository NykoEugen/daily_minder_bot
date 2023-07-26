from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(Text('settings', ignore_case=True))
async def answer_menu(callback: CallbackQuery):
    await callback.message.answer('In settings')
    await callback.answer()
