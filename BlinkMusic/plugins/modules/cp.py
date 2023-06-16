import requests
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("cp"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].upper()  # İlk kelimeyi alıyoruz ve büyük harfe çeviriyoruz
    url = f"https://api.coincap.io/v2/assets/{crypto_symbol}/"
    response = requests.get(url).json()
    
    if "data" in response:
        crypto_name = response["data"]["name"]
        crypto_price = response["data"]["priceUsd"]
        message.reply_text(f"{crypto_name} ({crypto_symbol}) anlık fiyatı: {crypto_price} USD")
    else:
        message.reply_text("Hata: Kripto birimi bulunamadı!")

