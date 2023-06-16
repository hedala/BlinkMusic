from BlinkMusic import app
from pyrogram import filters
from PIL import Image, ImageDraw, ImageFont
import io

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message

    # Kullanıcı ve grup kimliklerini alın
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Arka plan rengini ve boyutunu belirleyin
    background_color = (0, 0, 0)  # Siyah arka plan rengi
    image_width = 500
    image_height = 200

    # Yazı stilleri ve boyutları
    font = ImageFont.truetype("arial.ttf", 18)  # Kullanılacak yazı tipini ve boyutunu belirtin
    text_color = (255, 255, 255)  # Yazı rengini belirtin

    # Resmi oluşturun
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    draw.text((50, 50), f"Bu senin kimliğin: {user_id}", font=font, fill=text_color)
    if reply:
        reply_user_id = reply.from_user.id
        reply_user_name = reply.from_user.first_name
        draw.text((50, 80), f"{reply_user_name}'in ID'si: {reply_user_id}", font=font, fill=text_color)
    draw.text((50, 110), f"Bu grubun kimliği: {chat_id}", font=font, fill=text_color)

    # Resmi bir byte dizisine dönüştürün
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    # Resmi gönderin
    message.reply_photo(image_bytes, caption="Kimlik bilgileri")

    # Belleği temizleyin
    image.close()
    image_bytes.close()
