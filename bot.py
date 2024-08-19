import asyncio
import logging

from aiogram import Bot, Dispatcher, types, exceptions
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from config import BOT_TOKEN
from db_request import registration_ref
from keyboards import main_kb

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start_command(message: Message, command: CommandObject):
    # Получаем параметры из команды /start
    command_args: str = command.args
    try:
        await message.answer("Привет!\n\n"
                             "Добро пожаловать в игру <em><b>КрепкийOPPOрешек!</b></em>🌰\n\n"
                             "Здесь вы сможете весело провести время, познакомиться с новинками смартфонов OPPO и заработать реальные деньги.\n\n"
                             "Нажимайте на экран, чтобы <em>колоть орехи</em>, и выполняйте задания, чтобы увеличить свой доход!\n\n"
                             "Не забывайте о <b>друзьях</b> — приводите их в игру и зарабатывайте еще больше вместе!",
                             reply_markup=main_kb, parse_mode=ParseMode.HTML)
        registration_ref(message.from_user.username, message.from_user.first_name, message.from_user.last_name, int(message.from_user.id), str(command_args))
    except exceptions.TelegramForbiddenError:
        print(f"Пользователь {message.from_user.id} заблокировал бота")


@dp.callback_query(F.data == "rules")
async def show_rules(callback: types.CallbackQuery):
    await callback.message.answer(f"<em><ins>Правила игры:</ins></em>\n\n"
                                  f"- Нажимайте на экран, чтобы колоть орехи.\n\n"
                                  f"- <b>Выполняйте задания</b>, чтобы заработать еще больше!\n\n"
                                  f"- Заходите в игру <b>регулярно</b>, чтобы собрать больше ядер орехов для обмена на реальные деньги.\n\n"
                                  f"- <b>Приглашайте друзей</b>, чтобы зарабатывать вместе еще больше.\n\n"
                                  f"- <b>Следите за новостями</b>, чтобы не пропустить все самое интересное!",
                                  parse_mode=ParseMode.HTML, reply_markup=main_kb)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())