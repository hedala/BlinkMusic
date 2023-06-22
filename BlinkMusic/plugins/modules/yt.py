from BlinkMusic import app
from pyrogram import filters
import youtube_dl

@app.on_message(filters.command("yt"))
def youtube_video_indir(_, message):
    # Mesaj metninden YouTube video URL'sini çıkarın
    video_url = message.text.split(" ", 1)[1]

    # YouTube videosunu MP4 formatında indirin
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'indirilenler/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_basligi = info_dict.get('title', 'video')
        video_dosyaadi = ydl.prepare_filename(info_dict)

        ydl.download([video_url])

    # İndirilen video dosyasını kullanıcıya yanıt olarak gönderin
    message.reply_document(video_dosyaadi, caption=f"İşte indirilen video: {video_basligi}")
