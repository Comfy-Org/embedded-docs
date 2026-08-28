# ByteDance Seedance 2.0 Referanstan Videoya

Bu düğüm, ByteDance'in Seedance 2.5 veya 2.0 yapay zeka modellerini kullanarak videolar üretir, düzenler veya genişletir. Videoyu bir metin istemiyle tanımlarsınız ve sonucu yönlendirmek için referans görseller, videolar ve ses ekleyebilirsiniz. Çok modlu referans girdilerini, video düzenlemeyi ve video genişletmeyi destekler. Bu, Seedance reference-to-video düğümünün eski, kullanımdan kaldırılmış sürümüdür.

## Girdiler

Bir `model` seçmek, aşağıdaki parametrelerden hangilerinin kullanılabilir olduğunu belirler. `video_editing` ve `output_format` yalnızca Seedance 2.5 seçildiğinde görünür. Genişletilebilir referans yuvaları ve referans video otomatik boyutlandırma seçenekleri tüm modellerde ortaktır ve Referans Girdileri altında açıklanmıştır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu üretmek için kullanılan yapay zeka modeli. En yeni model için Seedance 2.5, 30 saniyeye kadar videolar ve mp4/mov çıktısı; maksimum kalite ve 4K için Seedance 2.0; hız optimizasyonu için Fast; en hızlı ve en düşük maliyetli üretim için Mini. Bir model seçmek, aşağıda listelenen modele özgü girdileri gösterir. | DYNAMIC_COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 2147483647<br>Adım: 1 |
| `watermark` | Videoya filigran eklenip eklenmeyeceğini belirler (varsayılan: False). Gelişmiş ayar. | BOOLEAN | Evet | `True`<br>`False` |

### Seedance 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Üretilen diyaloğu yönlendirmek için söylenen satırları çift tırnak içine alın. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 ila 30<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `video_editing` | İstemin bağlı bir referans videoyu düzenlemesi durumunda, örneğin içindeki bir nesneyi değiştirmesi durumunda etkinleştirin. Bu durumda çıktı, kaynak klibin kendi uzunluğunu ve en-boy oranını korur; duration ve ratio widget'ları yok sayılır. Yeni bir video üretmek veya bir videoyu belirlediğiniz süreye kadar genişletmek için devre dışı bırakın (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |
| `output_format` | Çıktı videosunun kapsayıcı biçimi (varsayılan: `"mp4"`). | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ila 15<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Seedance 2.0 Fast ve Seedance 2.0 Mini tarafından paylaşılır. Bu iki model, `resolution` değeri 480p ve 720p ile sınırlandırılmış olmak dışında Seedance 2.0 ile aynı girdi kümesini sunar.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ila 15<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses üretimini etkinleştirir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

### Referans Girdileri

