from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = ${{ secrets.BOTAPIKEY }}
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to $HitCoin! Start mining now!")

@dp.message_handler(commands=['tasks'])
async def show_tasks(message: types.Message):
    tasks = ["1. Complete your profile", "2. Invite a friend"]
    await message.reply("\n".join(tasks))

@dp.message_handler(commands=['complete'])
async def complete_task(message: types.Message):
    user_id = message.from_user.id
    task_id = 1  # Example task ID
    # Interact with the smart contract here to confirm task completion
    await message.reply("Task completed! You've earned 1 $HitCoin!")

@dp.message_handler(commands=['mine'])
async def mine_coin(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("💩 Mine $HitCoin", callback_data="mine")
    keyboard.add(button)
    await message.reply("Ready to mine?", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
