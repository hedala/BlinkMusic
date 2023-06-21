from BlinkMusic import app
from pyrogram import filters
import youtube_dl


def download_media(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        ydl.download([url])
        filename = ydl.prepare_filename(info)
        return filename


@app.on_message(filters.text & filters.entity("url"))
def download_media_from_url(_, message):
    url = message.text[message.entities[0].offset:message.entities[0].offset+message.entities[0].length]
    filename = download_media(url)
    text = f"İndirilen medyanın dosya adı: {filename}"
    message.reply_text(text)
￼Enter
