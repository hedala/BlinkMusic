import requests
from BlinkMusic import app
from pyrogram import filters


@app.on_message(filters.command("price"))
def get_price(_, message):
    symbol = message.text.split()[1].upper()
    url = f"https://api3.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'price' in data:
            price = data['price']
            message.reply_text(f"{symbol} fiyatı: {price}")
            return
    message.reply_text(f"{symbol} fiyatı bulunamadı.")


