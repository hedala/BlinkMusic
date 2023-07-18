import httpx
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
            gif_url = data['results'][0]['media_formats']['tinygif']['url']
            await message.reply_text(f"Here's a GIF for you: {gif_url}")
        else:
            await message.reply_text("Failed to fetch the GIF URL.")
