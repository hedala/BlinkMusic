from BlinkMusic import app
from pyrogram import filters
import requests

@app.on_message(filters.command("coin"))
def coin_command(_, message):
    symbol = "BTCUSDT"  # Örnek olarak BTCUSDT sembolünü kullanıyoruz, dilediğiniz sembolü burada belirtebilirsiniz
    interval = "1d"  # Örnek olarak 1 günlük (1d) veri alıyoruz, dilediğiniz aralığı burada belirtebilirsiniz
    
    # Anlık fiyatı çekmek için API'yi kullanıyoruz
    price_url = f"https://api3.binance.com/api/v3/ticker/price?symbol={symbol}"
    price_response = requests.get(price_url)
    price_data = price_response.json()
    current_price = float(price_data.get("price", 0))
    
    # Fiyat değişimini çekmek için API'yi kullanıyoruz
    klines_url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
    klines_response = requests.get(klines_url)
    klines_data = klines_response.json()
    
    if isinstance(klines_data, list) and len(klines_data) > 0:
        price_change = float(klines_data[-1][4]) - float(klines_data[0][4])
    else:
        price_change = 0
    
    message.reply_text(
        f"**{symbol} Coin Bilgileri**\n"
        f"Anlık Fiyat: {price}\n"
        f"Fiyat Değişimi: {price_change}"
    )
