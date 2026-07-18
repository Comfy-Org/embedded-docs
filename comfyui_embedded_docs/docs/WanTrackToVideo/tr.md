WanTrackToVideo düğümü, izleme noktalarını işleyerek ve karşılık gelen video karelerini oluşturarak hareket izleme verilerini video dizilerine dönüştürür. Giriş olarak izleme koordinatlarını alır ve video oluşturma için kullanılabilecek video koşullandırması ve gizli temsiller üretir. Hiçbir iz sağlanmadığında, standart görüntüden videoya dönüştürmeye geri döner.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Video oluşturma için pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Video oluşturma için negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Kodlama ve kod çözme için VAE modeli | VAE | Evet | - |
| `tracks` | Çok satırlı bir dize olarak JSON biçimli izleme verileri (varsayılan: "[]") | STRING | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `length` | Çıktı videosundaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 - MAKSİMUM ÇÖZÜNÜRLÜK |
| `batch_size` | Aynı anda oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `temperature` | Hareket yamalama için sıcaklık parametresi (varsayılan: 220,0, adım: 0,1) | FLOAT | Evet | 1,0 - 1000,0 |
| `topk` | Hareket yamalama için en yüksek-k değeri (varsayılan: 2) | INT | Evet | 1 - 10 |
| `start_image` | Video oluşturma için başlangıç görüntüsü | IMAGE | Hayır | - |
| `clip_vision_output` | Ek koşullandırma için CLIP görüş çıktısı | CLIPVISIONOUTPUT | Hayır | - |

**Not:** `tracks` geçerli izleme verileri içerdiğinde, düğüm video oluşturmak için hareket izlerini işler. `tracks` boş olduğunda, standart görüntüden videoya moduna geçer. `start_image` sağlanırsa, video dizisinin ilk karesini başlatır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Hareket izi bilgisi uygulanmış pozitif koşullandırma | CONDITIONING |
| `negatif` | Hareket izi bilgisi uygulanmış negatif koşullandırma | CONDITIONING |
| `latent` | Oluşturulan video gizli temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
