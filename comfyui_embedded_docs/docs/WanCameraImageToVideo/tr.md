> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/tr.md)

WanCameraImageToVideo düğümü, video üretimi için gizli temsiller oluşturarak görüntüleri video dizilerine dönüştürür. Video modelleriyle kullanılabilecek video gizli temsilleri oluşturmak için koşullandırma girdilerini ve isteğe bağlı başlangıç görüntülerini işler. Düğüm, gelişmiş video üretimi kontrolü için kamera koşullarını ve clip vision çıktılarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video üretimi için pozitif koşullandırma istemleri |
| `negative` | CONDITIONING | Evet | - | Video üretiminde kaçınılacak negatif koşullandırma istemleri |
| `vae` | VAE | Evet | - | Görüntüleri gizli uzaya kodlamak için VAE modeli |
| `width` | INT | Evet | 16 to MAX_RESOLUTION | Çıktı videosu genişliği piksel cinsinden (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 to MAX_RESOLUTION | Çıktı videosu yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 to MAX_RESOLUTION | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 to 4096 | Aynı anda üretilecek video sayısı (varsayılan: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP vision çıktısı |
| `start_image` | IMAGE | Hayır | - | Video dizisini başlatmak için isteğe bağlı başlangıç görüntüsü |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | Hayır | - | Video üretimi için isteğe bağlı kamera gömme koşulları |

**Not:** `start_image` sağlandığında, düğüm video dizisini başlatmak için bunu kullanır ve başlangıç kareleri ile üretilen içeriği harmanlamak için maskeleme uygular. `camera_conditions` ve `clip_vision_output` parametreleri isteğe bağlıdır ancak sağlandığında, hem pozitif hem de negatif istemler için koşullandırmayı değiştirir.

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Uygulanan kamera koşulları ve clip vision çıktıları ile değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Uygulanan kamera koşulları ve clip vision çıktıları ile değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Video modelleriyle kullanım için üretilen video gizli temsili |