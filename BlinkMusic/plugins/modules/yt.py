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
        
        with tqdm(total=selected_stream.filesize, unit="B", unit_scale=True, desc="İndiriliyor") as progress_bar:
            def on_progress_callback(chunk, file_handle, bytes_remaining):
                progress_bar.update(selected_stream.filesize - bytes_remaining)
                progress_bar.set_postfix({"Progress": f"{(1 - bytes_remaining / selected_stream.filesize) * 100:.2f}%"})

            selected_stream.download(output_path=download_folder, on_progress_callback=on_progress_callback)

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
