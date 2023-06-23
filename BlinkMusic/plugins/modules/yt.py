from pytube import YouTube
import os
from pyrogram import filters

@app.on_message(filters.command("yt") & filters.private)
def yt(_, message):
    link = message.text.split("/yt")[1]
    bruh = message.reply("Downloading...")
    video = YouTube(link)
    video = video.streams.get_highest_resolution()

    try:
        video.download(output_path="./downloads")
    except:
        message.reply_text("Error")

    bruh.delete()
    a = message.reply_text("Uploading...")
    app.send_video(chat_id=message.chat.id, video="./downloads/" + video.default_filename)
    os.remove("./downloads/" + video.default_filename)

