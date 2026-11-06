# Kling 4.0 Referanstan Videoya

Kling 4.0 modeliyle referans görüntülerden ve referans videolardan ses dahil olmak üzere bir video oluşturur. Referanslar özneyi, stili ve hareketi yönlendirir; isteğe bağlı bir ilk ve son kare, klibin başlangıcını ve sonunu sabitler. Bir karakteri veya sahneyi bir çekim boyunca tutarlı tutmak ve eylemi istemde tanımlamak için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. `"kling-4.0"` 1080p'ye kadar, 30 saniyelik klipleri ve son kareyi destekler; `"kling-4.0-flash"` 720p ve 20 saniye ile sınırlıdır ve `last_frame` girdisi yoktur. Bir model seçildiğinde, o modelin girdileri aşağıda görünür. | DYNAMIC_COMBO | Evet | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### kling-4.0 Girdileri

Bu girdiler, `model` `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Referans görüntüler için büyütülebilir yuvalar, en fazla 10. İstemde bunlara bağlantı sırasına göre `@Image1`, `@Image2` ve benzeri şekilde atıfta bulunun. | AUTOGROW | Hayır | 0 ile 10 görüntü arası |
| `reference_videos` | Referans videolar için büyütülebilir yuvalar, en fazla 5. İstemde bunlara `@Video1`, `@Video2` ve benzeri şekilde atıfta bulunun. Her video ve tüm videolar birlikte 3 ile 30 saniye arasında olmalıdır. | AUTOGROW | Hayır | 0 ile 5 video arası |
| `first_frame` | Videonun başladığı isteğe bağlı kare. Referans görüntülerle birlikte 10 görüntü sınırına dahildir. | IMAGE | Hayır | - |
| `last_frame` | Videonun bittiği isteğe bağlı kare. Referans görüntülerle birlikte 10 görüntü sınırına dahildir. | IMAGE | Hayır | - |
| `prompt` | Oluşturulacak videonun açıklaması. Girdilere `@Image1`, `@Image2` ve benzeri ile `@Video1`, `@Video2` ve benzeri şekilde atıfta bulunun. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"` önce istemi, ardından ilk kareyi veya referans videoları takip eder; aksi durumda 16:9'a geri döner. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 30 arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

### kling-4.0-flash Girdileri

Bu girdiler, `model` `"kling-4.0-flash"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Referans görüntüler için büyütülebilir yuvalar, en fazla 10. İstemde bunlara bağlantı sırasına göre `@Image1`, `@Image2` ve benzeri şekilde atıfta bulunun. | AUTOGROW | Hayır | 0 ile 10 görüntü arası |
| `reference_videos` | Referans videolar için büyütülebilir yuvalar, en fazla 5. İstemde bunlara `@Video1`, `@Video2` ve benzeri şekilde atıfta bulunun. Her video ve tüm videolar birlikte 3 ile 20 saniye arasında olmalıdır. | AUTOGROW | Hayır | 0 ile 5 video arası |
| `first_frame` | Videonun başladığı isteğe bağlı kare. Referans görüntülerle birlikte 10 görüntü sınırına dahildir. | IMAGE | Hayır | - |
| `prompt` | Oluşturulacak videonun açıklaması. Girdilere `@Image1`, `@Image2` ve benzeri ile `@Video1`, `@Video2` ve benzeri şekilde atıfta bulunun. | STRING | Evet | 1 ile 26000 karakter arası |
| `resolution` | Çıktı videosunun çözünürlüğü. Flash yalnızca 720p oluşturur. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"` önce istemi, ardından ilk kareyi veya referans videoları takip eder; aksi durumda 16:9'a geri döner. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 20 arası |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlar ve davranış:**

* Görüntüler toplamda 10 ile sınırlıdır; referans görüntüler, ilk kare ve son kare bu sayıya dahildir.
* Her görüntü en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* Her referans video 3 ile 30 saniye arasında (`kling-4.0-flash` ile 3 ile 20 arası), en az 700x700 ve en fazla 4553x4553 piksel, toplamda en fazla 8,294,400 piksel olmalı; en-boy oranı 2:5 ile 5:2 arasında ve kare hızı en az 24 fps olmalıdır. Tüm referans videolar birlikte aynı sınırı aşmamalıdır.
* `@ImageN` veya `@VideoN` içeren bir istem, bu türden N'den daha az girdi bağlı olduğunda hata verir.
* Bir ilk veya son kare bağlandığında düğüm, videonun tam olarak o karede başlaması veya bitmesi için bir talimat ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `78a85e66ab05f784102829fc86917b363fabad6bb5443c36b83e250e59ed07b7`
