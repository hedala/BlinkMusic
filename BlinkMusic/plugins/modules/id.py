from BlinkMusic import app

from pyrogram import filters

user_message_count = {}

@app.on_message(filters.command("id"))

def ids(_, message):

    user_id = message.from_user.id

    chat_id = message.chat.id

    # Kullanıcıyı uyar

    if message.chat.type == "private":

        message.reply_text("Bu komutu grup sohbetinde kullanmalısınız.")

    # Mesajı yanıtlanan kullanıcının mesaj sayısını al

    reply = message.reply_to_message

    if reply:

        replied_user_id = reply.from_user.id

        if replied_user_id in user_message_count:

            message_count = user_message_count[replied_user_id]

        else:

            message_count = 0

        message.reply_text(

            f"Bu senin kimliğin: {user_id}\n{reply.from_user.first_name}'s ɪᴅ: {replied_user_id}\nBu grubun kimliği: {chat_id}\nMesaj sayısı: {message_count}"

        )

    else:

        message.reply(

            f"Bu senin kimliğin: {user_id}\nBu grubun kimliği: {chat_id}"

        )

@app.on_message(filters.text & ~filters.command)

def update_message_count(_, message):

    user_id = message.from_user.id

    if user_id in user_message_count:

        user_message_count[user_id] += 1

    else:

        user_message_count[user_id] = 1

@app.on_message(filters.left_chat_member)

def remove_user_message_count(_, message):

    user_id = message.left_chat_member.id

    if user_id in user_message_count:

        del user_message_count[user_id]
