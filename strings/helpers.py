HELP_1 = """🙄**<u>admin komutları:</u>**

Sadece komutların başına "c" ekleyin, kanalda kullanmak için.

/duraklat : Şu an oynatılan yayını durdurur.
/devam : Duraklatılmış yayını devam ettirir.
/sessiz : Şu an oynatılan yayını sessize alır.
/sesac : Sessize alınmış yayını seslendirir.
/atla : Şu an oynatılan yayını atlar ve sıradaki parçayı başlatır.
/end veya /durdur : Sırayı temizler ve mevcut yayını sonlandırır.
/karistir : Sıradaki parçaları karıştırır.
/ileri : Yayını belirtilen süreye atlar.
/gerisar : Yayını belirtilen süre kadar geriye alır.
/reboot : Sohbetiniz için botu yeniden başlatır.

🥴<u>**oynatılan parçanın tekrarlanması :**</u>

/tekrarla [devre dışı bırak/etkinleştir] veya [1:10 arasında]
    : Etkinleştirildiğinde, bot mevcut oynatılan akışı döngüye alır ve 10 kez veya istenilen döngü sayısı kadar tekrar çalar.

😜<u>**Yetkili Kullanıcılar :**</u>

Yetkili Kullanıcılar (Auth Users), chat içinde admin hakları olmadan bot üzerinde admin yetkilerini kullanabilirler.

/auth [kullanıcı_adı]: Bir kullanıcıyı botun yetkili kullanıcılar listesine ekler.
/unauth [kullanıcı_adı]: Yetkili kullanıcılar listesinden bir kullanıcıyı kaldırır.
/authusers: Yetkili kullanıcılar listesini gösterir.
"""

HELP_2 = """💞<u>**oynatma komutları:**</u>

Mevcut komutlar: oynat, voynat, coynat: Şarkı çalma komutları.

Zorla oynatma komutları:playforce, vplayforce, cplayforce: Şarkıyı zorla oynatma komutları.

**c**: Kanal oynatma anlamına gelir.
**v**: Video oynatma anlamına gelir.
**force**: Zorla oynatma anlamına gelir.

/oynat veya /voynat veya /coynat: İstenilen parçayı video sohbette yayınlamaya başlar.

/playforce veya /vplayforce veya /cplayforce: Zorla oynat mevcut yayını durdurur ve istenilen parçayı yayınlamaya başlar.

/channelplay [sohbet kullanıcı adı veya kimlik] veya [devre dışı bırak]: Bir kanalı bir gruba bağlar ve komutlar yardımıyla grupta parçaları yayınlamaya başlar.


🤨**<u>Sunucu Çalma Listeleri:</u>**

/playlist : Sunuculardaki kayıtlı çalma listenizi kontrol edin.
/deleteplaylist : Çalma listenizdeki herhangi bir kaydedilmiş parçayı silin.
/play : Sunucudaki kayıtlı çalma listenizden çalmaya başlar.
"""

HELP_3 = """😉<u>BOT KOMUTLARI:</u>

/stats : En iyi 10 parça global istatistiklerini, botun en iyi 10 kullanıcısını, bot üzerindeki en iyi 10 sohbeti, sohbet içinde en çok çalınan 10 parçayı ve daha fazlasını alır.
/sudolist : Müzik botunun süper kullanıcı listesini gösterir.
/lyrics [parça adı] : İstenen parçanın sözlerini arar.
/song [parça adı] veya [yt bağlantısı] : Herhangi bir YouTube parçasını ses veya video formatında indirir.
/player : Etkileşimli bir oynatıcı paneli alır.
/sıra : Kuyrukta bekleyen parçaların listesini gösterir.
Powered by @esilabotbilgilendirme, @sorundestekk @sohbet_siir."""

HELP_4 = """😴<u>**Ekstra Komutlar:**</u>

/start : Müzik botunu başlatır.
/help : Komutların açıklamalarıyla birlikte yardım menüsünü al.
/ping : Botun ping değerini ve sistem istatistiklerini gösterir.

🧐<u>**Grup Ayarları:**</u>
/settings : Grubun ayarlarını etkileşimli çevrimiçi menü ile gösterir.
"""

