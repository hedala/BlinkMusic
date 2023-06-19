import requests
from BlinkMusic import app
from pyrogram import filters

binance_api_url = "https://api3.binance.com/api/v3/ticker/price"


@app.on_message(filters.command("fiyat"))
def get_crypto_price(_, message):
    try:
        response = requests.get(binance_api_url)
        response_json = response.json()
        btc_price = next(item for item in response_json if item["symbol"] == "BTCUSDT")["price"]
        eth_price = next(item for item in response_json if item["symbol"] == "ETHUSDT")["price"]
        
        message.reply_text(
            f"BTC fiyatı: {btc_price}\nETH fiyatı: {eth_price}"
        )
    except Exception as e:
        message.reply_text("Kripto fiyatlarını alırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        print(f"Hata: {str(e)}")
