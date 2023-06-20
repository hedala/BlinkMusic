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
            caption = f"{reply.from_user.first_name}'ın profil fotoğrafı:"
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
            photos = app.get_user_profile_photos(user_id).photos
            if photos:
                app.send_message(chat_id, f"{len(photos)} adet fotoğraf buldum. Hemen indirip iletiyorum efendi {reply.from_user.first_name}.")
                for index, photo in enumerate(photos):
                    downloaded_photo = app.download_media(photo.file_id)
                    caption = f"{reply.from_user.first_name}'ın {index+1}. profil fotoğrafı:"
                    app.send_photo(chat_id, downloaded_photo, caption=caption)
            else:
                app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
        else:
            app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        app.send_message(chat_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
