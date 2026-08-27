# LTXVImgToVideoInplace

LTXVImgToVideoInplace, bir girdi görüntüsünü latent uzaya kodlar ve bu kodlanmış kareleri mevcut bir latent videonun başına yerleştirir. `strength` değeri, kodlanmış görüntünün bu ilk kareleri ne kadar güçlü koşullandırdığını kontrol eder ve `bypass` etkinleştirildiğinde girdi latent değiştirilmeden döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Girdi görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `görüntü` | Kodlanacak ve video latentini koşullandırmak için kullanılacak girdi görüntüsü. | IMAGE | Evet | - |
| `latent` | Değiştirilecek hedef latent video temsili. | LATENT | Evet | - |
| `güç` | Kodlanmış görüntünün latentin ilk karelerini ne kadar güçlü koşullandırdığını kontrol eder. 1.0 değeri ilk kareleri tamamen kodlanmış görüntüyle koşullandırırken, daha düşük değerler daha az güçlü koşullandırır. İlk kareler için gürültü maskesi `1.0 - strength` olarak ayarlanır. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 1.0 |
| `atla` | Koşullandırmayı atlar. Etkinleştirildiğinde düğüm girdi latentini değiştirmeden döndürür. (varsayılan: False) | BOOLEAN | Hayır | True or False |

**Not:** `image`, `latent` girdisinin genişlik ve yüksekliğine bağlı olarak `vae` tarafından kodlama için gereken uzamsal boyutlarla eşleşecek şekilde otomatik olarak yeniden boyutlandırılır. Görüntünün yalnızca RGB kanalları kodlama için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Ortaya çıkan latent video temsili. Bypass devre dışıyken, güncellenmiş `samples` ve koşullandırma gücünü ilk karelere uygulayan bir `noise_mask` içerir. Bypass etkinken, girdi latentinin değiştirilmeden döndürülmüş halidir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/tr.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
