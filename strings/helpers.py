HELP_1 = """<u>Admin komutları:</u>

/pause: Şu anda çalınan yayını duraklatır.
/resume: Duraklatılan yayını devam ettirir.
/mute: Şu anda çalınan yayının sesini kapatır.
/unmute: Kapatılan sesi açar.
/skip: Şu anda çalınan yayını atlar ve sıradaki şarkıya geçer.
/end veya /stop: Çalınan yayını sonlandırır.
/shuffle: Sıradaki şarkıları karıştırır.
/seek: Yayını belirtilen süreye ilerletir.
/seekback: Yayını belirtilen süre kadar geri sarar.
/reboot: Sohbetinizdeki botu yeniden başlatır.

<u>Döngü (Loop):</u>

/loop [enable/disable] veya [Sayı 1:10]:

<u>Yetkili Kullanıcılar:</u>

Yetkili kullanıcılar, sohbette yönetici haklarına sahip olmadan botu yönetici haklarıyla kullanabilir.

/auth [kullanıcı adı]: Bir kullanıcıyı botun yetkililer listesine ekler.
/unauth [kullanıcı adı]: Bir kullanıcıyı yetkililer listesinden çıkarır.
/authusers: Yetkili kullanıcılar listesini gösterir."""


HELP_2 = """<u>Oynatma Komutları:</u>

Mevcut komutlar = play, vplay, cplay

Zorla Oynatma Komutları = playforce, vplayforce, cplayforce

c, kanal oynatma anlamına gelir.
v, video oynatma anlamına gelir.
force, zorla oynatma anlamına gelir.

/play veya /vplay veya /cplay: İstenen parçayı video sohbetinde yayınlamaya başlar.

/playforce veya /vplayforce veya /cplayforce: Zorla Oynatma mevcut yayını durdurur ve istenen parçayı yayınlamaya başlar.

/channelplay [sohbet kullanıcı adı veya ID] veya [devre dışı]: Kanalı bir gruba bağlar ve komutlar aracılığıyla parçaları yayınlamaya başlar.

**<u>Oynatma Listeleri:</u>**

/playlist: Kaydedilmiş oynatma listelerinizi sunucularda kontrol eder.
/deleteplaylist: Kaydedilmiş oynatma listesindeki herhangi bir parçayı siler.
/play: Kaydedilmiş oynatma listenizden sunucuda çalmaya başlar."""


HELP_3 = """<u>Bot Komutları:</u>

/stats: En iyi 10 parça global istatistiklerini, botun en iyi 10 kullanıcısını, bot üzerindeki en iyi 10 sohbeti, sohbette çalınan en iyi 10 parçayı ve çok daha fazlasını alın...

/sudolist: Müzik botunun sudolu kullanıcılarını gösterir.

/lyrics [şarkı adı]: İstenen şarkının sözlerini arar.

/song [şarkı adı] veya [yt linki]: Herhangi bir YouTube parçasını sesli veya video formatında indirin.

/player: İnteraktif bir oynatıcı paneli alın.

/queue: Sıraya alınan parçaları listeler."""


HELP_4 = """<u>**ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs:**</u>

/start : sᴛᴀʀᴛs ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ.
/help  : ɢᴇᴛ ʜᴇʟᴩ ᴍᴇɴᴜ ᴡɪᴛʜ ᴇxᴩʟᴀɴᴀᴛɪᴏɴ ᴏғ ᴄᴏᴍᴍᴀɴᴅs.
.ping: sʜᴏᴡ ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

<u>**ɢʀᴏᴜᴩ sᴇᴛᴛɪɴɢs:**</u>
/settings : sʜᴏᴡs ᴛʜᴇ ɢʀᴏᴜᴩ sᴇᴛᴛɪɴɢs ᴡɪᴛʜ ᴀɴ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ɪɴʟɪɴᴇ ᴍᴇɴᴜ.""

HELP_5 = """**<u>Yetkili Ekleme ve Kaldırma:</u>**
/addsudo [kullanıcı adı veya kullanıcıya yanıt olarak]
/delsudo [kullanıcı adı veya kullanıcıya yanıt olarak]

**<u>Heroku:</u>**
/usage: Ayın dyno kullanımını gösterir.

