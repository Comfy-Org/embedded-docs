# LTXVImgToVideoInplace

LTXVImgToVideoInplace düğümü, bir giriş görüntüsünü ilk karelerine kodlayarak bir video gizil temsilini koşullandırır. Bir VAE kullanarak görüntüyü gizil uzaya kodlar ve belirtilen bir güç değerine göre mevcut gizil örneklerle harmanlar. Bu sayede bir görüntü, video üretimi için başlangıç noktası veya koşullandırma sinyali olarak kullanılabilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Giriş görüntüsünü gizil uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `görüntü` | Kodlanacak ve video gizilini koşullandırmak için kullanılacak giriş görüntüsü. | IMAGE | Evet | - |
| `latent` | Değiştirilecek hedef video gizil temsili. | LATENT | Evet | - |
| `güç` | Kodlanmış görüntünün gizile harmanlanma gücünü kontrol eder. 1.0 değeri ilk kareleri tamamen değiştirirken, daha düşük değerler harmanlama yapar. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `atla` | Koşullandırmayı atlar. Etkinleştirildiğinde, düğüm giriş gizilini değiştirmeden döndürür. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** `image`, `latent` girişinin genişlik ve yüksekliğine bağlı olarak, `vae` tarafından kodlama için gereken uzamsal boyutlara otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Değiştirilmiş video gizil temsili. Güncellenmiş örnekleri ve ilk karelere koşullandırma gücünü uygulayan bir `noise_mask` içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/tr.md)

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
