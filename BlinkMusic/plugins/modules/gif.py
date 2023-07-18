import httpx
import io
from PIL import Image
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("gif"))
async def search_gif_command(_, message):
    query = message.text.split(" ", 1)[1]
    apikey = "AIzaSyBuGpE8dH_kR5s2yzp3yusdUiOhmaHs8_4"
    lmt = 5
    ckey = "vercel_app"

    url = f"https://tenor.googleapis.com/v2/search?q={query}&key={apikey}&client_key={ckey}&limit={lmt}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data['results']
            
            for result in results:
                gif_url = result['media_formats']['tinygif']['url']
                response = await client.get(gif_url)
                
                if response.status_code == 200:
                    gif_data = response.content
                    gif_image = Image.open(io.BytesIO(gif_data))
                    await app.send_media(message.chat.id, media=gif_image)
                    break  # Sadece ilk GIF'ı gönderdikten sonra döngüden çık
            else:
                await message.reply_text("GIF bulunamadı.")
        else:
            await message.reply_text("GIF URL'si alınamadı.")
