import sys

from pyrogram import Client

import config

from ..logging import LOGGER

class BlinkBot(Client):
    def __init__(self):
        LOGGER(name).info(f"Bot Başlatılıyor...")
        super().__init__(
            "Müzik",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(name).error(
                "Lütfen Logger Grubunda Bot'u yönetici olarak atayın"
            )
            sys.exit()
        LOGGER(name).info(f"{self.name} Olarak MüzikBot'u Başlattı")
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} Bot Başlatıldı:**\n\n✨ ID : `{self.id}`\n❄️ İsim : {self.name}\n💫 Kullanıcı Adı : @{self.username}"
            )
        except:
            LOGGER(name).error(
                "Bot, log Grubuna erişmeyi başaramadı. Botunuzu günlük kanalınıza eklediğinizden ve yönetici olarak atadığınızdan emin olun!"
            )
            sys.exit()
