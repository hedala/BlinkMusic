from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from BlinkMusic.utils.database import is_on_off
from BlinkMusic import app


async def create_chat_invite_link(chat):
    chat_id = chat.id
    if (await app.get_chat_member(chat_id, "me")).can_manage_chat:
        try:
            link = await app.export_chat_invite_link(chat_id)
            return link
        except Exception as e:
            return False
    return False

async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Özel Sohbet"
        logger_text = f"""
** {MUSIC_BOT_NAME} Müzik Kayıtları **
** Sohbet Adı :** {message.chat.title} [`{message.chat.id}`]
** İsim :** {message.from_user.mention}
** Kullanıcı Adı :** @{message.from_user.username}
** Kimlik :** `{message.from_user.id}`
** Chat Bağlantısı:** {chatusername}
** Davet Bağlantısı:** {await create_chat_invite_link(message.chat)}
** Aranan İfade:** {message.text}
** Yayın Türü:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
