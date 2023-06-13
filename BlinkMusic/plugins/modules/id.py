from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        user_name = reply.from_user.first_name
        group_id = message.chat.id
        message.reply_text(f"**Bu senin kimliğin:** {message.from_user.id}`\n**{user_name}'s ɪᴅ**: {user_id}\n **Bu grubun kimliği:** {group_id}`")
    else:
        user_id = message.from_user.id
        group_id = message.chat.id
        message.reply_text(f"**Bu senin kimliğin:** {user_id}`\n **Bu grubun kimliği:** {group_id}`")

@app.on_message(filters.group)
def count_messages(_, message):
    user_id = message.from_user.id
    group_id = message.chat.id
    member = app.get_chat_member(group_id, user_id)
    message_count = member.user.status.mesaj_gönderme_sayısı
    message.reply_text(f"**Bu kullanıcının grup içinde gönderdiği mesaj sayısı:** {message_count}")

