import requests
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("cp"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].lower()
    
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url).json()
    
    crypto_id = None
    
    if isinstance(response, list):  # Response'ın liste olup olmadığını kontrol ediyoruz
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
        
        # Kripto para birimi fiyatını al
        price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
        price_response = requests.get(price_url).json()
        
        if crypto_id in price_response:
            crypto_price = price_response[crypto_id]["usd"]
            crypto_name = crypto_symbol.upper()
            message.reply_text(f"{crypto_name} anlık fiyatı: {crypto_price} USD")
        else:
            message.reply_text("Hata: Fiyat bilgisi bulunamadı!")
        
        # Kripto para birimi piyasa istatistiklerini al
        stats_url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_statistics"
        stats_response = requests.get(stats_url).json()
        
        if "market_cap" in stats_response and "volume" in stats_response:
            market_cap = stats_response["market_cap"]["usd"]
            volume = stats_response["volume"]["usd"]
            message.reply_text(f"{crypto_name} piyasa değeri: {market_cap} USD\n"
                               f"{crypto_name} 24 saatlik işlem hacmi: {volume} USD")
        else:
            message.reply_text("Hata: Piyasa istatistikleri bulunamadı!")
    else:
        message.reply_text("Hata: Kripto birimi bulunamadı!")
