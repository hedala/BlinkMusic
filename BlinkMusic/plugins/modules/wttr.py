from BlinkMusic import app
from pyrogram import filters
import requests

def get_weather_info(city):
    url = f"https://wttr.in/{city}?qmT0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
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
