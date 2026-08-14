# ByteDance Seedance 2.0 Referanstan Videoya

Bu düğüm, ByteDance'in Seedance 2.5 veya 2.0 yapay zeka modellerini kullanarak videolar oluşturur, düzenler veya genişletir. Videoyu bir metin istemiyle tanımlarsınız ve sonucu yönlendirmek için referans görseller, videolar ve sesler ekleyebilirsiniz. Çok modlu referans girdilerini, video düzenlemeyi ve video genişletmeyi destekler.

## Girdiler

Bir `model` seçmek, aşağıdaki parametrelerden hangilerinin kullanılabilir olduğunu belirler. `video_editing` ve `output_format` yalnızca Seedance 2.5 seçildiğinde görünür. Genişletilebilir referans yuvaları ve referans video otomatik yeniden boyutlandırma seçenekleri tüm modeller tarafından paylaşılır ve Referans Girdileri altında açıklanır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan yapay zeka modeli. En yeni model için Seedance 2.5, 30 saniyeye kadar videolar ve mp4 çıktısı; maksimum kalite ve 1080p/4k için Seedance 2.0; hız optimizasyonu için Fast; en hızlı, en düşük maliyetli oluşturma için Mini. Bir model seçmek, aşağıda listelenen modele özgü girdileri ortaya çıkarır. | COMBO | Evet | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |

### Seedance 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için konuşma satırlarını çift tırnak içine alın. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: `"720p"`). | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 ile 30<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |
| `video_editing` | İstem, örneğin içindeki bir nesneyi değiştirmek gibi bağlı bir referans videoyu düzenlediğinde etkinleştirin. Çıktı daha sonra kaynak klibin kendi uzunluğunu ve en-boy oranını korur; süre ve oran widget'ları yok sayılır. Yeni bir video oluşturmak veya bir videoyu belirlediğiniz süreye kadar genişletmek için kapalı bırakın (varsayılan: False). | BOOLEAN | Evet | `True`<br>`False` |
| `output_format` | Çıktı videosunun kap formatı (varsayılan: `"mp4"`). | COMBO | Evet | `"mp4"` |

### Seedance 2.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ile 15<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Seedance 2.0 Fast ve Seedance 2.0 Mini tarafından paylaşılır. Bu iki model, Seedance 2.0 ile aynı girdi kümesini sunar; ancak `resolution` 480p ve 720p ile sınırlıdır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"` |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"adaptive"`). | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 7). | INT | Evet | 4 ile 15<br>Adım: 1 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştir (varsayılan: True). | BOOLEAN | Evet | `True`<br>`False` |

### Referans Girdileri

