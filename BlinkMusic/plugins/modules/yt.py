from BlinkMusic import app
from pyrogram import filters
import os
from pytube import YouTube
from requests import get
from tqdm import tqdm

@app.on_message(filters.command("yt"))
def youtube_download(_, message):
    url = message.text.split(" ", 1)[1]
    
    try:
        video = YouTube(url)
        available_streams = video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()

        # Kullanıcıya mevcut formatları göstermek için available_streams'ı kullanabilirsiniz
        
        selected_stream = available_streams.first()  # Kullanıcının seçtiği formatı alabilirsiniz

        download_folder = "downloads"  # İndirilen videoların kaydedileceği klasör
        
        video.register_on_progress_callback(lambda stream, chunk, bytes_remaining: progress_callback(chunk, bytes_remaining))

        def progress_callback(chunk, bytes_remaining):
            file_size = selected_stream.filesize
            bytes_downloaded = file_size - bytes_remaining
            progress = bytes_downloaded / file_size * 100
            progress_bar.update(bytes_downloaded - progress_bar.n)

        with tqdm(total=selected_stream.filesize, unit="B", unit_scale=True, desc="İndiriliyor") as progress_bar:
            selected_stream.download(output_path=download_folder)

        new_filename = selected_stream.default_filename
        os.rename(os.path.join(download_folder, new_filename), os.path.join(download_folder, f"{message.from_user.id}_{new_filename}"))

        request = get(video.thumbnail_url)
        thumb_file = os.path.join(download_folder, f"{message.from_user.id}_{new_filename}.jpg")
        with open(thumb_file, "wb") as file:
            file.write(request.content)

        message.reply_video(os.path.join(download_folder, f"{message.from_user.id}_{new_filename}"), duration=video.length, thumb=thumb_file)
        message.reply_text("Video başarıyla indirildi.")
    except Exception as e:
        message.reply_text("Video indirme hatası: " + str(e))
