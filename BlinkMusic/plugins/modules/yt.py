from BlinkMusic import app
from pyrogram import filters
import os
from pytube import YouTube
from requests import get

@app.on_message(filters.command("yt"))
def youtube_download(_, message):
    url = message.text.split(" ", 1)[1]
    
    try:
        video = YouTube(url)
        video_stream = video.streams.get_highest_resolution()
        
        # Videoyu indirme
        video_stream.download()
        
        # İndirilen videoyu kaydetme
        new_filename = video_stream.default_filename
        os.rename(new_filename, f"{message.from_user.id}_{new_filename}")

        request = get(video.thumbnail_url)
        thumb_file = f"{message.from_user.id}_{new_filename}.jpg"
        with open(thumb_file, "wb") as file:
            file.write(request.content)

        message.reply_video(f"{message.from_user.id}_{new_filename}", duration=video.length, thumb=thumb_file)
        message.reply_text("Video başarıyla indirildi.")
    except Exception as e:
        message.reply_text("Video indirme hatası: " + str(e))
