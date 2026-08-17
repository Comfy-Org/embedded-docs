# LTXVImgToVideoInplace

LTXVImgToVideoInplace düğümü, bir girdi görüntüsünü başlangıç karelerine kodlayarak bir video latent temsilini koşullandırır. Görüntüyü latent uzaya kodlamak için bir VAE kullanır ve ardından latent video örneklerinin ilk karelerini bu kodlanmış görüntüyle değiştirir. Bir gürültü maskesi uygulanır; böylece koşullandırma gücü, görüntünün üretim sırasında bu başlangıç karelerini ne kadar güçlü etkilediğini kontrol eder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Girdi görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `image` | Kodlanacak ve video latentini koşullandırmak için kullanılacak girdi görüntüsü. | IMAGE | Evet | - |
| `latent` | Değiştirilecek hedef latent video temsili. | LATENT | Evet | - |
| `strength` | Kodlanmış görüntünün başlangıç latent kareleri üzerindeki koşullandırma gücünü kontrol eder. 1.0 değeri başlangıç karelerini tamamen koşullandırırken, daha düşük değerler daha zayıf koşullandırma uygular. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `bypass` | Koşullandırmayı atlar. Etkinleştirildiğinde, düğüm girdi latentini değiştirmeden döndürür. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** `image`, `latent` girdisinin genişliğine ve yüksekliğine dayalı olarak `vae` tarafından kodlama için gereken uzamsal boyutlara uyacak şekilde otomatik olarak yeniden boyutlandırılır (bilineer enterpolasyon). Görüntünün yalnızca ilk 3 renk kanalı (RGB) kullanılır; herhangi bir alfa kanalı yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Değiştirilmiş latent video temsili. Güncellenmiş örnekleri ve başlangıç karelerine koşullandırma gücünü uygulayan bir `noise_mask` içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/tr.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
