import requests
from BlinkMusic import app
from pyrogram import filters
import locale
from datetime import datetime
import pytz

@app.on_message(filters.command("coin"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].lower()

    url = f"https://api3.binance.com/api/v3/ticker/price?symbol={crypto_symbol.upper()}USDT"
    response = requests.get(url).json()

    if "symbol" in response and "price" in response:
        crypto_price = response["price"]
        crypto_name = crypto_symbol.upper()

        # Anlık zamanı al ve mesajın sonuna ekle (Türkiye saati)
        istanbul_tz = pytz.timezone("Europe/Istanbul")
        current_time = datetime.now(istanbul_tz).strftime("%Y-%m-%d %H:%M:%S")

        reply_text = f"{crypto_name} anlık fiyatı: {crypto_price} USDT\n\nGüncelleme Zamanı: {current_time}"
        message.reply_text(reply_text)
    else:
        message.reply_text("Hata: Fiyat bilgisi bulunamadı!")


@app.on_message(filters.command("stats"))
def get_crypto_stats(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].lower()

    url = f"https://api.coingecko.com/api/v3/coins/{crypto_symbol}"
    response = requests.get(url).json()

    if "market_data" in response and "market_cap" in response["market_data"] and "total_volume" in response["market_data"]:
        market_cap = response["market_data"]["market_cap"]["usd"]
        volume = response["market_data"]["total_volume"]["usd"]

        # Sayıları okunaklı bir şekilde formatla
        formatted_market_cap = format_large_number(market_cap) if market_cap else None
        formatted_volume = format_large_number(volume) if volume else None

        reply_text = f"{crypto_symbol.upper()} piyasa değeri: {formatted_market_cap} USD\n" if formatted_market_cap else ""
        reply_text += f"{crypto_symbol.upper()} 24 saatlik işlem hacmi: {formatted_volume} USD" if formatted_volume else ""

        message.reply_text(reply_text)
    else:
        message.reply_text("Hata: Piyasa istatistikleri bulunamadı!")


def format_large_number(number):
    if number is None:
        return None

    if abs(number) >= 1_000_000_000:
        formatted_number = f"{number / 1_000_000_000:.2f}B"
    elif abs(number) >= 1_000_000:
        formatted_number = f"{number / 1_000_000:.2f}M"
    else:
        formatted_number = f"{number:,.2f}"

    return formatted_number
