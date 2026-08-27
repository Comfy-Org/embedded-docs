# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video, bir metin istemi ve isteğe bağlı referans görseller, videolar, sesler veya daha önce yüklenmiş kütüphane varlıkları tarafından yönlendirilen ByteDance Seedance modellerini (Seedance 2.5, 2.0, 2.0 Fast ve 2.0 Mini) kullanarak videolar oluşturur, düzenler veya genişletir. Referansları yükler, bir oluşturma görevi gönderir, tamamlanmasını bekler ve bitmiş video dosyasını döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. En yeni model için Seedance 2.5, 30 saniyeye kadar videolar ve mp4/mov çıktısı; maksimum kalite ve 4k için Seedance 2.0; hız optimizasyonu için Fast; en hızlı ve en düşük maliyetli oluşturma için Mini. Bir model seçmek, aşağıda gösterilen girdi widget'larını değiştirir. | DYNAMIC_COMBO | Evet | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 ila 2147483647 |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. Varsayılan: False. Gelişmiş ayar. | BOOLEAN | Evet | true<br>false |

### Seedance 2.5 Girdileri

Bu girdiler `model` "Seedance 2.5" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Oluşturulan diyaloğu yönlendirmek için sözlü satırları çift tırnak içine alın. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: 720p. | COMBO | Evet | "480p"<br>"720p"<br>"1080p" |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan: 16:9. | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-30). Varsayılan: 5. | INT | Evet | 4 ila 30 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `task_type` | Referans medyayla ne yapılacağı. auto dışındaki her değer görev gönderildiğinde doğrulanır; bu nedenle uyumsuz ayarlar oluşturma başlamadan önce başarısız olur.<br>auto: model görevi istemden ve girdilerden çıkarır ve kendi okumasıyla çelişen ayarlar yalnızca oluşturma başladıktan sonra başarısız olur.<br>reference: referans görseller, videolar ve sesler tarafından yönlendirilen yeni bir video oluşturur.<br>edit: bağlı bir referans videoyu değiştirir (ekleme, çıkarma, değiştirme); çıktı kaynak klibin kendi uzunluğunu ve en-boy oranını korur ve süre ile oran widget'ları yok sayılır.<br>extend: bağlı bir referans videoyu ileri veya geri doğru genişletir; istem "extend forward", "extend backward" veya "continue" demelidir, en-boy oranı kaynak klibi takip eder ve çıktı yalnızca kaynak klibi değil, sizin belirlediğiniz süredeki yeni oluşturulan bölümü içerir. Varsayılan: auto. | COMBO | Evet | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | Çıktı videosunun kap formatı. Varsayılan: mp4. | COMBO | Evet | "mp4" |

### Seedance 2.0 Girdileri

Bu girdiler `model` "Seedance 2.0" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan: adaptive. | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan: 7. | INT | Evet | 4 ila 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. Varsayılan: True. | BOOLEAN | Evet | true<br>false |

### Seedance 2.0 Fast ve Seedance 2.0 Mini Girdileri

Bu girdiler `model` "Seedance 2.0 Fast" veya "Seedance 2.0 Mini" olarak ayarlandığında görünür. Her iki model de aynı girdi kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Varsayılan: boş dize. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "480p"<br>"720p" |
| `ratio` | Çıktı videosunun en-boy oranı. Varsayılan: adaptive. | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15). Varsayılan: 7. | INT | Evet | 4 ila 15 |
| `generate_audio` | Çıktı videosu için ses oluşturmayı etkinleştirir. Varsayılan: True. | BOOLEAN | Evet | true<br>false |

### Referans Girdileri

