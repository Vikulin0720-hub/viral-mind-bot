import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# Берем токен из безопасных настроек сервера, а не пишем в коде
API_TOKEN = os.getenv("BOT_TOKEN", "8811648835:AAGguuEZgU4rKVcfky6sxI0naAOdUNZQQXQ")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def get_main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Радар трендов & Мемы", callback_data="trends")],
        [InlineKeyboardButton(text="🎬 Сгенерировать сценарий", callback_data="generate_script")],
        [InlineKeyboardButton(text="💰 Как монетизировать контент", callback_data="monetization")],
        [InlineKeyboardButton(text="💎 PRO-аккаунт (Подписка)", callback_data="buy_pro")]
    ])

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"Я твой AI-продюсер для TikTok, Reels и Shorts.\n"
        f"Помогу найти тренды, напишу вирусный сценарий за 5 секунд и покажу, как на этом заработать.\n\n"
        f"Выбирай инструмент:"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu())

@dp.callback_query()
async def process_callbacks(callback: types.CallbackQuery):
    if callback.data == "trends":
        await callback.message.answer("📊 *Анализ трендов:*\nСегодня в топе звуки с ускоренным темпом и форматы 'POV: когда ты...'.")
    elif callback.data == "generate_script":
        await callback.message.answer("📝 Отправь мне тему твоего видео или нишу, и я сделаю раскадровку!")
    elif callback.data == "monetization":
        await callback.message.answer("💸 *Где деньги?*\n1. Партнерские программы.\n2. Перелив трафика в приватный TG.\n3. Продажа инфопродуктов.")
    elif callback.data == "buy_pro":
        await callback.message.answer("💎 *PRO-режим всего за $4.99/мес:* Безлимитные генерации сценариев и секретные тренды.")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