Tüm modeller için kullanılabilir. Maksimum yuva sayısı seçilen modele bağlıdır: Seedance 2.5, Seedance 2.0 modellerinden daha fazla referans destekler.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: video üretimini yönlendiren bir veya daha fazla referans görseli bağlayın (`image_1`, `image_2`, ...). Görseller otomatik olarak en fazla 6000 piksel kenar uzunluğuna küçültülür ve en-boy oranı 0,4 ile 2,5 arasında olacak şekilde en az 300x300 piksel olmalıdır. | IMAGE | Hayır | En fazla 30 (Seedance 2.5)<br>En fazla 9 (Seedance 2.0 modelleri) |
| `reference_videos` | Genişletilebilir yuva: video üretimini yönlendiren bir veya daha fazla referans videoyu bağlayın (`video_1`, `video_2`, ...); video düzenleme ve genişletme için kullanılır. | VIDEO | Hayır | En fazla 10 (Seedance 2.5)<br>En fazla 3 (Seedance 2.0 modelleri) |
| `reference_audios` | Genişletilebilir yuva: video üretimini yönlendiren bir veya daha fazla referans ses klibini bağlayın (`audio_1`, `audio_2`, ...). | AUDIO | Hayır | En fazla 10 (Seedance 2.5)<br>En fazla 3 (Seedance 2.0 modelleri) |
| `auto_downscale` | Seçilen çözünürlük için modelin piksel bütçesini aşan referans videoları otomatik olarak küçültür. En-boy oranı korunur; zaten sınırlar içinde olan videolara dokunulmaz (varsayılan: True). | BOOLEAN | Hayır | `True`<br>`False` |
| `auto_upscale` | Gelişmiş ayar. Seçilen çözünürlük için modelin minimum piksel sayısının altında kalan referans videoları otomatik olarak büyütür. En-boy oranı korunur; minimum değeri zaten karşılayan videolara dokunulmaz. Not: düşük çözünürlüklü bir kaynağı büyütmek gerçek ayrıntı eklemez ve daha düşük kaliteli üretimlere yol açabilir (varsayılan: False). | BOOLEAN | Hayır | `True`<br>`False` |
| `reference_assets` | Genişletilebilir yuva: referans olarak kullanılacak daha önce oluşturulmuş Seedance sanal kitaplık varlıklarının (Image, Video veya Audio) kimlikleri (`asset_1`, `asset_2`, ...). Her varlık mevcut olmalı ve Active durumuna sahip olmalıdır. İstem içinde varlıklara `asset1`, `asset 1`, vb. şeklinde atıfta bulunulabilir; düğüm bu belirteçleri "Image 2" gibi etiketlerle değiştirir. | STRING | Hayır | En fazla 30 (Seedance 2.5)<br>En fazla 9 (Seedance 2.0 modelleri) |

**Önemli Kısıtlamalar:**

* En az bir referans gereklidir. Seedance 2.0, 2.0 Fast ve 2.0 Mini için en az bir görsel veya video referansı sağlamanız gerekir (`reference_images`, `reference_videos` veya `reference_assets` içinde bir görsel veya video girdisi aracılığıyla). Seedance 2.5 ayrıca yalnızca ses referanslarını da kabul eder (`reference_audios` veya bir ses `reference_assets` girdisi aracılığıyla).
* Referans sayıları modele bağlıdır ve doğrudan girdiler ile varlık referansları birlikte doğrulanır: Seedance 2.5, 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` ve 30 `reference_assets` öğesine izin verir; Seedance 2.0 modelleri ise en fazla 9 görsel, 3 video, 3 ses klibi ve 9 varlığa izin verir.
* Her referans video en az 1,8 saniye uzunluğunda olmalı ve her referans ses klibi en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans videolarının ve tüm referans seslerinin toplam süresi, seçilen modelin sınırı dahilinde kalmalıdır (Seedance 2.0 modelleri için 15,1 saniye).
* Referans videolar ayrıca seçilen çözünürlük için modelin piksel sayısı sınırlarını karşılamalıdır. `auto_downscale` etkinleştirildiğinde (varsayılan), aşırı büyük videolar otomatik olarak yeniden boyutlandırılır; `auto_upscale` etkinleştirildiğinde, çok küçük videolar büyütülür. Otomatik ayarlamalardan herhangi biri devre dışı bırakılırsa, ilgili sınırın dışındaki videolar bir hata verir.
* Seedance 2.5'te `video_editing` etkinleştirildiğinde, `duration` ve `ratio` girdileri yok sayılır; çıktı, referans videonun kendi uzunluğu ve en-boy oranıyla eşleşir. Sağlayıcı istemi bir referans videoyu düzenleme olarak yorumlarsa, `video_editing` etkinleştirilmediği veya istem yeni bir videoyu tanımlayacak şekilde yeniden ifade edilmediği sürece üretim başarısız olur.
* Sağlayıcı, video için üretilen ses parçasını reddederse (örneğin olası bir telif hakkı eşleşmesi nedeniyle), görev başarısız olur; `generate_audio` devre dışı bırakıldığında sessiz bir video üretilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
