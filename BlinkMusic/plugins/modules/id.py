from BlinkMusic import app
from pyrogram import filters

def ids(_, message):
    reply = message.reply_to_message
    total_messages = app.get_chat_member(message.chat.id, message.from_user.id).user.total_messages
    if reply:
        return (
            f"**Bu senin kimliğin**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**Bu grubun kimliği**: `{message.chat.id}`\n**Toplam gönderdiğin mesaj sayısı**: `{total_messages}`"
        )
    else:
        return (
            f"**Bu senin kimliğin**: `{message.from_user.id}`\n**Bu grubun kimliği**: `{message.chat.id}`\n**Toplam gönderdiğin mesaj sayısı**: `{total_messages}`"
        )

@app.on_message(filters.command("id"))
def handle_ids(_, message):
    result = ids(_, message)
    message.reply_text(result)
