# WanKameraGörüntüdenVideoya

WanCameraImageToVideo düğümü, görüntülerden kamera kontrollü video üretimi için koşullandırma ve latent verilerini hazırlar. Pozitif ve negatif koşullandırma istemlerinin yanı sıra başlangıç görüntüsü, CLIP görü çıktısı ve kamera koşulları gibi isteğe bağlı girdileri alır; güncellenmiş koşullandırma ile bir video modelinin doldurabilmesi için hazır boş bir latent tensörü çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimi için pozitif koşullandırma istemleri | CONDITIONING | Evet | - |
| `negatif` | Video üretiminde kaçınılacak negatif koşullandırma istemleri | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent uzaya kodlamak için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı video genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı video yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_iş_boyutu` | Aynı anda üretilecek video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `clip_vision_çıktısı` | Ek koşullandırma için isteğe bağlı CLIP görü çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video dizisini başlatmak için isteğe bağlı başlangıç görüntüsü. Sağlandığında, yalnızca ilk `length` kare kullanılır ve görüntü belirtilen `width` ile `height` değerlerine uyacak şekilde yeniden boyutlandırılır. Dizinin ilk kareleri latent içine kodlanır ve başlangıç karelerini üretilen içerikle harmanlamak için bir maske uygulanır. | IMAGE | Hayır | - |
| `kamera_koşulları` | Video üretimi için isteğe bağlı kamera gömme koşulları. Sağlandığında, bu koşullar hem pozitif hem de negatif koşullandırmaya uygulanır. | WAN_CAMERA_EMBEDDING | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm hem `positive` hem de `negative` koşullandırmasında `concat_latent_image` ve `concat_mask` değerlerini ayarlar. `camera_conditions` ve `clip_vision_output` parametreleri isteğe bağlıdır, ancak sağlandıklarında hem pozitif hem de negatif istemler için koşullandırmayı değiştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Uygulanan kamera koşulları, CLIP görü çıktısı ve/veya başlangıç görüntüsü verileriyle değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Uygulanan kamera koşulları, CLIP görü çıktısı ve/veya başlangıç görüntüsü verileriyle değiştirilmiş negatif koşullandırma | CONDITIONING |
| `latent` | Video modelleriyle kullanılmak üzere boş video latent temsili. Latent tensörünün boyutları [batch_size, 16, frames, height/8, width/8] şeklindedir; burada frames, ((length - 1) // 4) + 1 olarak hesaplanır. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
