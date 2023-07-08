import requests
from BlinkMusic import app
from pyrogram import filters


def get_weather(city):
    url = f"https://wttr.in/{city.replace(' ', '+')}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "Hava durumu bilgisi alınamadı."


@app.on_message(filters.command("hv"))
def weather(_, message):
    if len(message.command) > 1:
        city = " ".join(message.command[1:])
        weather_info = get_weather(city)
        message.reply_text(weather_info)
    else:
        message.reply_text("Lütfen bir şehir adı belirtin.")


if __name__ == "__main__":
    app.run()
