from aiogram import Router, F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

start_router = Router()

@start_router.message(Commadstart())
async def cmd_start(messange: Message):
    await messange