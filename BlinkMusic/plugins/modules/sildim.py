from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("sil"))
def delete_messages(_, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reply_message_id = message.reply_to_message.message_id

        app.delete_messages(chat_id, range(reply_message_id, message.message_id + 1))
        message.reply_text("Mesajlar silindi.")
    else:
        message.reply_text("Sil komutunu bir mesajın üzerinde kullanmalısınız.")

