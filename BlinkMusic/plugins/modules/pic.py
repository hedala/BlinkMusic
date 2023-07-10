from pyrogram import Client, filters
from BlinkMusic import app

def get_profile_photo(app, user_id):
    photos = app.get_profile_photos(user_id, limit=1)
    if photos.total_count > 0:
        photo = photos[0]
        photo_path = app.download_media(photo.file_id)
        return photo_path
    else:
        return None

def get_all_profile_photos(app, user_id):
    photos = app.get_profile_photos(user_id, limit=1000)
    photo_paths = []
    for photo in photos.photos:
        photo_path = app.download_media(photo.file_id)
        photo_paths.append(photo_path)
    return photo_paths

@app.on_message(filters.command("pic"))
def pic(_, message):
    user_id = message.from_user.id
    photo_path = get_profile_photo(app, user_id)
    if photo_path != None:
        with open(photo_path, 'rb') as photo:
            message.reply_photo(photo)
    else:
        message.reply("Profil fotoğrafı bulunamadı.")

@app.on_message(filters.command("picall"))
def picall(_, message):
    user_id = message.from_user.id
    photo_paths = get_all_profile_photos(app, user_id)
    for photo_path in photo_paths:
        if photo_path != None:
            with open(photo_path, 'rb') as photo:
                message.reply_photo(photo)
        else:
            message.reply("Profil fotoğrafları bulunamadı.")
