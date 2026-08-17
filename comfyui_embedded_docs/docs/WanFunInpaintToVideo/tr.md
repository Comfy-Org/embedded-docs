# WanEğlenceİçBoyamadanVideoya

WanFunInpaintToVideo düğümü, başlangıç ve bitiş görüntüleri arasında inpainting yaparak video dizileri oluşturur. Video latentleri üretmek için pozitif ve negatif koşullandırma ile birlikte isteğe bağlı kare görüntülerini alır. Düğüm, yapılandırılabilir boyut ve uzunluk parametreleriyle video üretimini yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimi için pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negative` | Video üretiminde kaçınılacak negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Kodlama/kod çözme işlemleri için VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ila MAX_RESOLUTION |
| `batch_size` | Bir batch içinde üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `clip_vision_output` | Ek koşullandırma için isteğe bağlı CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `start_image` | Video üretimi için isteğe bağlı başlangıç karesi görüntüsü | IMAGE | Hayır | - |
| `end_image` | Video üretimi için isteğe bağlı bitiş karesi görüntüsü | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | İşlenmiş pozitif koşullandırma çıktısı | CONDITIONING |
| `negative` | İşlenmiş negatif koşullandırma çıktısı | CONDITIONING |
| `latent` | Üretilen video latent gösterimi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
