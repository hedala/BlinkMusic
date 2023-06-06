from BlinkMusic import app

from pyrogram import filters

# Sadece grup sohbetlerinde çalışacak bir filtre tanımlama

group_filter = filters.group

# 'user_to_message_count' adlı boş bir sözlük tanımlama

user_to_message_count = {}

@app.on_message(filters.command("id"))

def ids(_, message):

    # Mesajı gönderen kullanıcının ID'si ile sohbet ID'sini al

    user_id, chat_id = message.from_user.id, message.chat.id

    # Eğer kullanıcı özel bir sohbetteyse bir uyarı göster

    if message.chat.type == "private":

        message.reply_text("Bu komut yalnızca grup sohbetlerinde çalışıyor!")

        return

    # Daha önce mesaj sayısını kaydettiğimiz kullanıcı sözlükte varsa "user_count"

    user_count = user_to_message_count.get(user_id, 0)

    # "user_count" mesaj sayısını 1 arttır

    user_count += 1

    # Kullanıcıyı sözlükte güncelle

    user_to_message_count[user_id] = user_count

    # Yinelemeli olarak kullanıcının adını ve mesaj sayısını bulmak için `member_count`'u kullanın.

    # Burada, bir 'inline if' ifadesi kullanıyoruz.

    member_count = sum((1 for member in app.iter_chat_members(chat_id) if member.user.id == user_id))

    # Mesajları yanıtlarken, kaç mesaj gönderdiğini de göster.

    reply = message.reply_to_message

    if reply:

        message.reply_text(

            f"Bu senin kimliğin: {user_id}\n{reply.from_user.first_name}'s ɪᴅ: {reply.from_user.id}\nBu grubun kimliği: {chat_id}\nMesaj sayınız: {user_count}\n{reply.from_user.first_name} bu grupta toplam {member_count} mesaj gönderdi."

        )

    else:

        message.reply_text(

            f"Bu senin kimliğin: {user_id}\nBu grubun kimliği: {chat_id}\nMesaj sayınız: {user_count}\nToplam mesaj sayısı: {member_count}"

        )
