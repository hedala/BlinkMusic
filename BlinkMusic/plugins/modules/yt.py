from BlinkMusic import app
from pyrogram import filters
import os
from pytube import YouTube

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
        
        message.reply_text("Video başarıyla indirildi.")
    except Exception as e:
        message.reply_text("Video indirme hatası: " + str(e))
