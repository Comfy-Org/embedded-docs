# HitPaw Video İyileştirme

The HitPaw Video Enhance düğümü, videoların kalitesini artırmak için harici bir API kullanır. Düşük çözünürlüklü videoları daha yüksek bir çözünürlüğe yükseltir, görsel bozuklukları giderir ve gürültüyü azaltır. İşlem maliyeti, giriş videosunun saniyesi başına hesaplanır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video geliştirme için kullanılacak AI modeli. Bir model seçildiğinde iç içe geçmiş bir `resolution` parametresi görüntülenir. Kullanılabilir modeller ve destekledikleri çözünürlükler farklılık gösterir. | DYNAMIC_COMBO | Evet | `"Portrait Restore Model (1x)"`<br>`"Portrait Restore Model (2x)"`<br>`"General Restore Model (1x)"`<br>`"General Restore Model (2x)"`<br>`"General Restore Model (4x)"`<br>`"Ultra HD Model (2x)"`<br>`"Generative Model (1x)"` |
| `video` | Geliştirilecek giriş video dosyası. | VIDEO | Evet | N/A |

### Portrait Restore, General Restore ve Ultra HD Model Girdileri

Bu çözünürlük seçenekleri Portrait Restore Model (1x), Portrait Restore Model (2x), General Restore Model (1x), General Restore Model (2x), General Restore Model (4x) ve Ultra HD Model (2x) tarafından paylaşılır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `çözünürlük` | Geliştirilmiş videonun hedef çözünürlüğü. `"original"` seçildiğinde giriş videosunun çözünürlüğü korunur. | COMBO | Evet | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"`<br>`"8K"` |

### Generative Model (1x) Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `çözünürlük` | Geliştirilmiş videonun hedef çözünürlüğü. `"original"` seçildiğinde giriş videosunun çözünürlüğü korunur. `"8K"` seçeneği bu model için kullanılamaz. | COMBO | Evet | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"` |

**Notlar:**

* Giriş `video` süresi 0,5 saniye ile 60 dakika (3600 saniye) arasında olmalıdır.
* Seçilen `resolution`, giriş videosunun boyutlarına eşit veya daha büyük olmalıdır. Kare videolar için videonun genişliği ve yüksekliğine eşit veya daha büyük olmalıdır. Kare olmayan videolar için videonun kısa kenarına eşit veya daha büyük olmalıdır. Hedef çözünürlük daha küçükse bir hata oluşturulur. `"original"` seçildiğinde giriş videosunun çözünürlüğü korunur.
* `"original"` dışında bir çözünürlük seçildiğinde, kare olmayan videolar en boy oranı korunarak kısa kenarları seçilen çözünürlükle eşleşecek şekilde ölçeklenir. Kare videolar, her iki boyutu da seçilen çözünürlüğün kare hedef boyutuyla eşleşecek şekilde ölçeklenir (örneğin, `"4K/UHD"` 2048×2048 boyutunda bir çıktı üretir).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Geliştirilmiş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`
