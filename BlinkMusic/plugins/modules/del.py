from BlinkMusic import app
from pyrogram import filters


@app.on_message(filters.command("del") & filters.group)
def delete_messages(_, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reply_message_id = message.reply_to_message.message_id
        message_count = message.message_id - reply_message_id + 1

        if app.get_chat_member(chat_id, message.from_user.id).status in ("creator", "administrator"):
            try:
                app.delete_messages(chat_id, range(reply_message_id, message.message_id + 1))
                message.reply_text(f"{message_count} mesaj silindi.")
            except Exception as e:
                message.reply_text("Mesajları silerken bir hata oluştu.")
                app.send_message(message.from_user.id, f"Silme işlemi sırasında bir hata oluştu: {str(e)}")
        else:
            message.reply_text("Bu komutu kullanma yetkiniz bulunmuyor.")
    else:
        message.reply_text("Sil komutunu bir mesajın üzerinde kullanmalısınız.")
