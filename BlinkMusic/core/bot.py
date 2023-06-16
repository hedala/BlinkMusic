import sys
from pyrogram import Client
import config
from ..logging import LOGGER

class BlinkBot(Client):
    def __init__(self):
        LOGGER(__name__).info("Bot Başlatılıyor...")
        super().__init__(
            "Music",
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
            LOGGER(__name__).error(
                "Lütfen Bot'u Logger Grubunda Admin olarak yetkilendirin"
            )
            sys.exit()
        LOGGER(__name__).info(f"MusicBot, {self.name} olarak başlatıldı")
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ʙᴏᴛ Başlatıldı :**\n\n✨ ɪᴅ : `{self.id}`\n❄ ɴᴀᴍᴇ : {self.name}\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "Bot, log grubuna erişmekte başarısız oldu. Lütfen botunuzu log kanalınıza eklediğinizden ve admin olarak yetkilendirdiğinizden emin olun!"
            )
            sys.exit()
