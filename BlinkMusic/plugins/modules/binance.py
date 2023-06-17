import requests
from BlinkMusic import app
from pyrogram import filters
import locale
from datetime import datetime
import pytz

binance_api_url = "https://api.binance.com/api/v3"

@app.on_message(filters.command("coin"))
def get_crypto_price(_, message):
    crypto_symbol = message.text.split(" ", 1)[1].upper()

    # Binance API'sinden anlık fiyatı al
    price_response = get_binance_price(crypto_symbol)

    if price_response:
        crypto_price = float(price_response["price"])
        crypto_name = crypto_symbol

        # Binance API'sinden 1 saatlik ve 1 dakikalık değişim verilerini al
        hour_change_percentage = get_binance_change_percentage(crypto_symbol, interval="1h")
        minute_change_percentage = get_binance_change_percentage(crypto_symbol, interval="1m")

        # Sayıları okunaklı bir şekilde formatla
        formatted_price = locale.format_string("%.2f", crypto_price, grouping=True)

        reply_text = f"{crypto_name} anlık fiyatı: {formatted_price} USDT\n"
        reply_text += f"{crypto_name} son 1 saatlik değişim yüzdesi: {hour_change_percentage:.2f}%\n"
        reply_text += f"{crypto_name} son 1 dakikalık değişim yüzdesi: {minute_change_percentage:.2f}%\n"

        # Anlık zamanı al ve mesajın sonuna ekle (Türkiye saati)
        istanbul_tz = pytz.timezone("Europe/Istanbul")
        current_time = datetime.now(istanbul_tz).strftime("%H:%M:%S")
        reply_text += f"\n**Güncelleme Zamanı:** {current_time}"

        message.reply_text(reply_text)
    else:
        message.reply_text("Hata: Fiyat bilgisi bulunamadı!")


def get_binance_price(symbol):
    url = f"{binance_api_url}/ticker/price"
    params = {"symbol": symbol + "USDT"}

    response = requests.get(url, params=params).json()

    if "price" in response:
        return response
    else:
        # Özel sembolle tekrar deneyin
        custom_symbol = f"{symbol}USDT"
        params = {"symbol": custom_symbol}
        response = requests.get(url, params=params).json()

        if "price" in response:
            return response
        else:
            return None


def get_binance_change_percentage(symbol, interval):
    url = f"{binance_api_url}/klines"
    params = {"symbol": symbol + "USDT", "interval": interval, "limit": 2}

    response = requests.get(url, params=params).json()

    if len(response) >= 2:
        start_price = float(response[0][1])
        end_price = float(response[1][4])
        change_percentage = ((end_price - start_price) / start_price) * 100
        return change_percentage
    else:
        return 0.0


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
