import asyncio
import logging
import sys
import wikipedia

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN
wikipedia.set_lang('en')



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Assalomu alaykum {html.bold(message.from_user.full_name)}, wikipediya botiga xush kelibsiz!\n"
                         f"BU bot sizga yozgan narsangiz haqida ingliz tilida maqolalar bolsa shuni yuboradi :) ")



@dp.message()
async def wiki(message: Message) -> None:
    try:
        respond = wikipedia.summary(message.text)
        await message.reply(respond)
    except :
        await message.answer("Afsuski bunday maqola topilmadi! :(")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())