HELP_5 = """<u>ᴀᴅᴅ & ʀᴇᴍᴏᴠᴇ sᴜᴅᴏᴇʀs:</u>**
/addsudo [kullanıcı adı veya bir kullanıcıya yanıt ver]
/delsudo [kullanıcı adı veya bir kullanıcıya yanıt ver]

🥶**<u>HEROKU:</u>**
/usage : Kullanım verilerini gösterir.

🤯**<u>Konfigürasyon Değişkenleri:</u>**
/get_var: Heroku veya .env'den bir konfigürasyon değişkenini alır.
/del_var: Heroku veya .env'den bir konfigürasyon değişkenini siler.
/set_var [var adı] [değer]: Heroku veya .env'de bir konfigürasyon değişkenini ayarlar veya günceller.

🤖**<u>Bot Komutları:</u>**
/restart: Botunuzu yeniden başlatır.
/update: Botu, akış deposundan günceller.
/speedtest: Botun sunucu hızını kontrol eder.
/maintenance [enable/disable]
/logger [enable/disable]: Bot, gerçekleşen aktiviteleri kaydetmeye başlar.
/get_log [satır sayısı]: Botunuzun günlüklerini alır (varsayılan değer 100 satırdır).
/autoend [enable|disable]: Eğer kimse dinlemiyorsa akışı otomatik olarak sona erdirir.

🤑**<u>İstatistik Komutları:</u>**
/activevoice: Bot üzerindeki aktif sesli sohbetlerin listesini gösterir.
/activevideo: Bot üzerindeki aktif video sohbetlerin listesini gösterir.
/stats: Botun mevcut istatistiklerini gösterir.

😒**<u>Karartılmış Sohbet:</u>**
/blacklistchat [sohbet ID]: Bir sohbeti botu kullanmaktan yasaklar.
/whitelistchat [sohbet ID]: Yasaklı sohbeti beyaz listeye ekler.
/blacklistedchat: Yasaklı sohbetlerin listesini gösterir.

😤**<u>Kullanıcıları Engelle:</u>**
/block [kullanıcı adı veya bir kullanıcıya yanıt]: Kullanıcıyı görmezden gelmeye başlar, böylece bot komutlarını kullanamaz.
/unblock [kullanıcı adı veya bir kullanıcıya yanıt]: Engellenen kullanıcıyı engelden çıkarır.
/blockedusers: Engellenen kullanıcıların listesini gösterir.

🤬**<u>Global Ban Özelliği:</u>**
/gban [kullanıcı adı veya bir kullanıcıya yanıt]: Kullanıcıyı tüm sunuculardan global olarak yasaklar ve botu kullanmasını engeller.
/ungban [kullanıcı adı veya bir kullanıcıya yanıt]: Global olarak yasaklanan kullanıcıyı yasaktan çıkarır.
/gbannedusers: Global olarak yasaklanmış kullanıcıların listesini gösterir.

🎥**<u>Video Sohbet Modu:</u>**
/set_video_limit [sohbet sayısı]: Bot üzerinde izin verilen maksimum video sohbet sayısını ayarlar. [Varsayılan - 3]
/videomode [indir|m3u8]: Eğer indirme modu etkinleştirilirse, bot parçaları oynatmak yerine indirecektir.

💔**<u>Özel Bot:</u>**
/authorize [sohbet ID'si]: Bir sohbetin botu kullanmasına izin verir.
/unauthorize [sohbet ID'si]: İzin verilen sohbeti devre dışı bırakır.
/authorized: Tüm izin verilen sohbetlerin listesini gösterir.

🍒**<u>Yayın Özelliği:</u>**
/broadcast [mesaj veya bir mesaja yanıt]: Bir mesajı botun hizmet verdiği sohbetlere yayınlar.

<u>Yayın Modları:</u>
**-pin** : Yayınladığınız mesajları hizmet verilen sohbetlerde sabitler.
**-pinloud** : Yayınladığınız mesajı hizmet verilen sohbetlerde sabitler ve üyelere bildirim gönderir.
**-user** : Mesajı botunuzu başlatan kullanıcılara yayınlar.
**-assistant** : Mesajınızı botun asistan hesabından yayınlar.
**-nobot** : Botun mesajı yayınlamasını zorla engeller.

**Örnek**: `/broadcast -user -assistant -pin Yayın Testi`
"""

HELP_7 = """💌**<u>Burada yeni özellikleri bulabilirsiniz:</u>**

/alive : Şimdi Alexa Müzik Botu'nun çalışıp çalışmadığını kontrol edebilirsiniz.
/id : Kullanıcı ve sohbet ID'sini kontrol etmek için.
/gcast -user -assistant -pin Yayın Testi
/verify : Alexa veritabanında kendinizi doğrulayın.
Powered © by """

HELP_8 = """💰**<u>  ✶ Etiket Komutları:</u>**

» /tag - Tek tek etiketler.

» /utag - Çoklu etiketler.

örnek /utag selam veya /tag selam