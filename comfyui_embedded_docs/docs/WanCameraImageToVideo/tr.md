# WanKameraGörüntüdenVideoya

WanCameraImageToVideo, görüntülerden video üretimi için koşullandırma ve latent verileri hazırlar. Pozitif ve negatif koşullandırma istemlerini, isteğe bağlı başlangıç görüntüleri ve kamera kontrolleriyle birlikte alır; değiştirilmiş koşullandırmayı ve bir video modelinin doldurması için hazır boş bir latent tensörü çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video üretimi için pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negative` | Video üretiminde kaçınılacak negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için VAE modeli | VAE | Evet | - |
| `width` | Çıktı video genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `clip_vision_output` | Ek koşullandırma için isteğe bağlı CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `start_image` | Video dizisini başlatmak için isteğe bağlı başlangıç görüntüsü. Sağlandığında, videonun ilk kareleri bu görüntüye dayanır ve başlangıç karelerini üretilen içerikle harmanlamak için bir maske uygulanır. Görüntü, belirtilen genişlik ve yüksekliğe uyacak şekilde yeniden boyutlandırılır. | IMAGE | Hayır | - |
| `camera_conditions` | Video üretimi için isteğe bağlı kamera embedding koşulları. Sağlandığında, bu koşullar hem pozitif hem de negatif koşullandırmaya uygulanır. | WAN_CAMERA_EMBEDDING | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm bunu video dizisini başlatmak için kullanır ve başlangıç karelerini üretilen içerikle harmanlamak için maskeleme uygular. `camera_conditions` ve `clip_vision_output` parametreleri isteğe bağlıdır, ancak sağlandığında hem pozitif hem de negatif istemler için koşullandırmayı değiştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Uygulanmış kamera koşulları, CLIP vision çıktıları ve/veya başlangıç görüntüsü verileriyle değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Uygulanmış kamera koşulları, CLIP vision çıktıları ve/veya başlangıç görüntüsü verileriyle değiştirilmiş negatif koşullandırma | CONDITIONING |
| `latent` | Video modelleriyle kullanılmak üzere üretilmiş boş video latent gösterimi. Latent tensörü [batch_size, 16, frames, height/8, width/8] boyutlarına sahiptir; burada frames, ((length - 1) // 4) + 1 olarak hesaplanır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
