from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("pic"))
def send_profile_photo(_, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        chat_id = message.chat.id
        
        # Kullanıcının profil fotoğrafını almak için get_chat_member metodu kullanılır.
        member = app.get_chat_member(chat_id, user_id)
        if member and member.user and member.user.photo:
            photo = app.get_file(member.user.photo.big_file_id)
            # Profil fotoğrafını göndermek için send_photo metodunu kullanabilirsiniz
            app.send_photo(chat_id, photo.file_id)
        else:
            app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        app.send_message(chat_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
