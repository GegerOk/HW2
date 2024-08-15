from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = '7334022973:AAHsG1he-igZclt9ZCFDK0nsF-zeZnQ1MZc'
bot = Bot(token= api)
Ds = Dispatcher(bot, storage= MemoryStorage())

class UserState (StatesGroup):
    age = State()
    growth = State()
    weight = State()

@Ds.message_handler(text = ('Calories'))
async def set_age(message):
    await message.answer ('Введите свой возраст')
    await UserState.age.set()

@Ds.message_handler(state= UserState.age)
async def set_growth(message, state):
    print(f"Updating data with age: {message.text}")
    await state.update_data (f = message.text)
    await message.answer ('Введите свой рост')
    await UserState.growth.set()

@Ds.message_handler(state=UserState.growth)
async def set_weight(message, state):
    print(f"Updating data with height: {message.text}")
    await state.update_data (s = message.text)
    await message.answer ('Введите свой вес')
    await UserState.weight.set()

@Ds.message_handler(state=UserState.weight)
async def send_calories(message, state):
    print(f"Updating data with weight: {message.text}")
    await state.update_data (t = message.text)
    data = await state.get_data()
    final_calc = (10  *  int(data ['t']) + 6.25  *  int(data ['s']) - 5  *  int(data ['f']) +5)
    await message.answer (f'Ваша норма: {final_calc}')
    await state.finish()


@Ds.message_handler(commands= ['start'])
async def start_message (message):
    await message.answer ('Привет! Я бот помогающий твоему здоровью.')

@Ds.message_handler()
async def first_message(message):
    await message.answer ('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dispatcher= Ds, skip_updates= True)

