import requests
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("cp"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].lower()
    
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url).json()
    
    crypto_id = None
    
    for crypto in response:
        if crypto.get("symbol") == crypto_symbol:
            crypto_id = crypto["id"]
            break
    
    if crypto_id:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
        response = requests.get(url).json()
        
        if crypto_id in response:
            crypto_price = response[crypto_id]["usd"]
            message.reply_text(f"{crypto_id.upper()} anlık fiyatı: {crypto_price} USD")
        else:
            message.reply_text("Hata: Fiyat bilgisi bulunamadı!")
    else:
        message.reply_text("Hata: Kripto birimi bulunamadı!")
