# Kling 4.0 Referanstan Videoya

Kling 4.0 modeliyle referans görsellerden ve referans videolardan, ses dahil olmak üzere video oluşturur. Referanslar özneyi, stili ve hareketi yönlendirir; isteğe bağlı bir ilk ve son kare, klibin başlangıcını ve sonunu sabitler. İstemde eylemi açıklarken bir karakteri veya sahneyi bir çekim boyunca tutarlı tutmak için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"kling-4.0"` 4K HDR, 30 saniyelik klipler ve son kareyi destekler; `"kling-4.0-flash"` 720p ve 20 saniye ile sınırlıdır ve `last_frame` girdisi yoktur. Bir model seçmek, aşağıda o modelin girdilerini gösterir. | DYNAMIC_COMBO | Evet | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Girdileri

Bu girdiler, `model` değeri `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Referans görseller için büyütülebilir yuvalar, en fazla 10. İstemde bunlara bağlantı sırasına göre `@Image1`, `@Image2` vb. olarak başvurun. | AUTOGROW | Hayır | 0 ile 10 görsel arası |
| `reference_videos` | Referans videolar için büyütülebilir yuvalar, en fazla 5. İstemde bunlara `@Video1`, `@Video2` vb. olarak başvurun. Her video ve tüm videolar birlikte 3 ile 30 saniye arasında olmalıdır. | AUTOGROW | Hayır | 0 ile 5 video arası |
| `first_frame` | Videonun başladığı isteğe bağlı kare. Referans görsellerle birlikte 10 görsel sınırına dahildir. | IMAGE | Hayır | - |
| `last_frame` | Videonun bittiği isteğe bağlı kare. Referans görsellerle birlikte 10 görsel sınırına dahildir. | IMAGE | Hayır | - |
| `prompt` | Oluşturulacak videonun açıklaması. Girdilere `@Image1`, `@Image2` vb. ve `@Video1`, `@Video2` vb. olarak başvurun. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü; adında `HDR` bulunan bir seçenek HDR video döndürür. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"`, istemi, ardından ilk kareyi veya referans videoları izler; aksi durumda 16:9'a geri döner. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 30 arası |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### kling-4.0-flash Girdileri

Bu girdiler, `model` değeri `"kling-4.0-flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Referans görseller için büyütülebilir yuvalar, en fazla 10. İstemde bunlara bağlantı sırasına göre `@Image1`, `@Image2` vb. olarak başvurun. | AUTOGROW | Hayır | 0 ile 10 görsel arası |
| `reference_videos` | Referans videolar için büyütülebilir yuvalar, en fazla 5. İstemde bunlara `@Video1`, `@Video2` vb. olarak başvurun. Her video ve tüm videolar birlikte 3 ile 20 saniye arasında olmalıdır. | AUTOGROW | Hayır | 0 ile 5 video arası |
| `first_frame` | Videonun başladığı isteğe bağlı kare. Referans görsellerle birlikte 10 görsel sınırına dahildir. | IMAGE | Hayır | - |
| `prompt` | Oluşturulacak videonun açıklaması. Girdilere `@Image1`, `@Image2` vb. ve `@Video1`, `@Video2` vb. olarak başvurun. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Flash yalnızca 720p oluşturur. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"`, istemi, ardından ilk kareyi veya referans videoları izler; aksi durumda 16:9'a geri döner. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 20 arası |
| `seed` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlar ve davranış:**

* Görseller, referans görseller, ilk kare ve son kare dahil olmak üzere toplamda 10 ile sınırlıdır.
* Her görsel en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* Her referans video 3 ile 30 saniye arasında (`kling-4.0-flash` ile 3 ile 20 arası), en az 700x700 ve en fazla 4553x4553 piksel olmalı, toplamda en fazla 8.294.400 piksel olmalı, en-boy oranı 2:5 ile 5:2 arasında ve kare hızı en az 24 fps olmalıdır. Tüm referans videolar birlikte aynı sınırı aşmamalıdır.
* `@ImageN` veya `@VideoN` belirten bir istem, bu türden N'den daha az girdi bağlandığında hata verir.
* Bir ilk veya son kare bağlandığında, düğüm videonun tam olarak o karede başladığını veya bittiğini belirten bir talimat ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d1048c637074d79fa41da1f903a1f4b2c895563dde4c5ee761c20460a8d2e383`
