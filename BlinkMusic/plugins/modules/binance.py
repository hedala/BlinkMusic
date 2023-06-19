import requests
from BlinkMusic import app
from pyrogram import filters

# Yeni özellik: Binance API'den anlık kripto fiyatlarını çekme
def get_crypto_price(symbol):
    url = f"https://api3.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'price' in data:
            return data['price']
    return None

@app.on_message(filters.command("price"))
def get_price(_, message):
    symbol = message.text.split()[1].upper()
    price = get_crypto_price(symbol)
    if price:
        message.reply_text(f"{symbol} fiyatı: {price}")
    else:
        message.reply_text(f"{symbol} fiyatı bulunamadı.")
