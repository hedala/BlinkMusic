from BlinkMusic import app
from pyrogram import filters
import requests

def get_crypto_stats(symbol):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}USDT"
    response = requests.get(url)
    data = response.json()
    try:
        stats = {
            "symbol": data["symbol"],
            "price_change": float(data["priceChange"]),
            "price_change_percent": float(data["priceChangePercent"]),
            "high_price": float(data["highPrice"]),
            "low_price": float(data["lowPrice"]),
            "volume": float(data["volume"]),
            "quote_volume": float(data["quoteVolume"])
        }
        return stats
    except KeyError:
        return None

@app.on_message(filters.command("coin"))
def coin(_, message):
    symbol = message.text.split(" ")[1]
    stats = get_crypto_stats(symbol)
    if stats is not None:
        reply_text = f"""
        {stats['symbol'].upper()} fiyat istatistikleri:
        Değişim: {stats['price_change']} USDT
        Değişim Yüzdesi: {stats['price_change_percent']}%
        En Yüksek Fiyat: {stats['high_price']} USDT
        En Düşük Fiyat: {stats['low_price']} USDT
        Hacim: {stats['volume']}
        Alıntı Hacmi: {stats['quote_volume']}
        """
    else:
        reply_text = f"{symbol.upper()} fiyat istatistikleri alınamadı."
    message.reply_text(reply_text)
