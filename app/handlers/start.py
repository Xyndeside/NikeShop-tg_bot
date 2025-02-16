from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from ..keyboards import main_kb
from app.database import requests

router = Router()


@router.message(CommandStart)
async def cmd_start(message: Message):
    await requests.set_user(message.from_user.id)
    await message.answer('Welcome to the nike store', reply_markup=main_kb)


@router.callback_query(F.data == 'to_main')
async def to_main(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer('Welcome to the nike store', reply_markup=main_kb)
