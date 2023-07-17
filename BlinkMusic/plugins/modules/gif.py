from BlinkMusic import app
from pyrogram import filters
import requests
import random

# Tenor API'den GIF'leri almak için bir fonksiyon
def get_gifs_from_tenor(keyword):
    api_key = "AIzaSyBuGpE8dH_kR5s2yzp3yusdUiOhmaHs8_4"  # API anahtarınızı buraya ekleyin
    url = f"https://api.tenor.com/v1/search?q={keyword}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data)  # API yanıtını kontrol etmek için
    if "results" in data:
        gifs = data["results"]
        gif_urls = []
        for gif in gifs:
            gif_url = gif["media"][0]["gif"]["url"]
            gif_urls.append(gif_url)
        return gif_urls
    else:
        return None

@app.on_message(filters.command("gif"))
def send_gifs(_, message):
    keyword = message.text.split("/gif ", 1)[1]
    gif_urls = get_gifs_from_tenor(keyword)
    if gif_urls:
        random.shuffle(gif_urls)
        num_gifs_to_send = 3  # İstediğiniz sayıda GIF göndermek için değiştirilebilir
        gifs_to_send = gif_urls[:num_gifs_to_send]
        for gif_url in gifs_to_send:
            message.reply_animation(gif_url)
    else:
        message.reply_text("GIF bulunamadı.")

# app.run() satırını kaldırdık

