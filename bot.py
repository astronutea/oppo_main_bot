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


@dp.callback_query(F.data == "info")
async def show_info(callback: types.CallbackQuery):
    await callback.message.answer(f"1️⃣ Все оформленные запросы на получение вознаграждения, за исключением запросов, которые противоречат правилам Акции, будут выплачены в ближайшие дни. На данный момент выплаты идут.\n"
                                  f"2️⃣ Прямо сейчас все еще есть участники, у которых соблюдены все условия. Призовой фонд Акции подходит к концу, рекомендуем поторопиться!\n"
                                  f"Как только призовой фонд будет исчерпан, мы не сможем принимать новые запросы на получение вознаграждения.\n"
                                  f"🔍Пожалуйста, проверьте, что вы выполнили ВСЕ условия получения вознаграждения:\n"
                                  f"- игровая сессия минимум 3 дня подряд (в течение каждого дня нужно было заходить в игру, совершать игровые действия)\n"
                                  f"- выполнение как минимум 4-х заданий\n"
                                  f"- более 100 000 орехов на балансе\n"
                                  f"- вы еще не получали выплату\n"
                                  f"🏆Если вы уверены, что все выполнили, то вам нужно нажать «Получить вознаграждение» во вкладке «Обмен». Проверка условий автоматическая.\n"
                                  f"Если вы уже были в боте выплат до момента выполнения условий, то обязательно нажмите /start, когда зайдете в него снова.\n"
                                  f"⏰ Призовой фонд выплачивается до момента его исчерпания или до 27 августа 2024 года.\n"
                                  f"Оставайтесь на связи с нами в официальном канале OPPO Россия в Telegram. Мы готовим для вас что-то особенное. 🎁",
                                  reply_markup=main_kb)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())