# ByteDance Seedance 2.0 Referanstan Videoya

## Girdiler

Bir `model` seçmek, aşağıdaki parametrelerden hangilerinin kullanılabilir olduğunu belirler. `video_editing` ve `output_format` yalnızca Seedance 2.5 seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan AI modeli. Seedance 2.5, 30 saniyeye kadar videolar ve mp4/mov çıktısı sunan en yeni modeldir; Seedance 2.0 maksimum kalite ve 1080p/4k içindir; Fast hız optimizasyonu içindir; Mini en hızlı ve en düşük maliyetli üretim içindir. Bir model seçmek, aşağıda listelenen modele özgü girdileri ortaya çıkarır. | COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |
| `prompt` | Video oluşturma için metin promptu. Seedance 2.5 için, oluşturulan diyaloğu yönlendirmek üzere sözlü satırları çift tırnak içinde yazın. En az bir boşluk dışı karakter içermelidir. | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Seedance 2.5, 2.0 Fast ve 2.0 Mini 480p ve 720p sunar; Seedance 2.0 ayrıca 1080p ve 4k sunar (Seedance 2.5 varsayılanı: 720p). | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı (Seedance 2.5 varsayılanı: `"16:9"`; Seedance 2.0 modelleri varsayılanı: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (Seedance 2.5: 4-30, varsayılan 5; Seedance 2.0 modelleri: 4-15, varsayılan 7). | INT | Evet | 4 ile 30 (Seedance 2.5)<br>4 ile 15 (Seedance 2.0)<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirin (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `video_editing` | Yalnızca Seedance 2.5. Bağlı bir referans videosunu düzenleyen bir prompt kullanıldığında etkinleştirin; örneğin, içindeki bir nesneyi değiştirme. Bu durumda çıktı, kaynak klibin kendi uzunluğunu ve en-boy oranını korur; duration ve ratio alanları yok sayılır. Yeni bir video oluşturmak veya bir videoyu belirlediğiniz süreye kadar uzatmak için devre dışı bırakın (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |
| `output_format` | Yalnızca Seedance 2.5. Çıktı videosunun kapsayıcı formatı (varsayılan: `"mp4"`). | COMBO | Evet | `"mp4"` |
| `reference_images` | Video oluşturmayı yönlendiren referans görüntüler. Görüntüler, maksimum kenarı 6000 piksel olacak şekilde otomatik olarak küçültülür ve en-boy oranı 0,4 ile 2,5 arasında olacak şekilde en az 300x300 piksel olmalıdır. | IMAGE | Hayır | 30 adede kadar (Seedance 2.5)<br>9 adede kadar (Seedance 2.0) |
| `reference_videos` | Video oluşturmayı yönlendiren referans videolar; video düzenleme ve uzatma için kullanılır. | VIDEO | Hayır | 10 adede kadar (Seedance 2.5)<br>3 adede kadar (Seedance 2.0) |
| `reference_audios` | Video oluşturmayı yönlendiren referans ses klipleri. | AUDIO | Hayır | 10 adede kadar (Seedance 2.5)<br>3 adede kadar (Seedance 2.0) |
| `auto_downscale` | Seçilen çözünürlük için modelin piksel bütçesini aşan referans videolarını otomatik olarak küçültür. En-boy oranı korunur; sınırlar içindeki videolara dokunulmaz (varsayılan: True). | BOOLEAN | Hayır | `True`<br>`False` |
| `auto_upscale` | Seçilen çözünürlük için modelin minimum piksel sayısının altındaki referans videolarını otomatik olarak büyütür. En-boy oranı korunur; minimumu zaten karşılayan videolara dokunulmaz. Not: düşük çözünürlüklü bir kaynağı büyütmek gerçek detay eklemez ve daha düşük kaliteli çıktılar üretebilir (varsayılan: False). | BOOLEAN | Hayır | `True`<br>`False` |
| `reference_assets` | Referans olarak kullanılacak daha önce oluşturulmuş Seedance sanal kütüphane varlıklarının (Görüntü, Video veya Ses) kimlikleri. Her varlık mevcut olmalı ve Aktif durumda olmalıdır. Promptta varlıklara asset1, asset 2, vb. şeklinde atıfta bulunulabilir; düğüm bu belirteçleri Image 2 gibi etiketlerle değiştirir. | STRING | Hayır | 30 adede kadar (Seedance 2.5)<br>9 adede kadar (Seedance 2.0) |

**Önemli Kısıtlamalar:**

* En az bir referans gereklidir. Seedance 2.0, 2.0 Fast ve 2.0 Mini için en az bir görüntü veya video referansı sağlamanız gerekir (`reference_images`, `reference_videos` veya bir görüntü/video `reference_assets` girdisi aracılığıyla). Seedance 2.5 ayrıca yalnızca ses içeren referansları da kabul eder.
* Referans sayıları modele bağlıdır: Seedance 2.5, 30 adede kadar `reference_images`, 10 `reference_videos`, 10 `reference_audios` ve 30 `reference_assets` sağlar; Seedance 2.0 modelleri 9 adede kadar görüntü, 3 video, 3 ses klibi ve 9 varlık sağlar. Toplamlar, doğrudan girdiler ve varlık referansları birleştirilerek sayılır ve oluşturma öncesinde doğrulanır.
* Her referans videosu en az 1,8 saniye uzunluğunda olmalı ve her referans ses klibi en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans videolarının ve tüm referans seslerinin toplam süresi, seçilen modelin sınırı içinde kalmalıdır (Seedance 2.0 modelleri için 15,1 saniye).
* Referans videoları ayrıca seçilen çözünürlük için modelin piksel sayısı sınırlarını karşılamalıdır. `auto_downscale` etkinken (varsayılan), boyutu büyük videolar otomatik olarak yeniden boyutlandırılır; `auto_upscale` etkinken, boyutu küçük videolar büyütülür. Otomatik ayarlamalardan herhangi biri devre dışı bırakılırsa, ilgili sınırın dışındaki videolar hata verir.
* Seedance 2.5 üzerinde `video_editing` etkinleştirildiğinde, `duration` ve `ratio` girdileri yok sayılır; çıktı, referans videosunun kendi uzunluğu ve en-boy oranıyla eşleşir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
