import asyncio, nest_asyncio
from aiogram import Bot, dispatcher, executor
from config import BOT_TOKEN, BOT_ADMINS

bot = Bot(BOT_TOKEN)
dp = dispatcher.Dispatcher(bot)

async def send_msg(dp):
    """ 
    Отправляет уведомление админу об ошибке API сервера.
    """

    for admin in BOT_ADMINS:
        await bot.send_message(admin, 'Что-то не так с API :(')

    asyncio.get_event_loop().stop()

def notify():
    """
    Запускает работу бота и сразу же вызывает
    функцию `send_msg` для отправки уведомления.
    """

    nest_asyncio.apply()
    executor.start_polling(dp, on_startup=send_msg)