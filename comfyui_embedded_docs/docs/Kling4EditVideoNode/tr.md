# Kling 4.0 Video Düzenleme

Kling 4.0 modelini kullanarak, isteğe bağlı olarak referans videolar ve referans görseller rehberliğinde, bir metin istemiyle mevcut bir videoyu düzenler. Sonuç, girdi videosunun uzunluğunu korur. Bir klipte ne olduğunu değiştirmek, yeniden biçimlendirmek veya öğeleri değiştirmek için kullanın; orijinal zamanlama bozulmadan kalır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"kling-4.0"` 30 saniyeye kadar 1080p düzenlemeleri destekler; `"kling-4.0-flash"` 720p ve 20 saniye ile sınırlıdır. Bir model seçmek, aşağıda onun girdilerini gösterir. | DYNAMIC_COMBO | Evet | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Girdileri

Bu girdiler, `model` `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Düzenlenecek video, 3 ile 30 saniye arası uzunlukta. Çıktı, uzunluğunu korur. | VIDEO | Evet | 3 ile 30 saniye arası |
| `reference_videos` | Referans videolar için büyütülebilir yuvalar, en fazla 4. İstemde bunlara `@Video2` vb. olarak başvurun. Her video ve tüm videolar birlikte 3 ile 30 saniye arası uzunlukta olmalıdır. | AUTOGROW | Hayır | 0 ile 4 video arası |
| `reference_images` | Referans görseller için büyütülebilir yuvalar, en fazla 10. İstemde bunlara `@Image1`, `@Image2` vb. olarak başvurun. | AUTOGROW | Hayır | 0 ile 10 görsel arası |
| `prompt` | Neyin değiştirileceği ve neyin korunacağının açıklaması. Düzenlenen videoya `@Video1`, referans videolara `@Video2` vb., görsellere ise `@Image1` vb. olarak başvurun. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"` girdi videosunun en-boy oranını korur. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |
| `audio` | `"native"` düzenlenen video için yeni ses oluşturur, `"original"` girdi videosunun sesini korur. Varsayılan: `"native"`. | COMBO | Hayır | `"native"`<br>`"original"` |

### kling-4.0-flash Girdileri

Bu girdiler, `model` `"kling-4.0-flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Düzenlenecek video, 3 ile 20 saniye arası uzunlukta. Çıktı, uzunluğunu korur. | VIDEO | Evet | 3 ile 20 saniye arası |
| `reference_videos` | Referans videolar için büyütülebilir yuvalar, en fazla 4. İstemde bunlara `@Video2` vb. olarak başvurun. Her video ve tüm videolar birlikte 3 ile 20 saniye arası uzunlukta olmalıdır. | AUTOGROW | Hayır | 0 ile 4 video arası |
| `reference_images` | Referans görseller için büyütülebilir yuvalar, en fazla 10. İstemde bunlara `@Image1`, `@Image2` vb. olarak başvurun. | AUTOGROW | Hayır | 0 ile 10 görsel arası |
| `prompt` | Neyin değiştirileceği ve neyin korunacağının açıklaması. Düzenlenen videoya `@Video1`, referans videolara `@Video2` vb., görsellere ise `@Image1` vb. olarak başvurun. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Flash yalnızca 720p oluşturur. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"` girdi videosunun en-boy oranını korur. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |
| `audio` | `"native"` düzenlenen video için yeni ses oluşturur, `"original"` girdi videosunun sesini korur. Varsayılan: `"native"`. | COMBO | Hayır | `"native"`<br>`"original"` |

**Kısıtlamalar ve davranış:**

* Girdi videosu ve her referans video 3 ile 30 saniye arası ( `kling-4.0-flash` ile 3 ile 20 saniye arası), en az 700x700 ve en fazla 4553x4553 piksel, toplamda en fazla 8.294.400 piksel olmalı; en-boy oranı 2:5 ile 5:2 arasında ve kare hızı en az 24 fps olmalıdır. Tüm videolar birlikte aynı sınırı aşmamalıdır.
* Her referans görsel en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır; en fazla 10 görsel bağlanabilir.
* `@VideoN` veya `@ImageN` içeren bir istem, bu türden N'den daha az girdi bağlandığında hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen düzenlenmiş video. Girdi videosuyla aynı uzunluğa sahiptir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c682db61e1426059dc565b12c0da749944394f77f34aaa71b97c69f984cb0931`
