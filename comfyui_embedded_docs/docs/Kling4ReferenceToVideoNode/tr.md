# Kling 4.0 Reference to Video

Kling 4.0 modeli ile referans görüntülerden ve referans videolardan ses dahil video oluşturur. Referanslar konuyu, stili ve hareketi yönlendirir; isteğe bağlı bir ilk ve son kare, klibin başlangıcını ve sonunu sabitler. Bir çekim boyunca bir karakteri veya sahneyi tutarlı tutmak ve eylemi istemde tanımlamak için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Model seçici. Yalnızca `"kling-4.0"` mevcuttur; seçildiğinde aşağıdaki girdileri gösterir. | DYNAMIC_COMBO | Evet | `"kling-4.0"` |

### kling-4.0 Girdileri

Bu girdiler `model` `"kling-4.0"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Referans görüntüler için genişletilebilir yuvalar, en fazla 10. İstemde bunlara bağlantı sırasına göre `@Image1`, `@Image2` vb. olarak atıfta bulunun. | AUTOGROW | Hayır | 0 ila 10 görüntü |
| `reference_videos` | Referans videolar için genişletilebilir yuvalar, en fazla 5. İstemde bunlara `@Video1`, `@Video2` vb. olarak atıfta bulunun. Her video ve tüm videolar birlikte 3 ila 30 saniye uzunluğunda olmalıdır. | AUTOGROW | Hayır | 0 ila 5 video |
| `first_frame` | Videonun başladığı isteğe bağlı kare. Referans görüntülerle birlikte 10 görüntü sınırına sayılır. | IMAGE | Hayır | - |
| `last_frame` | Videonun bittiği isteğe bağlı kare. Referans görüntülerle birlikte 10 görüntü sınırına sayılır. | IMAGE | Hayır | - |
| `prompt` | Oluşturulacak videonun açıklaması. Girdilere `@Image1`, `@Image2` vb. ve `@Video1`, `@Video2` vb. olarak atıfta bulunun. | STRING | Evet | 1 ila 26000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: `"720p"`. | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Çıktı videosunun en-boy oranı. `"adaptive"` istemi, ardından ilk kareyi veya referans videoları takip eder; aksi takdirde 16:9'a geri döner. Varsayılan: `"adaptive"`. | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ila 30 |
| `seed` | Tohum, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ila 2147483647 |

**Kısıtlamalar ve davranış:**

* Görüntüler, referans görüntüler, ilk kare ve son kare dahil olmak üzere toplamda 10 ile sınırlıdır.
* Her görüntü en az 300x300 piksel olmalı ve en-boy oranı 2:5 ile 5:2 arasında olmalıdır.
* Her referans video 3 ila 30 saniye uzunluğunda, en az 700x700 ve en fazla 4553x4553 piksel, toplamda en fazla 8.294.400 piksel, en-boy oranı 2:5 ile 5:2 arasında ve kare hızı en az 24 fps olmalıdır. Tüm referans videolar birlikte 30 saniyeyi aşmamalıdır.
* `@ImageN` veya `@VideoN` içeren bir istem, bu türden N'den daha az girdi bağlandığında hata verir.
* Bir ilk veya son kare bağlandığında, düğüm videonun tam olarak o karede başladığı veya bittiği yönünde bir talimat ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Görev tamamlandığında sağlayıcıdan indirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bda2298ed6ed06db04a8f342ec6ad0d5a0494e09bfadee72fce4420ebe4eaf6a`