Tüm modeller için kullanılabilir. Maksimum yuva sayısı seçilen modele bağlıdır: Seedance 2.5, Seedance 2.0 modellerinden daha fazla referansı destekler.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: video oluşturmayı yönlendiren bir veya daha fazla referans görseli (`image_1`, `image_2`, ...) bağlayın. Görseller otomatik olarak maksimum 6000 piksel kenar uzunluğuna küçültülür ve en az 300x300 piksel boyutunda, 0,4 ile 2,5 arasında bir en-boy oranına sahip olmalıdır. | IMAGE | Hayır | En fazla 30 (Seedance 2.5)<br>En fazla 9 (Seedance 2.0 modelleri) |
| `reference_videos` | Genişletilebilir yuva: video oluşturmayı yönlendiren bir veya daha fazla referans videoyu (`video_1`, `video_2`, ...) bağlayın; video düzenleme ve genişletme için kullanılır. | VIDEO | Hayır | En fazla 10 (Seedance 2.5)<br>En fazla 3 (Seedance 2.0 modelleri) |
| `reference_audios` | Genişletilebilir yuva: video oluşturmayı yönlendiren bir veya daha fazla referans ses klibini (`audio_1`, `audio_2`, ...) bağlayın. | AUDIO | Hayır | En fazla 10 (Seedance 2.5)<br>En fazla 3 (Seedance 2.0 modelleri) |
| `auto_downscale` | Seçilen çözünürlük için modelin piksel bütçesini aşan referans videoları otomatik olarak küçültür. En-boy oranı korunur; zaten sınırlar içinde olan videolara dokunulmaz (varsayılan: True). | BOOLEAN | Hayır | `True`<br>`False` |
| `auto_upscale` | Seçilen çözünürlük için modelin minimum piksel sayısının altında olan referans videoları otomatik olarak büyütür. En-boy oranı korunur; minimumu zaten karşılayan videolara dokunulmaz. Not: Düşük çözünürlüklü bir kaynağı büyütmek gerçek ayrıntı eklemez ve daha düşük kaliteli oluşturmalar üretebilir (varsayılan: False). | BOOLEAN | Hayır | `True`<br>`False` |
| `reference_assets` | Genişletilebilir yuva: referans olarak kullanılacak önceden oluşturulmuş Seedance sanal kitaplık varlıklarının (Görsel, Video veya Ses) kimlikleri (`asset_1`, `asset_2`, ...). Her varlık mevcut olmalı ve Etkin duruma sahip olmalıdır. İstemde, varlıklara `asset1`, `asset 1` vb. şeklinde atıfta bulunulabilir; düğüm bu belirteçleri "Görsel 2" gibi etiketlerle değiştirir. | STRING | Hayır | En fazla 30 (Seedance 2.5)<br>En fazla 9 (Seedance 2.0 modelleri) |

**Önemli Kısıtlamalar:**

* En az bir referans gereklidir. Seedance 2.0, 2.0 Fast ve 2.0 Mini için en az bir görsel veya video referansı sağlamanız gerekir (`reference_images`, `reference_videos` veya `reference_assets` içinde bir görsel ya da video girdisi aracılığıyla). Seedance 2.5 ayrıca yalnızca ses içeren referansları da kabul eder (`reference_audios` veya bir ses `reference_assets` girdisi aracılığıyla).
* Referans sayıları modele bağlıdır ve doğrudan girdiler ile varlık referanslarının birleşimi üzerinden doğrulanır: Seedance 2.5, en fazla 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` ve 30 `reference_assets` öğesine izin verir; Seedance 2.0 modelleri en fazla 9 görsele, 3 videoya, 3 ses klibine ve 9 varlığa izin verir.
* Her referans video en az 1,8 saniye uzunluğunda olmalı ve her referans ses klibi en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans videolarının ve tüm referans seslerinin toplam süresi, seçilen modelin sınırı içinde kalmalıdır (Seedance 2.0 modelleri için 15,1 saniye).
* Referans videolar ayrıca seçilen çözünürlük için modelin piksel sayısı limitlerini karşılamalıdır. `auto_downscale` etkinleştirildiğinde (varsayılan), büyük videolar otomatik olarak yeniden boyutlandırılır; `auto_upscale` etkinleştirildiğinde, küçük videolar büyütülür. Otomatik ayarlamalardan herhangi biri devre dışı bırakılırsa, ilgili limitin dışındaki videolar bir hata verir.
* Seedance 2.5'te `video_editing` etkinleştirildiğinde, `duration` ve `ratio` girdileri yok sayılır; çıktı, referans videonun kendi uzunluğu ve en-boy oranıyla eşleşir. Sağlayıcı istemi bir referans videoyu düzenleme olarak yorumlarsa, `video_editing` etkinleştirilmediği veya istem yeni bir videoyu tanımlayacak şekilde yeniden ifade edilmediği sürece oluşturma başarısız olur.
* Sağlayıcı, video için oluşturulan ses parçasını reddederse (örneğin, olası bir telif hakkı eşleşmesi), görev başarısız olur; `generate_audio` seçeneğini devre dışı bırakmak sessiz bir video üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
