> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/tr.md)

LTXVImgToVideoInplace düğümü, bir giriş görüntüsünü ilk karelerine kodlayarak bir video gizil temsilini koşullandırır. Bir VAE kullanarak görüntüyü gizil uzaya kodlar ve belirtilen bir güç değerine göre mevcut gizil örneklerle harmanlar. Bu sayede bir görüntü, video üretimi için başlangıç noktası veya koşullandırma sinyali olarak kullanılabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `vae` | VAE | Evet | - | Giriş görüntüsünü gizil uzaya kodlamak için kullanılan VAE modeli. |
| `image` | IMAGE | Evet | - | Kodlanacak ve video gizilini koşullandırmak için kullanılacak giriş görüntüsü. |
| `latent` | LATENT | Evet | - | Değiştirilecek hedef video gizil temsili. |
| `strength` | FLOAT | Hayır | 0.0 - 1.0 | Kodlanmış görüntünün gizile harmanlanma gücünü kontrol eder. 1.0 değeri ilk kareleri tamamen değiştirirken, daha düşük değerler harmanlama yapar. (varsayılan: 1.0) |
| `bypass` | BOOLEAN | Hayır | - | Koşullandırmayı atlar. Etkinleştirildiğinde, düğüm giriş gizilini değiştirmeden döndürür. (varsayılan: False) |

**Not:** `image`, `latent` girişinin genişlik ve yüksekliğine bağlı olarak, `vae` tarafından kodlama için gereken uzamsal boyutlara otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `latent` | LATENT | Değiştirilmiş video gizil temsili. Güncellenmiş örnekleri ve ilk karelere koşullandırma gücünü uygulayan bir `noise_mask` içerir. |

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
