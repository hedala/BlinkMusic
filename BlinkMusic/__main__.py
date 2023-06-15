import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from BlinkMusic import LOGGER, app, userbot
from BlinkMusic.core.call import Blink
from BlinkMusic.plugins import ALL_MODULES
from BlinkMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("BlinkMusic").error("Pyrogram oturum dizisi ekleyin ve tekrar deneyin...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BlinkMusic.plugins" + all_module)
    LOGGER("BlinkMusic.plugins").info("Gerekli Modüller Başarıyla İçe Aktarıldı.")
    await userbot.start()
    await Blink.start()
    await Blink.decorators()
    LOGGER("BlinkMusic").info("Müzik Botu Başarıyla Başlatıldı.")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("BlinkMusic").info("Müzik Botu Durduruldu.")
