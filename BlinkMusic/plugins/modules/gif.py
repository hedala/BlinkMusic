from BlinkMusic import app
from pyrogram import filters
from pyrogram.types import InputMediaVideo
import httpx

@app.on_message(filters.command("gif"))
async def search_gif(_, message):
    query = " ".join(message.command[1:])  # Alınan komut argümanlarını birleştirerek sorgu oluşturuyoruz
    
    apikey = "YOUR_API_KEY"
    lmt = 10
    ckey = "YOUR_CLIENT_KEY"

    url = f"https://tenor.googleapis.com/v2/search?q={query}&key={apikey}&client_key={ckey}&limit={lmt}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                media_group = []
                for result in data['results']:
                    if 'media' in result and len(result['media']) > 0:
                        gif_formats = result['media'][0]['gif']['url']
                        media_group.append(InputMediaVideo(gif_url))
                if media_group:
                    await message.reply_media_group(media_group)
                else:
                    await message.reply_text("GIF bulunamadı.")
            else:
                await message.reply_text("GIF bulunamadı.")
        else:
            await message.reply_text("GIF URL'si alınamadı.")
