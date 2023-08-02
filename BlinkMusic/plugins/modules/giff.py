import httpx
import io
from pyrogram import filters

@app.on_message(filters.command("giff"))
async def search_gif_command(_, message):
    try:
        query = message.text.split(" ", 1)[1]
    except IndexError:
        await message.reply_text("Lütfen bir arama sorgusu girin.")
        return

    apikey = "AIzaSyBuGpE8dH_kR5s2yzp3yusdUiOhmaHs8_4"
    lmt = 5  # İstenen GIF sayısı
    ckey = "vercel_app"

    url = f"https://tenor.googleapis.com/v2/search?q={query}&key={apikey}&client_key={ckey}&limit={lmt}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            results = data['results']

            gif_count = 0
            for result in results:
                gif_url = result['media'][0]['gif']['url']
                response = await client.get(gif_url)
                response.raise_for_status()

                gif_data = response.content
                gif_file = io.BytesIO(gif_data)
                gif_file.name = "animation.gif"
                await app.send_document(message.chat.id, document=gif_file)
                gif_count += 1

                if gif_count >= lmt:
                    break
        except httpx.HTTPStatusError:
            await message.reply_text("GIF indirilemedi.")
        except Exception:
            await message.reply_text("Bir hata oluştu.")
        finally:
            if gif_count == 0:
                await message.reply_text("GIF bulunamadı.")
