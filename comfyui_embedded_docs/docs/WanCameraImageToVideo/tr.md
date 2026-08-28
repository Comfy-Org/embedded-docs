# WanKameraGörüntüdenVideoya

WanCameraImageToVideo düğümü, görüntülerden video oluşturma için conditioning ve latent verilerini hazırlar. Pozitif ve negatif conditioning promptlarını, isteğe bağlı bir başlangıç görüntüsü ve isteğe bağlı kamera kontrolleriyle birlikte alır ve değiştirilmiş conditioning ile birlikte bir video modelinin doldurabileceği boş bir latent tensör çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturma için pozitif conditioning promptları | CONDITIONING | Evet | - |
| `negatif` | Video oluşturmada kaçınılacak negatif conditioning promptları | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ila MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `clip_vision_çıktısı` | Ek conditioning için isteğe bağlı CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video dizisini başlatmak için isteğe bağlı başlangıç görüntüsü. Sağlandığında, videonun ilk kareleri bu görüntüye dayanır ve başlangıç karelerini oluşturulan içerikle harmanlamak için bir maske uygulanır. Görüntü, belirtilen genişlik ve yüksekliğe uyacak şekilde yeniden boyutlandırılır. | IMAGE | Hayır | - |
| `kamera_koşulları` | Video oluşturma için isteğe bağlı kamera embedding koşulları. Sağlandığında, bu koşullar hem pozitif hem de negatif conditioning'e uygulanır. | WAN_CAMERA_EMBEDDING | Hayır | - |

**Not:** `start_image` sağlandığında, giriş görüntüsünün yalnızca ilk `length` karesi video dizisini başlatmak için kullanılır ve düğüm, bu başlangıç karelerini oluşturulan içerikle harmanlamak için bir maske uygular. `camera_conditions` ve `clip_vision_output` parametreleri isteğe bağlıdır, ancak sağlandıklarında hem pozitif hem de negatif promptlar için conditioning'i değiştirirler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Uygulanmış kamera koşulları, CLIP vision çıktıları ve/veya başlangıç görüntüsü verileriyle değiştirilmiş pozitif conditioning | CONDITIONING |
| `negatif` | Uygulanmış kamera koşulları, CLIP vision çıktıları ve/veya başlangıç görüntüsü verileriyle değiştirilmiş negatif conditioning | CONDITIONING |
| `latent` | Video modelleriyle kullanım için oluşturulan boş video latent gösterimi. Latent tensör, [batch_size, 16, frames, height/8, width/8] boyutlarına sahiptir; burada frames, ((length - 1) // 4) + 1 olarak hesaplanır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