**<u>Konfigürasyon Değişkenleri:</u>**
/get_var: Heroku'dan veya .env dosyasından bir konfigürasyon değişkeni alır.
/del_var: Heroku'dan veya .env dosyasından bir konfigürasyon değişkenini siler.
/set_var [değişken adı] [değer]: Heroku'da veya .env dosyasında bir konfigürasyon değişkeni ayarlar veya günceller.

**<u>Bot Komutları:</u>**
/restart: Botu yeniden başlatır.
/update: Botu günceller.
/speedtest: Botun sunucu hızını kontrol eder.
/maintenance [etkinleştir/devre dışı bırak]: Bot bakım modunu açar veya kapatır.
/logger [etkinleştir/devre dışı bırak]: Botun etkinlikleri kaydetmeye başlamasını sağlar.
/get_log [satır sayısı]: Botun kayıtlarını alır. [varsayılan değer 100 satır]
/autoend [etkinleştir/devre dışı bırak]: Eğer dinleyen yoksa yayını otomatik olarak sonlandırır.

**<u>İstatistik Komutları:</u>**
/activevoice: Bot üzerindeki etkin sesli sohbetleri gösterir.
/activevideo: Bot üzerindeki etkin video sohbetleri gösterir.
/stats: Botun mevcut istatistiklerini gösterir.

**<u>Kara Liste Sohbet:</u>**
/blacklistchat [sohbet kimliği]: Botun kullanılmasını engellemek için bir sohbeti kara listeye alır.
/whitelistchat [sohbet kimliği]: Kara listelenen bir sohbeti beyaz listeye alır.
/blacklistedchat: Kara listelenen sohbetlerin listesini gösterir.

**<u>Kullanıcı Engelleme:</u>**
/block [kullanıcı adı veya kullanıcıya yanıt olarak]: Bot komutlarını kullanmasını engellemek için bir kullanıcıyı engeller.
/unblock [kullanıcı adı veya kullanıcıya yanıt olarak]: Engellenen bir kullanıcının engellemesini kaldırır.
/blockedusers: Engellenen kullanıcıların listesini gösterir.

**<u>GBAN ÖZELLİĞİ:</u>**
/gban [kullanıcı adı veya bir kişiye yanıt ver] : Bu komut, kullanıcıyı tüm sunucu sohbetlerinden yasaklar ve onun botu kullanmasını engeller.
/ungban [kullanıcı adı veya bir kişiye yanıt ver] : Bu komut, global olarak yasaklanmış bir kullanıcının yasağını kaldırır.
/gbannedusers : Global olarak yasaklanmış kullanıcıların listesini gösterir.

**<u>Video Sohbet Modu:</u>**
/set_video_limit [sohbetlerin sayısı] : Bu komut, bot üzerinde izin verilen maksimum video sohbet sayısını ayarlar. [Varsayılan - 3]
/videomode [download|m3u8] : Eğer indirme modu etkinleştirilmişse, bot parçaları çalmak yerine indirir.

**<u>Özel Bot:</u>**
/authorize [sohbet kimliği] : Bu komut, botun kullanımına izin vermek için bir sohbeti yetkilendirir.
/unauthorize [sohbet kimliği] : Bu komut, yetkilendirilmiş bir sohbetin iznini kaldırır.
/authorized : İzin verilen sohbetlerin listesini gösterir.

**<u>Yayın Özelliği:</u>**
/broadcast [mesaj veya bir mesaja yanıt ver] : Bu komut, yayınlanacak bir mesajı sunucu sohbetlerine gönderir.

Yayın modları:
-pin : Yayınlanan mesajları sunucu sohbetlerinde sabitler.
-pinloud : Yayınlanan mesajı sunucu sohbetlerinde sabitler ve üyelere bildirim gönderir.
-user : Mesajı botunuzu başlatan kullanıcılara yayınlar.
-assistant : Mesajınızı botun asistan hesabından yayınlar.
-nobot : Botun mesajı yayınlamasını engeller.

Örnek: `/broadcast -user -assistant -pin Yayın testi`"""

💌**<u>Özellikler:</u>**

/alive : Artık BlinkMusic müzik botunun çalışıp çalışmadığını kontrol edebilirsiniz.
/id : Kullanıcı ve sohbet kimliğini kontrol etmek için.
/gcast -user -assistant -pin Yayın testi`
"""
