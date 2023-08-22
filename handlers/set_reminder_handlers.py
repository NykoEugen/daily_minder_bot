from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

from func.DayTimeCheck import time_check, date_check, valid_datetime
from handlers.db_handler import create_reminder, insert_reminder
from keyboards.inline_keyboard import inline_keyboard, main_menu_buttons

router = Router()


class MyState(StatesGroup):
    set_description = State()
    set_day = State()
    set_time = State()
    date_time = State()
    reminder_id = State()
    remove = State()


@router.callback_query(Text('set_remind'))
async def handle_set_remind(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('You will be asked to enter a description, '
                                  'day and time when the reminder should be made')
    await state.set_state(MyState.set_description)
    await callback.message.answer('Add description')


@router.message(MyState.set_description)
async def set_description(message: Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await state.set_state(MyState.set_day)
    await message.answer('Great, now enter a date (format: dd.mm.yy)')


@router.message(MyState.set_day)
async def set_day(message: Message, state: FSMContext):
    in_day = message.text
    valid_date = date_check(in_day)
    if valid_date is not None:
        await state.update_data(day=valid_date)
        await state.set_state(MyState.set_time)
        await message.answer('Good, now add a time (format: hh.mm)')
    else:
        await message.reply('Incorrect data format, please try again')


@router.message(MyState.set_time)
async def set_time(message: Message, state: FSMContext):
    in_time = message.text
    valid_time = time_check(in_time)
    if valid_time is not None:
        data = await state.get_data()
        description = data['description']
        day_obj = data['day']
        datetime_obj = valid_datetime(day_obj, valid_time)
        await state.update_data(datetime_obj=datetime_obj)
        kb = inline_keyboard(confirm='Confirm')
        await message.answer(f'Confirm reminder: {description}, at date: {datetime_obj}', reply_markup=kb)
    else:
        await message.reply('Incorrect time format, try again')


@router.callback_query(Text('confirm'))
async def handle_confirm(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    description = data['description']
    datetime_obj = data['datetime_obj']

    user_id = callback.from_user.id
    create_reminder()
    insert_reminder(description=description, noty_at=datetime_obj, is_done=0, user_pk=user_id)

    kb = main_menu_buttons()

    await callback.message.answer('Good your reminder was set', reply_markup=kb)
    await callback.answer()


