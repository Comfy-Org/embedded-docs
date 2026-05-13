> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/tr.md)

WanCameraImageToVideo düğümü, video oluşturma için gizil temsiller üreterek görüntüleri video dizilerine dönüştürür. Koşullandırma girdilerini ve isteğe bağlı başlangıç görüntülerini işleyerek video modelleriyle kullanılabilecek video gizilleri oluşturur. Düğüm, gelişmiş video oluşturma kontrolü için kamera koşullarını ve clip vision çıktılarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video oluşturma için pozitif koşullandırma yönlendirmeleri |
| `negative` | CONDITIONING | Evet | - | Video oluşturmada kaçınılması gereken negatif koşullandırma yönlendirmeleri |
| `vae` | VAE | Evet | - | Görüntüleri gizil uzaya kodlamak için VAE modeli |
| `width` | INT | Evet | 16 - MAKSİMUM_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 - MAKSİMUM_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 - MAKSİMUM_ÇÖZÜNÜRLÜK | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP vision çıktısı |
| `start_image` | IMAGE | Hayır | - | Video dizisini başlatmak için isteğe bağlı başlangıç görüntüsü. Sağlandığında, videonun ilk kareleri bu görüntüye dayanır ve başlangıç karelerini oluşturulan içerikle harmanlamak için bir maske uygulanır. Görüntü, belirtilen genişlik ve yüksekliğe uyacak şekilde yeniden boyutlandırılır. |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | Hayır | - | Video oluşturma için isteğe bağlı kamera gömme koşulları. Sağlandığında, bu koşullar hem pozitif hem de negatif koşullandırmaya uygulanır. |

**Not:** `start_image` sağlandığında, düğüm video dizisini başlatmak için bunu kullanır ve başlangıç karelerini oluşturulan içerikle harmanlamak için maskeleme uygular. `camera_conditions` ve `clip_vision_output` parametreleri isteğe bağlıdır ancak sağlandıklarında hem pozitif hem de negatif yönlendirmeler için koşullandırmayı değiştirirler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Uygulanan kamera koşulları ve clip vision çıktılarıyla değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Uygulanan kamera koşulları ve clip vision çıktılarıyla değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Video modelleriyle kullanım için oluşturulan video gizil temsili. Gizil tensör, [batch_size, 16, frames, height/8, width/8] boyutlarına sahiptir; burada frames, ((length - 1) // 4) + 1 olarak hesaplanır. |

---
**Source fingerprint (SHA-256):** `19d76097d580b14663afd0aab58810f9dc1685cd32e8f67aa43c820be65239e7`
