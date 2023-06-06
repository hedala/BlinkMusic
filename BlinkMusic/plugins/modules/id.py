from BlinkMusic import app, db

from pyrogram import filters

@app.on_message(filters.command("id"))

def ids(_, message):

    reply = message.reply_to_message

    if reply:

        message.reply_text(

            f"Bu senin kimliğin: {message.from_user.id}\n{reply.from_user.first_name}'s ɪᴅ: {reply.from_user.id}\nBu grubun kimliği: {message.chat.id}"

        )

    else:

        message.reply(

            f"Bu senin kimliğin: {message.from_user.id}\nBu grubun kimliği: {message.chat.id}"

        )

@app.on_message(filters.text & ~filters.private)

def count_messages(_, message):

    user_id = message.from_user.id

    chat_id = message.chat.id

    user_data = db.get(f"{user_id}-{chat_id}")

    if not user_data:

        user_data = {"message_count": 0}

    user_data["message_count"] += 1

    db.set(f"{user_id}-{chat_id}", user_data)

    

@app.on_message(filters.command("id", prefixes="/") & filters.private)

def warn_user(_, message):

    message.reply_text("Bu komutu özel bir sohbette kullanamazsın.")
