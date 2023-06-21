import requests
from datetime import datetime
from BlinkMusic import app
from pyrogram import filters

API_KEY = "4160fb7f3780456d8b9103155232903"  # WeatherAPI.com API anahtarını buraya ekleyin

# Kullanıcıların ID'lerini ve tercih ettikleri şehirleri saklamak için bir sözlük oluşturulur
user_cities = {}

@app.on_message(filters.command("hava"))
def get_weather(_, message):
    user_id = message.from_user.id
    command_parts = message.text.split(" ")

    if len(command_parts) == 2 and command_parts[1] != "":
        city = command_parts[1]
        user_cities[user_id] = city  # Kullanıcının tercih ettiği şehri kaydet

    elif user_id in user_cities:
        city = user_cities[user_id]
    else:
        message.reply_text("Lütfen bir şehir adı belirtin.")
        return

    # Hava durumu tahminleri için API'ye istek gönderir
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&lang=tr"
    response = requests.get(url).json()

    if "error" not in response:
        # API'den dönen verilere göre hava durumu bilgilerini alır
        location = response["location"]["name"]
        current_weather = response["current"]["condition"]["text"]
        current_temperature = response["current"]["temp_c"]
        current_humidity = response["current"]["humidity"]
        last_updated = response["current"]["last_updated"]

        # İleriye dönük tahminlerin alınması
        forecast_data = response["forecast"]["forecastday"]
        forecast_info = []

        for forecast in forecast_data:
            date = datetime.strptime(forecast["date"], "%Y-%m-%d").strftime("%d.%m.%Y")
            weather = forecast["day"]["condition"]["text"]
            max_temp = forecast["day"]["maxtemp_c"]
            min_temp = forecast["day"]["mintemp_c"]
            forecast_info.append(f"{date}: {weather}, Max: {max_temp}°C, Min: {min_temp}°C")

        # Son güncelleme zamanını formatlar
        last_updated_datetime = datetime.strptime(last_updated, "%Y-%m-%d %H:%M")
        last_updated_formatted = last_updated_datetime.strftime("%d.%m.%Y %H:%M")

        # Mesajı oluşturarak kullanıcıya yanıt verir
        reply_text = f"<b>Hava Durumu Bilgileri</b>\n\n"
        reply_text += f"<b>Şehir:</b> {location} ({city})\n"
        reply_text += f"<b>Güncel Durum:</b> {current_weather}\n"
        reply_text += f"<b>Sıcaklık:</b> {current_temperature}°C\n"
        reply_text += f"<b>Nem:</b> {current_humidity}%\n"
        reply_text += f"<b>Son Güncelleme:</b> {last_updated_formatted}\n\n"
        reply_text += "<b>İleriye Dönük Tahminler:</b>\n"
        reply_text += "\n".join(forecast_info)
        
        message.reply_text(reply_text, parse_mode="HTML")
    else:
        error_message = response["error"]["message"]
        message.reply_text(f"<b>Hata:</b> Hava durumu bilgileri alınamadı. {error_message}", parse_mode="HTML")
