from datetime import datetime
from BlinkMusic import app
from pyrogram import filters
import requests

def get_weather_info(city):
    url = f"https://wttr.in/{city}?qT0m"
    response = requests.get(url)
    if response.status_code == 200:
        weather_info = response.text.strip()
        return f"Hava Durumu (Son Güncelleme Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}):\n\n{weather_info}"
    return "Hava durumu bilgisi alınamadı."

@app.on_message(filters.command("hv"))
def weather(_, message):
    if len(message.command) > 1:
        city = " ".join(message.command[1:])
        weather_info = get_weather_info(city)
        message.reply_text(weather_info)
    else:
        message.reply_text("Lütfen bir şehir adı belirtin.")

if __name__ == "__main__":
    app.run()
