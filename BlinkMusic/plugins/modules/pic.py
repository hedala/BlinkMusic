from BlinkMusic import app
from pyrogram import filters


@app.on_message(filters.command("pic"))
def get_profile_photo(_, message):
    user = message.from_user
    if user.photo:
        photo = user.photo.big_file_id
        app.download_media(photo, file_name="profile_photo.jpg")
        message.reply_photo("profile_photo.jpg")
    else:
        message.reply_text("Profil fotoğrafı bulunamadı.")


@app.on_message(filters.command("picall"))
def get_all_profile_photos(_, message):
    user = message.from_user
    if user.photos:
        photos = user.photos
        for index, photo in enumerate(photos.total_count):
            app.download_media(photo.big_file_id, file_name=f"profile_photo_{index}.jpg")
            message.reply_photo(f"profile_photo_{index}.jpg")
    else:
        message.reply_text("Profil fotoğrafı bulunamadı.")
