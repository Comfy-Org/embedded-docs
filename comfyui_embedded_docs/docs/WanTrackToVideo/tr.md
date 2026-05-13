> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/tr.md)

WanTrackToVideo düğümü, izleme noktalarını işleyerek ve karşılık gelen video karelerini oluşturarak hareket izleme verilerini video dizilerine dönüştürür. Giriş olarak izleme koordinatlarını alır ve video oluşturma için kullanılabilecek video koşullandırması ve gizli temsiller üretir. Hiçbir iz sağlanmadığında, standart görüntüden videoya dönüştürmeye geri döner.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video oluşturma için pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | Video oluşturma için negatif koşullandırma |
| `vae` | VAE | Evet | - | Kodlama ve kod çözme için VAE modeli |
| `tracks` | STRING | Evet | - | Çok satırlı bir dize olarak JSON biçimli izleme verileri (varsayılan: "[]") |
| `width` | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 - MAKSİMUM ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 - MAKSİMUM ÇÖZÜNÜRLÜK | Çıktı videosundaki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 - 4096 | Aynı anda oluşturulacak video sayısı (varsayılan: 1) |
| `temperature` | FLOAT | Evet | 1,0 - 1000,0 | Hareket yamalama için sıcaklık parametresi (varsayılan: 220,0, adım: 0,1) |
| `topk` | INT | Evet | 1 - 10 | Hareket yamalama için en yüksek-k değeri (varsayılan: 2) |
| `start_image` | IMAGE | Hayır | - | Video oluşturma için başlangıç görüntüsü |
| `clip_vision_output` | CLIPVISIONOUTPUT | Hayır | - | Ek koşullandırma için CLIP görüş çıktısı |

**Not:** `tracks` geçerli izleme verileri içerdiğinde, düğüm video oluşturmak için hareket izlerini işler. `tracks` boş olduğunda, standart görüntüden videoya moduna geçer. `start_image` sağlanırsa, video dizisinin ilk karesini başlatır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Hareket izi bilgisi uygulanmış pozitif koşullandırma |
| `latent` | CONDITIONING | Hareket izi bilgisi uygulanmış negatif koşullandırma |
| `latent` | LATENT | Oluşturulan video gizli temsili |

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
