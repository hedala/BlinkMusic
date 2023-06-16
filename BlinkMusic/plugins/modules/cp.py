import requests
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("cp"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].lower()
    
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url).json()
    
    crypto_id = None
    
    if isinstance(response, list):
        for crypto in response:
            if crypto.get("symbol") == crypto_symbol:
                crypto_id = crypto["id"]
                break
    else:
        message.reply_text("Hata: Geçersiz API yanıtı!")
        return
    
    if crypto_id:
        if crypto_id.startswith("binance-peg-"):
            crypto_id = crypto_id.replace("binance-peg-", "")
        
        price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
        stats_url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}"
        
        price_response = requests.get(price_url).json()
        stats_response = requests.get(stats_url).json()
        
        if crypto_id in price_response:
            crypto_price = price_response[crypto_id]["usd"]
            crypto_name = crypto_symbol.upper()
            
            market_cap = stats_response.get("market_data", {}).get("market_cap", {}).get("usd")
            volume = stats_response.get("market_data", {}).get("total_volume", {}).get("usd")
            
            reply_text = f"{crypto_name} anlık fiyatı: {crypto_price} USD\n"
            if market_cap:
                reply_text += f"{crypto_name} piyasa değeri: {market_cap} USD\n"
            if volume:
                reply_text += f"{crypto_name} 24 saatlik işlem hacmi: {volume} USD"
            
            message.reply_text(reply_text)
        else:
            message.reply_text("Hata: Fiyat bilgisi bulunamadı!")
    else:
        message.reply_text("Hata: Kripto birimi bulunamadı!")
