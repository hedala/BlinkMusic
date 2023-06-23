from BlinkMusic import app
from pyrogram import filters
import httpx

@app.on_message(filters.command("gif"))
async def search_gif(_, message):
    query = " ".join(message.command[1:])  # Alınan komut argümanlarını birleştirerek sorgu oluşturuyoruz
    
    apikey = "AIzaSyBuGpE8dH_kR5s2yzp3yusdUiOhmaHs8_4"
    lmt = 10
    ckey = "vercel_app"

    url = f"https://tenor.googleapis.com/v2/search?q={query}&key={apikey}&client_key={ckey}&limit={lmt}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'results' in data and len(data['results']) > 0:
                media_group = []
                for result in data['results']:
                    gif_url = result['media_formats']['tinygif']['url']
                    media_group.append(InputMediaVideo(gif_url))
                await message.reply_media_group(media_group)
            else:
                await message.reply_text("GIF bulunamadı.")
        else:
            await message.reply_text("GIF URL'si alınamadı."
                                     
