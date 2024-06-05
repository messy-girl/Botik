import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token="7178580468:AAElDlSZ_JImKOGBal8zHYjR-4ff5tIrkA4")
dp = Dispatcher()

# Список зарегистрированных участников
participants = []

# Команда /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать на регистрацию на марафон! 👋\n"
                         "Чтобы зарегистрироваться, введите свои ФИО и тип забега (например, 'Иванов Иван Иванович, полумарафон').")

# Обработчик для записи участников
@dp.message()
async def handle_registration(message: types.Message):
    try:
        full_name, race_type = message.text.split(",")
        full_name = full_name.strip()
        race_type = race_type.strip()

        participants.append({"ФИО": full_name, "Забег": race_type})
        await message.answer(f"Запись на марафон успешно оформлена! 🎉\n"
                             f"Ваши данные:\n"
                             f"ФИО: {full_name}\n"
                             f"Забег: {race_type}")
    except ValueError:
        await message.answer("Неверный формат ввода данных. Пожалуйста, введите свои ФИО и тип забега через запятую (например, 'Иванов Иван Иванович, полумарафон').")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())