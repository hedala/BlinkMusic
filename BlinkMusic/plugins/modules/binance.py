from BlinkMusic import app
from pyrogram import filters
import requests

def get_crypto_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    try:
        price = float(data["price"])
        return price
    except KeyError:
        return None

@app.on_message(filters.command("coin"))
def coin(_, message):
    price = get_crypto_price()
    if price is not None:
        reply_text = f"BTCUSDT fiyatı: {price} USDT"
    else:
        reply_text = "BTCUSDT fiyatı alınamadı."
    message.reply_text(reply_text)
