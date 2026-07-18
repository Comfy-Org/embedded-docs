WanFirstLastFrameToVideo düğümü, başlangıç ve bitiş karelerini metin istemleriyle birleştirerek video koşullandırması oluşturur. İlk ve son kareleri kodlayarak, oluşturma sürecini yönlendirmek için maskeler uygulayarak ve mevcut olduğunda CLIP görüntü özelliklerini dahil ederek video oluşturma için bir gizli temsil oluşturur. Bu düğüm, video modelleri için belirtilen başlangıç ve bitiş noktaları arasında tutarlı diziler oluşturmak üzere hem olumlu hem de olumsuz koşullandırma hazırlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturmayı yönlendirmek için olumlu metin koşullandırması | CONDITIONING | Evet | - |
| `negatif` | Video oluşturmayı yönlendirmek için olumsuz metin koşullandırması | CONDITIONING | Evet | - |
| `vae` | Görüntüleri gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosu genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `yükseklik` | Çıktı videosu yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `toplu_boyut` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `clip_görü_başlangıç_görüntüsü` | Başlangıç görüntüsünden çıkarılan CLIP görüntü özellikleri | CLIP_VISION_OUTPUT | Hayır | - |
| `clip_görü_bitiş_görüntüsü` | Bitiş görüntüsünden çıkarılan CLIP görüntü özellikleri | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video dizisi için başlangıç kare görüntüsü | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Video dizisi için bitiş kare görüntüsü | IMAGE | Hayır | - |

**Not:** Hem `start_image` hem de `end_image` sağlandığında, düğüm bu iki kare arasında geçiş yapan bir video dizisi oluşturur. `clip_vision_start_image` ve `clip_vision_end_image` parametreleri isteğe bağlıdır ancak sağlandıklarında, CLIP görüntü özellikleri birleştirilir ve hem olumlu hem de olumsuz koşullandırmaya uygulanır. `start_image`, işlemeden önce ilk `length` kareye, `end_image` ise son `length` kareye kırpılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Uygulanmış video kare kodlaması ve CLIP görüntü özellikleri ile olumlu koşullandırma | CONDITIONING |
| `negatif` | Uygulanmış video kare kodlaması ve CLIP görüntü özellikleri ile olumsuz koşullandırma | CONDITIONING |
| `gizli` | Boyutları belirtilen video parametreleriyle eşleşen boş gizli tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
