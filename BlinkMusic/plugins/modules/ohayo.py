import requests
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("hel"))
def show_coin_price(_, message):
    symbol = message.text.upper().split()[1] 
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200:
        data = response.json()
        message.reply_text(f"{data['symbol']} fiyatı: {data['price']}")
    else:
        message.reply_text(f"{symbol} sembolü bulunamadı.")
