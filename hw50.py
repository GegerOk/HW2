from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = 'BBB'
bot = Bot(token= api)
Ds = Dispatcher(bot, storage= MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
kb.add(button_1)
kb.add(button_2)

ib = InlineKeyboardMarkup()
ibutton_1 = InlineKeyboardButton(text= 'Расчитать норму каллорий', callback_data='calories')
ibutton_2 = InlineKeyboardButton(text= 'Формулы расчёта', callback_data= 'formulas')
ib.add (ibutton_1)
ib.add (ibutton_2)

class UserState (StatesGroup):
    age = State()
    growth = State()
    weight = State()

@Ds.message_handler(commands='start')
async def main_menu(message):
    await message.answer (text = 'Выберите опцию', reply_markup = ib)

@Ds.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer (text = 'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;')
    await call.message()

@Ds.callback_query_handler(text = ('calories'))
async def set_age(call):
    await call.message.answer (text = 'Введите свой возраст')
    call.answer()
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


#@Ds.message_handler(commands= ['start'])
#async def start_message (message):
#    await message.answer ('Привет! Я бот помогающий твоему здоровью.')

@Ds.message_handler()
async def first_message(message):
    await message.answer (text = 'Представляю клавиатуру', reply_markup = kb)

if __name__ == '__main__':
    executor.start_polling(dispatcher= Ds, skip_updates= True)

