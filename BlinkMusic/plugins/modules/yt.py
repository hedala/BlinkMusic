from BlinkMusic import app
from pyrogram import filters
import os
from pytube import YouTube

@app.on_message(filters.command("yts"))
def youtube_video_download(_, message):
    url = message.text.split(" ", 1)[1]

    try:
        video = YouTube(url)
        video_stream = video.streams.get_highest_resolution()
        
        # Videoyu indirme
        video_stream.download()
        
        # İndirilen videoyu kaydetme
        new_filename = f"{message.from_user.id}_{video_stream.default_filename}"
        os.rename(video_stream.default_filename, new_filename)
        
        message.reply_video(new_filename)
        message.reply_text("Video başarıyla indirildi.")
    except Exception as e:
        message.reply_text("Video indirme hatası: " + str(e))

@app.on_message(filters.command("yta"))
def youtube_audio_download(_, message):
    url = message.text.split(" ", 1)[1]

    try:
        video = YouTube(url)
        audio_stream = video.streams.filter(only_audio=True).first()
        
        # Ses parçasını indirme
        audio_stream.download()
        
        # İndirilen ses parçasını kaydetme
        new_filename = f"{message.from_user.id}_{audio_stream.default_filename.split('.')[0]}.mp3"
        os.rename(audio_stream.default_filename, new_filename)
        
        message.reply_audio(new_filename)
        message.reply_text("Ses parçası başarıyla indirildi.")
    except Exception as e:
        message.reply_text("Ses parçası indirme hatası: " + str(e))
