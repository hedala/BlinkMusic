import youtube_dl
from BlinkMusic import app
from pyrogram import filters

@app.on_message(filters.command("yt"))
def download_youtube(_, message):
    url = message.text.split(" ", 1)[1]  # Get the YouTube URL from the command message
    
    # Set the options for downloading the video in the desired format
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Set the preferred format as MP4
        'outtmpl': '/path/to/save/video/%(title)s.%(ext)s',  # Set the output file name and path
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)  # Get the video information
        video_title = info_dict.get('title', None)  # Get the video title
        
        # Download the video
        ydl.download([url])
        
    if video_title:
        message.reply_text(f"Video '{video_title}' has been downloaded.")
    else:
        message.reply_text("Video has been downloaded.")
