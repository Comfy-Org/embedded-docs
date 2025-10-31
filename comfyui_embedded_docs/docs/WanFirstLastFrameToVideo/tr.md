> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/tr.md)

WanFirstLastFrameToVideo düğümü, başlangıç ve bitiş karelerini metin istemleriyle birleştirerek video koşullandırma oluşturur. İlk ve son kareleri kodlayarak, üretim sürecini yönlendirmek için maskeler uygulayarak ve mevcut olduğunda CLIP görsel özelliklerini dahil ederek video üretimi için gizli bir temsil oluşturur. Bu düğüm, video modellerinin belirtilen başlangıç ve bitiş noktaları arasında tutarlı diziler oluşturması için hem pozitif hem de negatif koşullandırmayı hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için pozitif metin koşullandırması |
| `negative` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için negatif metin koşullandırması |
| `vae` | VAE | Evet | - | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosu genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosu yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Hayır | 1'den MAX_RESOLUTION'a | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Hayır | 1'den 4096'ya | Aynı anda üretilecek video sayısı (varsayılan: 1) |
| `clip_vision_start_image` | CLIP_VISION_OUTPUT | Hayır | - | Başlangıç görüntüsünden çıkarılan CLIP görsel özellikleri |
| `clip_vision_end_image` | CLIP_VISION_OUTPUT | Hayır | - | Bitiş görüntüsünden çıkarılan CLIP görsel özellikleri |
| `start_image` | IMAGE | Hayır | - | Video dizisi için başlangıç karesi görüntüsü |
| `end_image` | IMAGE | Hayır | - | Video dizisi için bitiş karesi görüntüsü |

**Not:** Hem `start_image` hem de `end_image` sağlandığında, düğüm bu iki kare arasında geçiş yapan bir video dizisi oluşturur. `clip_vision_start_image` ve `clip_vision_end_image` parametreleri isteğe bağlıdır ancak sağlandığında, CLIP görsel özellikleri birleştirilir ve hem pozitif hem de negatif koşullandırmaya uygulanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Uygulanan video kare kodlaması ve CLIP görsel özellikleri içeren pozitif koşullandırma |
| `negative` | CONDITIONING | Uygulanan video kare kodlaması ve CLIP görsel özellikleri içeren negatif koşullandırma |
| `latent` | LATENT | Belirtilen video parametreleriyle eşleşen boyutlara sahip boş gizli tensör |