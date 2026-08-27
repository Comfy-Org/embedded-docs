# WanTrackToVideo

WanTrackToVideo düğümü, takip noktalarını işleyerek ve ilgili video karelerini oluşturarak hareket takip verilerini video dizilerine dönüştürür. Girdi olarak takip koordinatlarını alır ve video oluşturma için kullanılabilen video koşullandırma ve latent temsiller üretir. Hiçbir takip sağlanmadığında, standart görüntüden videoya dönüştürme moduna geri döner.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video oluşturma için pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Video oluşturma için negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Kodlama ve kod çözme için VAE modeli | VAE | Evet | - |
| `tracks` | Çok satırlı bir dize olarak JSON biçiminde takip verileri (varsayılan: "[]"). Her takip, sabit 121 nokta uzunluğuna doldurulur veya kısaltılır. | STRING | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `length` | Çıktı videosundaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `batch_size` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `temperature` | Hareket yamalama için sıcaklık parametresi (varsayılan: 220.0, adım: 0.1) | FLOAT | Evet | 1.0 ile 1000.0 |
| `topk` | Hareket yamalama için top-k değeri (varsayılan: 2) | INT | Evet | 1 ile 10 |
| `start_image` | Video oluşturma için başlangıç görüntüsü | IMAGE | Hayır | - |
| `clip_vision_output` | Ek koşullandırma için CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** `tracks` geçerli takip verileri içerdiğinde, düğüm video oluşturmak için hareket takiplerini işler. `tracks` boş olduğunda, standart görüntüden videoya dönüştürme moduna geçer. `start_image` sağlanırsa, video dizisinin ilk karesini başlatır ve hareket yamalama sonucu hem pozitif hem de negatif koşullandırmaya eklenir. `clip_vision_output` sağlanırsa, bu da hem pozitif hem de negatif koşullandırmaya eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Hareket takip bilgisi uygulanmış pozitif koşullandırma | CONDITIONING |
| `negatif` | Hareket takip bilgisi uygulanmış negatif koşullandırma | CONDITIONING |
| `latent` | Oluşturulan video latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
