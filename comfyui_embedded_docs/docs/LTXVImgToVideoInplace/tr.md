> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/tr.md)

LTXVImgToVideoInplace düğümü, bir giriş görüntüsünü ilk karelerine kodlayarak bir video gizli temsilini koşullandırır. Görüntüyü gizli uzaya kodlamak için bir VAE kullanır ve ardından belirtilen bir güce dayalı olarak mevcut gizli örneklerle harmanlar. Bu, bir görüntünün video oluşturma için bir başlangıç noktası veya koşullandırma sinyali olarak hizmet etmesine olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Evet | - | Giriş görüntüsünü gizli uzaya kodlamak için kullanılan VAE modeli. |
| `image` | IMAGE | Evet | - | Kodlanacak ve video gizlisini koşullandırmak için kullanılacak giriş görüntüsü. |
| `latent` | LATENT | Evet | - | Değiştirilecek hedef gizli video temsili. |
| `strength` | FLOAT | Hayır | 0.0 - 1.0 | Kodlanmış görüntünün gizliye harmanlanma gücünü kontrol eder. 1.0 değeri ilk kareleri tamamen değiştirirken, daha düşük değerler onları harmanlar. (varsayılan: 1.0) |
| `bypass` | BOOLEAN | Hayır | - | Koşullandırmayı atla. Etkinleştirildiğinde, düğüm giriş gizlisini değiştirilmeden döndürür. (varsayılan: False) |

**Not:** `image`, `latent` girişinin genişlik ve yüksekliğine dayalı olarak `vae` tarafından kodlama için gereken uzamsal boyutlarla eşleşecek şekilde otomatik olarak yeniden boyutlandırılacaktır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latent` | LATENT | Değiştirilmiş gizli video temsili. Güncellenmiş örnekleri ve koşullandırma gücünü ilk karelere uygulayan bir `noise_mask` içerir. |
