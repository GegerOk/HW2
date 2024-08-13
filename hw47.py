from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'zzz'
bot = Bot(token= api)
Ds = Dispatcher(bot, storage= MemoryStorage())

@Ds.message_handler(commands= ['start'])
async def start_message (message):
    await message.answer ('Привет! Я бот помогающий твоему здоровью.')

@Ds.message_handler()
async def first_message(message):
    await message.answer ('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dispatcher= Ds, skip_updates= True)

