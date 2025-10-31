> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/tr.md)

İstem, giriş görüntüleri ve çıktı boyutuna dayalı olarak senkronize bir şekilde video oluşturur. Bu düğüm, video içeriğini ve yapısını tanımlamak için metin istemleri ve isteğe bağlı başlangıç/bitiş görüntüleri sağlayarak Luma API'sini kullanarak videolar oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Video oluşturma için istem (varsayılan: "") |
| `model` | COMBO | Evet | Birden fazla seçenek mevcut | Mevcut Luma modellerinden video oluşturma modelini seçer |
| `resolution` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan video için çıktı çözünürlüğü (varsayılan: 540p) |
| `duration` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan videonun süresi |
| `loop` | BOOLEAN | Evet | - | Oluşturulan videonun döngü yapıp yapmayacağı (varsayılan: False) |
| `seed` | INT | Evet | 0 ile 18446744073709551615 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohuma bakılmaksızın belirsizdir. (varsayılan: 0) |
| `first_image` | IMAGE | Hayır | - | Oluşturulan videonun ilk karesi. (isteğe bağlı) |
| `last_image` | IMAGE | Hayır | - | Oluşturulan videonun son karesi. (isteğe bağlı) |
| `luma_concepts` | CUSTOM | Hayır | - | Luma Kavramlar düğümü aracılığıyla kamera hareketini yönlendirmek için isteğe bağlı Kamera Kavramları. (isteğe bağlı) |

**Not:** `first_image` veya `last_image` parametrelerinden en az biri sağlanmalıdır. Her ikisi de eksikse düğüm bir istisna oluşturacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası |