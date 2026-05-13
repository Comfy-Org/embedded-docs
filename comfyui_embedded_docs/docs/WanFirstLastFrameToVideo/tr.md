> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/tr.md)

WanFirstLastFrameToVideo düğümü, başlangıç ve bitiş karelerini metin istemleriyle birleştirerek video koşullandırması oluşturur. İlk ve son kareleri kodlayarak, oluşturma sürecini yönlendirmek için maskeler uygulayarak ve mevcut olduğunda CLIP görüntü özelliklerini dahil ederek video oluşturma için bir gizli temsil oluşturur. Bu düğüm, video modelleri için belirtilen başlangıç ve bitiş noktaları arasında tutarlı diziler oluşturmak üzere hem olumlu hem de olumsuz koşullandırma hazırlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için olumlu metin koşullandırması |
| `negative` | CONDITIONING | Evet | - | Video oluşturmayı yönlendirmek için olumsuz metin koşullandırması |
| `vae` | VAE | Evet | - | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK | Çıktı videosu genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK | Çıktı videosu yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 - MAKSİMUM ÇÖZÜNÜRLÜK | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `clip_vision_start_image` | CLIP_VISION_OUTPUT | Hayır | - | Başlangıç görüntüsünden çıkarılan CLIP görüntü özellikleri |
| `clip_vision_end_image` | CLIP_VISION_OUTPUT | Hayır | - | Bitiş görüntüsünden çıkarılan CLIP görüntü özellikleri |
| `start_image` | IMAGE | Hayır | - | Video dizisi için başlangıç kare görüntüsü |
| `end_image` | IMAGE | Hayır | - | Video dizisi için bitiş kare görüntüsü |

**Not:** Hem `start_image` hem de `end_image` sağlandığında, düğüm bu iki kare arasında geçiş yapan bir video dizisi oluşturur. `clip_vision_start_image` ve `clip_vision_end_image` parametreleri isteğe bağlıdır ancak sağlandıklarında, CLIP görüntü özellikleri birleştirilir ve hem olumlu hem de olumsuz koşullandırmaya uygulanır. `start_image`, işlemeden önce ilk `length` kareye, `end_image` ise son `length` kareye kırpılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Uygulanmış video kare kodlaması ve CLIP görüntü özellikleri ile olumlu koşullandırma |
| `negative` | CONDITIONING | Uygulanmış video kare kodlaması ve CLIP görüntü özellikleri ile olumsuz koşullandırma |
| `latent` | LATENT | Boyutları belirtilen video parametreleriyle eşleşen boş gizli tensör |

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
