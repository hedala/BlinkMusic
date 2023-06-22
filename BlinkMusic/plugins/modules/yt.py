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
        
        # Formatları filtreleyin ve kullanıcıya mevcut formatları göstermek için bir liste oluşturun
        available_streams = video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()
        format_list = "\n".join([f"{i}. {stream.resolution}" for i, stream in enumerate(available_streams, start=1)])
        
        message.reply_text(f"Mevcut formatlar:\n{format_list}\n\nLütfen indirmek istediğiniz format numarasını seçin.")
        
        # Kullanıcının seçtiği formatı alın
        user_choice = int(message.text.split(" ", 2)[2])
        selected_stream = available_streams[user_choice - 1]
        
        # İlerleme çubuğunu başlatın
        progress_bar = tqdm(total=selected_stream.filesize, unit="B", unit_scale=True)
        
        # İndirme işlemi sırasında çağrılacak ilerleme geri çağırım fonksiyonu
        def progress_callback(chunk, file_handle, bytes_remaining):
            progress_bar.update(len(chunk))
        
        # Videoyu indirme
        selected_stream.download(output_path="downloads", on_progress_callback=progress_callback)
        
        # İndirilen videoyu kaydetme
        new_filename = selected_stream.default_filename
        user_filename = f"{message.from_user.id}_{new_filename}"
        os.rename(f"downloads/{new_filename}", f"downloads/{user_filename}")

        request = get(video.thumbnail_url)
        thumb_file = f"downloads/{message.from_user.id}_{new_filename}.jpg"
        with open(thumb_file, "wb") as file:
            file.write(request.content)

        message.reply_video(user_filename, duration=video.length, thumb=thumb_file)
        message.reply_text("Video başarıyla indirildi.")
        
        # İndirme tamamlandığında ilerleme çubuğunu kapatın
        progress_bar.close()
    except Exception as e:
        message.reply_text("Video indirme hatası: " + str(e))