Bu genişletilebilir referans yuvaları tüm modeller için kullanılabilir. Maksimum yuva sayısı modele göre değişir: Seedance 2.5, 30 görsele, 10 videoya, 10 sese ve 30 varlığa kadar destekler; Seedance 2.0, 2.0 Fast ve 2.0 Mini ise 9 görsele, 3 videoya, 3 sese ve 9 varlığa kadar destekler.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: çıktıyı yönlendiren 1..N referans görseli bağlayın. Sayı sınırı modele göredir (model bölümlerine bakın). Görseller en-boy oranı (0.4 ila 2.5) için doğrulanır ve maksimum kenarı 6000 piksele otomatik olarak küçültülür. | IMAGE | Hayır | 1..9 yuva (Seedance 2.0 ailesi)<br>1..30 yuva (Seedance 2.5) |
| `reference_videos` | Genişletilebilir yuva: 1..N referans video bağlayın. Sayı sınırı modele göredir (model bölümlerine bakın). Her video en az 1,8 saniye uzunluğunda olmalı ve seçilen model ile çözünürlüğün piksel sınırlarına uymalıdır. | VIDEO | Hayır | 1..3 yuva (Seedance 2.0 ailesi)<br>1..10 yuva (Seedance 2.5) |
| `reference_audios` | Genişletilebilir yuva: 1..N referans ses parçası bağlayın. Sayı sınırı modele göredir (model bölümlerine bakın). Her ses en az 1,8 saniye uzunluğunda olmalıdır. | AUDIO | Hayır | 1..3 yuva (Seedance 2.0 ailesi)<br>1..10 yuva (Seedance 2.5) |
| `reference_assets` | Genişletilebilir yuva: Seedance sanal kütüphanesine zaten yüklenmiş medya için 1..N varlık kimliği dizesi bağlayın. Her varlık Active durumunda olmalıdır. İstemde `asset1` veya `asset 1` gibi belirteçlerle bir varlığa atıfta bulunabilirsiniz; düğüm bunları varlığın konumsal etiketiyle (örneğin "Image 2" veya "Video 1") değiştirir. | STRING | Hayır | 1..9 yuva (Seedance 2.0 ailesi)<br>1..30 yuva (Seedance 2.5) |
| `auto_downscale` | Seçilen çözünürlük için modelin piksel bütçesini aşan referans videoları otomatik olarak küçültür. En-boy oranı korunur; zaten sınırlar içinde olan videolara dokunulmaz. Varsayılan: True. | BOOLEAN | Hayır | true<br>false |
| `auto_upscale` | Seçilen çözünürlük için modelin minimum piksel sayısının altında kalan referans videoları otomatik olarak büyütür. En-boy oranı korunur; minimumu zaten karşılayan videolara dokunulmaz. Not: Düşük çözünürlüklü bir kaynağı büyütmek gerçek ayrıntı eklemez ve daha düşük kaliteli oluşturmalara neden olabilir. Varsayılan: False. Gelişmiş ayar. | BOOLEAN | Hayır | true<br>false |

**Not:** Düğümü çalıştırmak için en az bir referans görsel, video veya varlık gereklidir (Seedance 2.5 yalnızca ses içeren referansları da kabul eder). Referans videoların ve seslerin her biri en az 1,8 saniye uzunluğunda olmalıdır ve tüm referans videoların (ve ayrıca tüm referans seslerin) birleşik süresi, seçilen modelin maksimum toplam saniyesini aşmamalıdır. Referans görseller yaklaşık 2:5 ila 5:2 (0.4 ila 2.5) arasında bir en-boy oranına sahip olmalı, en az 300x300 piksel olmalı ve otomatik olarak maksimum kenarı 6000 piksele küçültülür. `task_type` "edit" ve "extend" seçenekleri yalnızca Seedance 2.5 ile kullanılabilir ve her ikisi de en az bir referans video gerektirir; "edit" kullanıldığında çıktı kaynak klibin kendi uzunluğunu ve en-boy oranını korur ve `duration` ile `ratio` widget'ları yok sayılır; "extend" kullanıldığında çıktı yalnızca sizin belirlediğiniz süredeki yeni oluşturulan bölümü içerir. Referans verilen varlıklar Active durumunda olmalıdır, aksi takdirde görev başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video, oluşturma görevi tamamlandığında sağlayıcıdan indirilir. Ses oluşturma etkinleştirildiğinde ses içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
