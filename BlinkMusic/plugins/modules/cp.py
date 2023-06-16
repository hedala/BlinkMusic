import requests
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("cp"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].lower()  # İlk kelimeyi alıyoruz ve küçük harfe çeviriyoruz
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url).json()
    
    if crypto_symbol in response:
        crypto_price = response[crypto_symbol]["usd"]
        message.reply_text(f"{crypto_symbol.upper()} anlık fiyatı: {crypto_price} USD")
    else:
        message.reply_text("Hata: Kripto birimi bulunamadı!")
