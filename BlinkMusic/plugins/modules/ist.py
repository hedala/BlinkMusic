from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("istatistik"))
async def statistics(_, message):
    # İstatistikleri hesaplayın ve bir yanıt oluşturun
    sp_count = 0
    full_name = (await app.get_me()).mention
    response = f"🔸 {full_name} İstatistikleri\n\n"
    response += f"Özel Sohbetler: {private_chats}\n"
    response += f"  •• Kullanıcılar: {private_chats - bots}\n"
    response += f"  •• Botlar: {bots}\n"
    response += f"Gruplar: {groups}\n"
    response += f"Kanallar: {broadcast_channels}\n"
    response += f"Gruplarda Admin: {admin_in_groups}\n"
    response += f"  •• Oluşturan: {creator_in_groups}\n"
    response += f"  •• Admin Hakları: {admin_in_groups - creator_in_groups}\n"
    response += f"Kanallarda Admin: {admin_in_broadcast_channels}\n"
    response += f"  •• Oluşturan: {creator_in_channels}\n"
    response += f"  •• Admin Hakları: {admin_in_broadcast_channels - creator_in_channels}\n"
    response += f"Okunmamış Mesajlar: {unread}\n"
    response += f"Okunmamış Bahsetmeler: {unread_mentions}\n"
    response += f"Engellenen Kullanıcılar: {ct}\n"
    response += f"Toplam Yapıştırıcı Paketi Yüklendi: `{sp_count}`\n\n"
    response += f"__Geçen Süre:__ {stop_time:.02f}s\n"
    await message.reply(response)
