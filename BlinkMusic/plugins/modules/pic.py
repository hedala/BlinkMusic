from BlinkMusic import app
from pyrogram import filters

class BlinkBot:
    def __init__(self):
        # yapıcı fonksiyon kodu

    def start(self):
        # start fonksiyonu kodu

    def get_chat_photos(self, chat_id):
        # get_chat_photos fonksiyonu kodu
        pass

    async def send_all_profile_photos(self, chat_id, kullanici_id):
        # send_all_profile_photos fonksiyonu kodu
        toplam_sayi = await self.get_chat_members_count(chat_id)
        await self.send_message(chat_id, f"{toplam_sayi} adet fotoğraf buldum. Hemen indirip iletiyorum efendi {cevap.from_user.first_name}.")
        offset = None
        while True:
            uyeler = await self.get_chat_members(chat_id, limit=100)
            for uye in uyeler:
                if uye.user and uye.user.photo:
                    fotolar = await self.get_chat_photos(chat_id=uye.user.id)
                    for foto in fotolar:
                        dosya_id = foto.file_id
                        indirilen_foto = await self.download_media(dosya_id)
                        alt_baslik = f"{uye.user.first_name}'ın profil fotoğrafı:"
                        await self.send_photo(chat_id, indirilen_foto, caption=alt_baslik)
            if len(uyeler) < 100:
                break
            offset = uyeler[-1].user.id

@app.on_message(filters.command("pic"))
def send_profile_photo(_, message):
    # kodlar

@app.on_message(filters.command("picall"))
async def send_all_profile_photos(_, message):
    cevap = message.reply_to_message
    if cevap:
        kullanici_id = cevap.from_user.id
        sohbet_id = message.chat.id
        uyebilgisi = await app.get_chat_member(sohbet_id, kullanici_id)
        if uyebilgisi and uyebilgisi.user and uyebilgisi.user.photo:
            blink_bot = BlinkBot()
            await blink_bot.send_all_profile_photos(sohbet_id, kullanici_id)
        else:
            await app.send_message(sohbet_id, "Bu kullanıcının profil fotoğrafı bulunamadı.")
    else:
        await app.send_message(sohbet_id, "Bir kullanıcıya yanıt vererek bu komutu kullanmalısınız.")
