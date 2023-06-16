from BlinkMusic import app
from pyrogram import filters
from PIL import Image, ImageDraw, ImageFont

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message

    # Kullanıcı ve grup kimliklerini alın
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Arka plan resmini yükleyin
    background_image = Image.open("background.jpg")  # Arka plan resminin dosya adını ve yolunu belirtin

    # Yazı stilleri ve boyutları
    font = ImageFont.truetype("arial.ttf", 18)  # Kullanılacak yazı tipini ve boyutunu belirtin
    text_color = (255, 255, 255)  # Yazı rengini belirtin

    # Resme yazıları ekleyin
    draw = ImageDraw.Draw(background_image)
    draw.text((50, 50), f"Bu senin kimliğin: {user_id}", font=font, fill=text_color)
    if reply:
        reply_user_id = reply.from_user.id
        reply_user_name = reply.from_user.first_name
        draw.text((50, 80), f"{reply_user_name}'in ID'si: {reply_user_id}", font=font, fill=text_color)
    draw.text((50, 110), f"Bu grubun kimliği: {chat_id}", font=font, fill=text_color)

    # Resmi kaydedin veya başka bir şekilde paylaşın
    output_filename = "id_info.jpg"  # Kaydedilecek resmin dosya adını ve yolunu belirtin
    background_image.save(output_filename)

    # Resmi gönderin
    message.reply_photo(output_filename)

    # Kaynak resmi temizleyin (isteğe bağlı)
    background_image.close()
