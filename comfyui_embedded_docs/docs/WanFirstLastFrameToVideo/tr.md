# WanİlkSonKaredenVideoya

WanFirstLastFrameToVideo düğümü, başlangıç ve bitiş karelerini metin istemleriyle birleştirerek video koşullandırması oluşturur. İlk ve son kareleri kodlayarak, üretim sürecini yönlendirmek için maskeler uygulayarak ve mevcut olduğunda CLIP vision özelliklerini dahil ederek video üretimi için bir gizli uzay temsili oluşturur. Bu düğüm, belirtilen başlangıç ve bitiş noktaları arasında tutarlı diziler üretmek için video modelleri için hem pozitif hem de negatif koşullandırma hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimini yönlendirmek için pozitif metin koşullandırması | CONDITIONING | Evet | - |
| `negative` | Video üretimini yönlendirmek için negatif metin koşullandırması | CONDITIONING | Evet | - |
| `vae` | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı video genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı video yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `clip_vision_start_image` | Başlangıç görüntüsünden çıkarılan CLIP vision özellikleri | CLIP_VISION_OUTPUT | Hayır | - |
| `clip_vision_end_image` | Bitiş görüntüsünden çıkarılan CLIP vision özellikleri | CLIP_VISION_OUTPUT | Hayır | - |
| `start_image` | Video dizisi için başlangıç karesi görüntüsü | IMAGE | Hayır | - |
| `end_image` | Video dizisi için bitiş karesi görüntüsü | IMAGE | Hayır | - |

**Not:** Hem `start_image` hem de `end_image` sağlandığında, düğüm bu iki kare arasında geçiş yapan bir video dizisi oluşturur. `start_image`, işlemeden önce ilk `length` kareye kırpılır ve `end_image` son `length` kareye kırpılır. Yalnızca biri sağlanırsa, eksik taraf nötr gri karelerle doldurulur. Başlangıç ve bitiş karelerinin mevcut olduğu yerlerde maske 0, diğer yerlerde 1 olarak ayarlanır. `clip_vision_start_image` ve `clip_vision_end_image` parametreleri isteğe bağlıdır; her ikisi de sağlandığında, CLIP vision özellikleri birleştirilir ve hem pozitif hem de negatif koşullandırmaya uygulanır. Yalnızca biri sağlandığında, özellikleri tek başına kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Video kare kodlaması ve CLIP vision özellikleri uygulanmış pozitif koşullandırma | CONDITIONING |
| `negative` | Video kare kodlaması ve CLIP vision özellikleri uygulanmış negatif koşullandırma | CONDITIONING |
| `latent` | Belirtilen video parametreleriyle eşleşen boyutlara sahip boş gizli uzay tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
