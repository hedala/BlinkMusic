from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("pic"))
def send_profile_photo(_, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        chat_id = message.chat.id
        
        # Kullanıcının profil fotoğrafını almak için getUserProfilePhotos metodu kullanılmalıdır.
        photos = app.get_user_profile_photos(user_id, limit=1)
        if photos and len(photos.photos) > 0:
            photo = app.get_file(photos.photos[0].file_id)
            # Profil fotoğrafını göndermek için send_photo metodunu kullanabilirsiniz
            app.send_photo(chat_id, photo.file_id)
        else:
            app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        app.send_message(chat_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
