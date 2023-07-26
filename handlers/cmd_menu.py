from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from keyboards.inline_keyboard import inline_keyboard

router = Router()


@router.callback_query(Text('menu', ignore_case=True))
async def answer_menu(callback: CallbackQuery):
    kb = inline_keyboard(Set_date='Set date', Set_time='Set time')
    await callback.message.answer('Menu', reply_markup=kb)
    await callback.answer()
