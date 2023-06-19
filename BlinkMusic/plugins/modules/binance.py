from BlinkMusic import app
from pyrogram import filters
import requests

def get_crypto_price(symbol):
       url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
       response = requests.get(url)
       data = response.json()
       try:
           price = float(data["price"])
           return price
       except KeyError:
           # Handle the case where the 'price' key is not present in the response
           return None

@app.on_message(filters.command("coin"))
def coin(_, message):
    symbol = message.text.split(" ")[1]
    price = get_crypto_price(symbol)
    reply_text = f"{symbol.upper()} fiyatı: {price} USDT"
    message.reply_text(reply_text)
