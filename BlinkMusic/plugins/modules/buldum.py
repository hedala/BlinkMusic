from BlinkMusic import app
from pyrogram import filters


@app.on_message(filters.command("ara"))
def search(_, message):
    keyword = message.text.split(maxsplit=1)[1]  # Alınan kelimeyi elde ediyoruz
    chat_id = message.chat.id
    messages = []
    member_count = app.get_chat_members_count(chat_id)

    if member_count > 0:
        messages = app.get_chat_history(chat_id, limit=member_count)

    found_messages = []

    for msg in messages:
        if keyword.lower() in msg.text.lower():  # Kelimeyi büyük/küçük harf duyarlılığı olmadan arıyoruz
            found_messages.append(msg)

    if found_messages:
        reply_text = f"Grup içerisinde aratılan '{keyword}' kelimesinin sonuçları ({len(found_messages)} adet):\n\n"
        for msg in found_messages:
            reply_text += f"[Mesaj Linki](https://t.me/{chat_id}/{msg.message_id})\n"

        message.reply_text(reply_text)
    else:
        message.reply_text(f"Grup içerisinde aratılan '{keyword}' kelimesine ilişkin bir sonuç bulunamadı.")


if __name__ == "__main__":
    app.run()
