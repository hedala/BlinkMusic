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
            total_count = app.get_chat_members_count(chat_id)
            app.send_message(chat_id, f"{total_count} adet fotoğraf buldum. Hemen indirip iletiyorum efendi {reply.from_user.first_name}.")
            offset = 0
            while True:
                photos = app.get_chat_member(chat_id, user_id, offset=offset, limit=100).user.photos
                for photo in photos:
                    file_id = photo.big_file_id
                    downloaded_photo = app.download_media(file_id)
                    caption = f"{reply.from_user.first_name}'ın profil fotoğrafı:"
                    app.send_photo(chat_id, downloaded_photo, caption=caption)
                offset += len(photos)
                if len(photos) < 100:
                    break
        else:
            app.send_message(chat_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        app.send_message(chat_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
