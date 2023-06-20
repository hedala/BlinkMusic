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
async def send_all_profile_photos(_, message):
    cevap = message.reply_to_message
    if cevap:
        kullanici_id = cevap.from_user.id
        sohbet_id = message.chat.id
        uyebilgisi = await app.get_chat_member(sohbet_id, kullanici_id)
        if uyebilgisi and uyebilgisi.user and uyebilgisi.user.photo:
            toplam_sayi = await app.get_chat_members_count(sohbet_id)
            await app.send_message(sohbet_id, f"{toplam_sayi} adet fotoğraf buldum. Hemen indirip iletiyorum efendi {cevap.from_user.first_name}.")
            offset = None
            while True:
                uyeler = await app.get_chat_members(sohbet_id, limit=100)
                for uye in uyeler:
                    if uye.user and uye.user.photo:
                        fotolar = await app.get_chat_photos(chat_id=uye.user.id)
                        for foto in fotolar:
                            dosya_id = foto.file_id
                            indirilen_foto = await app.download_media(dosya_id)
                            alt_baslik = f"{uye.user.first_name}'ın profil fotoğrafı:"
                            await app.send_photo(sohbet_id, indirilen_foto, caption=alt_baslik)
                if len(uyeler) < 100:
                    break
            offset = uyeler[-1].user.id
        else:
            await app.send_message(sohbet_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        await app.send_message(sohbet_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
