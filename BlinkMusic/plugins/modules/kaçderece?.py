import requests
from datetime import datetime, timedelta
from BlinkMusic import app
from pyrogram import filters, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

API_KEY = "4160fb7f3780456d8b9103155232903"  # WeatherAPI.com API anahtarını buraya ekleyin

# Kullanıcıların ID'lerini ve tercih ettikleri şehirleri saklamak için bir sözlük oluşturulur
user_cities = {}

@app.on_message(filters.command("hava"))
async def get_weather(_, message):
    user_id = message.from_user.id
    command_parts = message.text.split(" ")

    if len(command_parts) == 2 and command_parts[1] != "":
        city = command_parts[1]
        user_cities[user_id] = city  # Kullanıcının tercih ettiği şehri kaydet

    elif user_id in user_cities:
        city = user_cities[user_id]
    else:
        await message.reply_text("Lütfen bir şehir adı belirtin.")
        return

    # Hava durumu tahminleri için API'ye istek gönderir
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&lang=tr"
    response = requests.get(url).json()

    if "error" not in response:
        # API'den dönen verilere göre hava durumu bilgilerini alır
        location = response["location"]["name"]
        current_weather = response["current"]["condition"]["text"]
        current_temperature = response["current"]["temp_c"]
        feels_like = response["current"]["feelslike_c"]
        current_humidity = response["current"]["humidity"]
        last_updated = response["current"]["last_updated"]

        # Son güncelleme zamanını formatlar
        last_updated_datetime = datetime.strptime(last_updated, "%Y-%m-%d %H:%M")
        last_updated_formatted = last_updated_datetime.strftime("%d.%m.%Y %H:%M")

        # "Hava durumu bilgileri alınıyor..." mesajını gönderir
        loading_message = await message.reply_text("Hava durumu bilgileri alınıyor...")

        # 4 saniye boyunca yükleme hissiyatı için periyotlarla mesajı günceller
        await asyncio.sleep(0.5)
        await loading_message.edit_text("Hava durumu bilgileri alınıyor.")
        await asyncio.sleep(0.5)
        await loading_message.edit_text("Hava durumu bilgileri alınıyor..")
        await asyncio.sleep(0.5)
        await loading_message.edit_text("Hava durumu bilgileri alınıyor...")

        await asyncio.sleep(0.5)  # Toplamda 2 saniye bekleme süresi

        # Güncelleme butonunu oluşturur
        update_button = InlineKeyboardButton("Güncelle", callback_data="update_weather")

        # İnline klavyeyi oluşturur
        keyboard = InlineKeyboardMarkup([[update_button]])

        # Mesajı oluşturarak kullanıcıya yanıt verir
        reply_text = f"🌍 <b>{city} için Hava Durumu Bilgileri</b> 🌍\n\n"
        reply_text += f"<b>Güncel Durum:</b> {current_weather}\n"
        reply_text += f"<b>Sıcaklık:</b> {current_temperature}°C\n"
        reply_text += f"<b>Hissedilen Sıcaklık:</b> {feels_like}°C\n"
        reply_text += f"<b>Nem:</b> {current_humidity}%\n"
        reply_text += f"<b>Son Güncelleme:</b> {last_updated_formatted}\n"

        await loading_message.edit_text(reply_text, reply_markup=keyboard, parse_mode="HTML")
    else:
        error_message = response["error"]["message"]
        await message.reply_text(f"<b>Hata:</b> Hava durumu bilgileri alınamadı. {error_message}", parse_mode="HTML")

# Callback verilerini dinleyen bir fonksiyon tanımlar
@app.on_callback_query()
async def handle_callback(_, callback_query):
    if callback_query.data == "update_weather":
        await get_weather(_, callback_query.message)  # Hava durumunu güncellemek için `get_weather` işlevini tekrar çağırır
