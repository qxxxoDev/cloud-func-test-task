import aiohttp, asyncio
from config import API_URL
from store import save

async def __call(attempt=0):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            res = await response.json()

            if res['success']:
                id = res['timestamp']
                usd_eur = res['quotes']['USDEUR']
                save(id, usd_eur)
            else:
                print('Failed. Restarting...')
                if (attempt < 5):
                    await asyncio.sleep(10)
                    new_attempt = attempt + 1
                    return await __call(new_attempt)
                else:
                    from bot import notify
                    notify()

def call_api():
    """
    Вызов API. В случае, если данные успешно получены
    функция сохраняет их, а иначе программа пробует дернуть API
    сервер еще максимум 4 раза с задержкой 10с между запросами,
    если же лимит попыток исчерпан, то Телеграм бот уведомит
    администратора сообщением о проблеме с сервером.
    """
    asyncio.run(__call())