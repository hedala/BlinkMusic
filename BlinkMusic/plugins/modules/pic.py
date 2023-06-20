from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("pic"))
def send_profile_photo(_, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        chat_id = message.chat.id
        member = app.get_chat_member(chat_id, user_id)
        if member and member.user and member.user.photo:
            photo = member.user.photo.big_file_id
            downloaded_photo = app.download_media(photo)
            caption = f"{reply.from_user.first_name}'nın profil fotoğrafı:"
            app.send_photo(chat_id, downloaded_photo, caption=caption)
        else:
            app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        app.send_message(chat_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")

@app.on_message(filters.command("picall"))
def send_all_profile_photos(_, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        chat_id = message.chat.id
        member = app.get_chat_member(chat_id, user_id)
        if member and member.user and member.user.photo:
            photos = app.get_user_profile_photos(user_id)
            if photos.total_count > 0:
                app.send_message(chat_id, f"{photos.total_count} adet fotoğraf buldum. Hemen indirip iletiyorum efendi {reply.from_user.first_name}.")
                for photo in photos.photos:
                    file_id = photo[0].file_id
                    downloaded_photo = app.download_media(file_id)
                    caption = f"{reply.from_user.first_name}'ın profil fotoğrafı:"
                    app.send_photo(chat_id, downloaded_photo, caption=caption)
            else:
                app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
        else:
            app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        app.send_message(chat_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
