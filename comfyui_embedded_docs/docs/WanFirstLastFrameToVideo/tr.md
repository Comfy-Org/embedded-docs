> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/tr.md)

WanFirstLastFrameToVideo düğümü, başlangıç ve bitiş karelerini metin istemleriyle birleştirerek video koşullandırma oluşturur. İlk ve son kareleri kodlayarak, üretim sürecini yönlendirmek için maskeler uygulayarak ve mevcut olduğunda CLIP görsel özelliklerini dahil ederek video üretimi için gizli bir temsil oluşturur. Bu düğüm, video modellerinin belirtilen başlangıç ve bitiş noktaları arasında tutarlı diziler oluşturması için hem pozitif hem de negatif koşullandırmayı hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için pozitif metin koşullandırması |
| `negatif` | CONDITIONING | Evet | - | Video üretimini yönlendirmek için negatif metin koşullandırması |
| `vae` | VAE | Evet | - | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosu genişliği (varsayılan: 832, adım: 16) |
| `yükseklik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosu yüksekliği (varsayılan: 480, adım: 16) |
| `uzunluk` | INT | Hayır | 1'den MAX_RESOLUTION'a | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `toplu_boyut` | INT | Hayır | 1'den 4096'ya | Aynı anda üretilecek video sayısı (varsayılan: 1) |
| `clip_görü_başlangıç_görüntüsü` | CLIP_VISION_OUTPUT | Hayır | - | Başlangıç görüntüsünden çıkarılan CLIP görsel özellikleri |
| `clip_görü_bitiş_görüntüsü` | CLIP_VISION_OUTPUT | Hayır | - | Bitiş görüntüsünden çıkarılan CLIP görsel özellikleri |
| `başlangıç_görüntüsü` | IMAGE | Hayır | - | Video dizisi için başlangıç karesi görüntüsü |
| `bitiş_görüntüsü` | IMAGE | Hayır | - | Video dizisi için bitiş karesi görüntüsü |

**Not:** Hem `start_image` hem de `end_image` sağlandığında, düğüm bu iki kare arasında geçiş yapan bir video dizisi oluşturur. `clip_vision_start_image` ve `clip_vision_end_image` parametreleri isteğe bağlıdır ancak sağlandığında, CLIP görsel özellikleri birleştirilir ve hem pozitif hem de negatif koşullandırmaya uygulanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Uygulanan video kare kodlaması ve CLIP görsel özellikleri içeren pozitif koşullandırma |
| `gizli` | CONDITIONING | Uygulanan video kare kodlaması ve CLIP görsel özellikleri içeren negatif koşullandırma |
| `latent` | LATENT | Belirtilen video parametreleriyle eşleşen boyutlara sahip boş gizli tensör |