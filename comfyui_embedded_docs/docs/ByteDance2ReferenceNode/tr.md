# ByteDance Seedance 2.5 Referanstan Videoya (Eski)

Bu düğüm, ByteDance'in Seedance 2.5 veya Seedance 2.0 yapay zeka modellerini kullanarak video oluşturur, düzenler veya uzatır. Videoyu bir metin istemiyle tanımlarsınız ve sonucu yönlendirmek için referans görüntüler, videolar ve ses ekleyebilirsiniz; çok modlu referans, video düzenleme ve video uzatma desteklenir. Bu, Seedance referanstan videoya düğümünün eski, kullanımdan kaldırılmış sürümüdür.

## Girdiler

`model` seçimi, aşağıdaki parametrelerden hangilerinin kullanılabilir olduğunu belirler. `video_editing` ve `output_format` yalnızca Seedance 2.5 seçildiğinde görünür. Genişletilebilir referans yuvaları ve referans videosu otomatik yeniden boyutlandırma seçenekleri tüm modeller tarafından paylaşılır ve Referans Girdileri altında açıklanmıştır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan yapay zeka modeli. En yeni model için Seedance 2.5, 30 saniyeye kadar videolar ve mp4/mov çıktısı; maksimum kalite ve 4k için Seedance 2.0; hız optimizasyonu için Fast; en hızlı, en düşük maliyetli oluşturma için Mini. Bir model seçildiğinde, aşağıda listelenen modele özgü girdiler görünür. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 arası<br>Adım: 1 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | `True`<br>`False` |

### Seedance 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için konuşma satırlarını çift tırnak içine alın. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 ile 30 arası<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `video_editing` | İstem, bağlı bir referans videosunu düzenlediğinde etkinleştirin; örneğin içindeki bir nesneyi değiştirmek için. Çıktı bu durumda kaynak klibin kendi uzunluğunu ve en-boy oranını korur; `duration` ve `ratio` bileşenleri yok sayılır. Yeni bir video oluşturmak veya bir videoyu ayarladığınız süreye uzatmak için devre dışı bırakın (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |
| `output_format` | Çıktı videosunun kapsayıcı biçimi (varsayılan: `"mp4"`). | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ile 15 arası<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Seedance 2.0 Fast ve Seedance 2.0 Mini tarafından paylaşılır. Bu iki model, `resolution` 480p ve 720p ile sınırlı olması dışında Seedance 2.0 ile aynı girdi kümesini sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ile 15 arası<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

### Referans Girdileri

Tüm modeller için kullanılabilir. Maksimum yuva sayısı seçilen modele bağlıdır: Seedance 2.5, Seedance 2.0 modellerinden daha fazla referansı destekler.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: video oluşturmayı yönlendiren bir veya daha fazla referans görüntüsü (`image_1`, `image_2`, ...) bağlayın. Görüntüler otomatik olarak en fazla 6000 piksel kenara küçültülür ve en az 300x300 piksel olmalı, en-boy oranı 0.4 ile 2.5 arasında olmalıdır. | IMAGE | Hayır | En fazla 30 (Seedance 2.5)<br>En fazla 9 (Seedance 2.0 modelleri) |
| `reference_videos` | Genişletilebilir yuva: video oluşturmayı yönlendiren bir veya daha fazla referans videosu (`video_1`, `video_2`, ...) bağlayın; video düzenleme ve uzatma için kullanılır. | VIDEO | Hayır | En fazla 10 (Seedance 2.5)<br>En fazla 3 (Seedance 2.0 modelleri) |
| `reference_audios` | Genişletilebilir yuva: video oluşturmayı yönlendiren bir veya daha fazla referans ses klibi (`audio_1`, `audio_2`, ...) bağlayın. | AUDIO | Hayır | En fazla 10 (Seedance 2.5)<br>En fazla 3 (Seedance 2.0 modelleri) |
| `auto_downscale` | Seçilen çözünürlük için modelin piksel bütçesini aşan referans videolarını otomatik olarak küçültür. En-boy oranı korunur; zaten sınırlar içinde olan videolara dokunulmaz (varsayılan: True). | BOOLEAN | Hayır | `True`<br>`False` |
| `auto_upscale` | Gelişmiş ayar. Seçilen çözünürlük için modelin minimum piksel sayısının altında olan referans videolarını otomatik olarak büyütür. En-boy oranı korunur; minimumu zaten karşılayan videolara dokunulmaz. Not: düşük çözünürlüklü bir kaynağı büyütmek gerçek ayrıntı eklemez ve daha düşük kaliteli oluşturmalara yol açabilir (varsayılan: False). | BOOLEAN | Hayır | `True`<br>`False` |
| `reference_assets` | Genişletilebilir yuva: referans olarak kullanılacak, önceden oluşturulmuş Seedance sanal kitaplık varlıklarının (Görüntü, Video veya Ses) kimlikleri (`asset_1`, `asset_2`, ...). Her varlık mevcut olmalı ve Etkin durumda olmalıdır. İstem içinde varlıklara `asset1`, `asset 1` vb. olarak atıfta bulunulabilir; düğüm bu belirteçleri "Image 2" gibi etiketlerle değiştirir. | STRING | Hayır | En fazla 30 (Seedance 2.5)<br>En fazla 9 (Seedance 2.0 modelleri) |

**Önemli Kısıtlamalar:**

* En az bir referans gereklidir. Seedance 2.0, 2.0 Fast ve 2.0 Mini için en az bir görüntü veya video referansı sağlamalısınız (`reference_images`, `reference_videos` veya `reference_assets` içinde bir görüntü ya da video girdisi aracılığıyla). Seedance 2.5 ayrıca yalnızca ses referanslarını kabul eder (`reference_audios` veya bir ses `reference_assets` girdisi aracılığıyla).
* Referans sayıları modele bağlıdır ve doğrudan girdiler ile varlık referansları birleştirilerek doğrulanır: Seedance 2.5 en fazla 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` ve 30 `reference_assets` değerine izin verir; Seedance 2.0 modelleri en fazla 9 görüntü, 3 video, 3 ses klibi ve 9 varlığa izin verir.
* Her referans videosu en az 1.8 saniye uzunluğunda olmalıdır ve her referans ses klibi en az 1.8 saniye uzunluğunda olmalıdır. Tüm referans videolarının ve tüm referans seslerinin toplam süresi seçilen modelin sınırı içinde kalmalıdır (Seedance 2.0 modelleri için 15.1 saniye).
* Referans videoları ayrıca seçilen çözünürlük için modelin piksel sayısı sınırlarını karşılamalıdır. `auto_downscale` etkinleştirildiğinde (varsayılan), aşırı büyük videolar otomatik olarak yeniden boyutlandırılır; `auto_upscale` etkinleştirildiğinde, alt sınırın altındaki videolar büyütülür. Otomatik ayarlamalardan biri devre dışı bırakılırsa, ilgili sınırın dışındaki videolar hata verir.
* Seedance 2.5 üzerinde `video_editing` etkinleştirildiğinde, `duration` ve `ratio` girdileri yok sayılır; çıktı, referans videosunun kendi uzunluğu ve en-boy oranıyla eşleşir. Sağlayıcı istemi bir referans videosunu düzenleme olarak yorumlarsa, `video_editing` etkinleştirilmedikçe veya istem yeni bir videoyu tanımlayacak şekilde yeniden yazılmadıkça oluşturma başarısız olur.
* Sağlayıcı, video için oluşturulan ses parçasını reddederse (örneğin olası bir telif hakkı eşleşmesi), görev başarısız olur; `generate_audio` devre dışı bırakıldığında sessiz bir video üretilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
