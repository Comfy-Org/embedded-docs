# WanTrackToVideo

WanTrackToVideo düğümü, video oluşturmayı yönlendirmek için hareket takip verilerini (nokta yörüngeleri) kullanır. Takip verilerini işler, isteğe bağlı olarak bunları bir başlangıç görüntüsüyle birleştirir ve Wan video modeli için pozitif ve negatif koşullandırma çıktılarının yanı sıra bir latent tensör üretir. Geçerli takip verisi sağlanmadığında, standart görüntüden videoya dönüştürme davranışına geri döner.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video oluşturma için pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Video oluşturma için negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `tracks` | Çok satırlı bir dize olarak JSON biçimli takip verisi (varsayılan: "[]") | STRING | Evet | - |
| `width` | Piksel cinsinden çıktı video genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Piksel cinsinden çıktı video yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Çıktı videosundaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `temperature` | Hareket yamalama için gelişmiş sıcaklık parametresi (varsayılan: 220.0, adım: 0.1) | FLOAT | Evet | 1.0 to 1000.0 |
| `topk` | Hareket yamalama için gelişmiş top-k değeri (varsayılan: 2) | INT | Evet | 1 to 10 |
| `start_image` | Video oluşturmanın ilk karesi için kullanılan başlangıç görüntüsü | IMAGE | Evet | - |
| `clip_vision_output` | Ek koşullandırma için CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |

**Notlar:**
- `tracks` girdisi, nokta takip verilerini içeren bir JSON dizesi veya JSON dizeleri listesi bekler. `tracks` boşsa veya ayrıştırılamıyorsa, düğüm WanImageToVideo davranışına geri döner.
- `start_image` mevcut olduğunda, `width` ve `height` ile eşleşecek şekilde yeniden boyutlandırılır ve video dizisinin ilk karesi olarak kullanılır.
- `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Hareket takibi ve isteğe bağlı görüntü bilgisi uygulanmış pozitif koşullandırma | CONDITIONING |
| `negative` | Hareket takibi ve isteğe bağlı görüntü bilgisi uygulanmış negatif koşullandırma | CONDITIONING |
| `latent` | İstenen video boyutları, uzunluk ve batch boyutuna göre boyutlandırılmış sıfır dolgulu latent tensör | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
