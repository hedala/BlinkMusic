import requests
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

    # Hava durumu API'sine istek gönderir
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url).json()

    if "error" not in response:
        # API'den dönen verilere göre hava durumu bilgilerini alır
        location = response["location"]["name"]
        weather = response["current"]["condition"]["text"]
        temperature = response["current"]["temp_c"]
        humidity = response["current"]["humidity"]

        # Mesajı oluşturarak kullanıcıya yanıt verir
        reply_text = (
            f"Hava durumu bilgileri {location} ({city}) için:\n"
            f"Durum: {weather}\n"
            f"Sıcaklık: {temperature}°C\n"
            f"Nem: {humidity}%"
        )
        message.reply_text(reply_text)
    else:
        error_message = response["error"]["message"]
        message.reply_text(f"Hava durumu bilgileri alınamadı. Hata: {error_message}")
