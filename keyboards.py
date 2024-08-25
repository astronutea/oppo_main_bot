from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import GAME_URL, SUPPORT_BOT_URL

builder_main_kb = InlineKeyboardBuilder()

builder_main_kb.row(types.InlineKeyboardButton(text="Играть!", url=GAME_URL))
builder_main_kb.row(types.InlineKeyboardButton(text="❗️ВАЖНАЯ ИНФОРМАЦИЯ❗️", callback_data="info"))
builder_main_kb.row(types.InlineKeyboardButton(text="Правила игры", callback_data="rules"))
builder_main_kb.row(types.InlineKeyboardButton(text="Чат технической поддержки", url=SUPPORT_BOT_URL))

main_kb = builder_main_kb.as_markup(resize_keyboard=True)
