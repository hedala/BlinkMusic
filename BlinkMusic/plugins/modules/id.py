from BlinkMusic import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"Bu senin kimliğin: {message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: {reply.from_user.id}\n**Bu grubun kimliği**: {message.chat.id}`"
        )
    else:
        message.reply(
            f"Bu senin kimliğin: {message.from_user.id}`\n**Bu grubun kimliği**: {message.chat.id}`"
        )
