from BlinkMusic import app
from pyrogram import filters


def is_group_admin(chat_id, user_id):
    chat_member = app.get_chat_member(chat_id, user_id)
    return chat_member.status in ("owner", "administrator")


@app.on_message(filters.command("sil") & filters.group)
def delete_messages(_, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reply_message_id = message.reply_to_message.message_id
        user_id = message.from_user.id

        if is_group_admin(chat_id, user_id) or user_id == app.get_me().id:
            try:
                app.delete_messages(chat_id, range(reply_message_id, message.message_id + 1))
                message.reply_text("Mesajlar silindi.")
            except Exception as e:
                message.reply_text("Mesajları silerken bir hata oluştu.")
                app.send_message(user_id, f"Silme işlemi sırasında bir hata oluştu: {str(e)}")
        else:
            message.reply_text("Bu komutu kullanma yetkiniz bulunmuyor.")
    else:
        message.reply_text("Sil komutunu bir mesajın üzerinde kullanmalısınız.")
