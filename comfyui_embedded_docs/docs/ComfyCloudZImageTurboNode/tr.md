# ComfyCloudZImageTurboNode

Bu düğüm, yalnızca 8 adımda tamamlanan Z-Image Turbo modelini kullanarak bir metin isteminden görüntü üretir. Üretim, Comfy Cloud GPU'larında uzaktan çalışır ve GPU süresine göre faturalandırılır; bu da onu görüntü fikirleri üzerinde yineleme yapmak için buradaki en hızlı ve en ucuz seçeneklerden biri yapar. Üretim tamamlandığında, düğüm iş akışınızda kullanmak üzere bitmiş görüntüyü indirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü açıklayan metin istemi. Çok satırlı girdiyi destekler ve gönderimden önce kırpılır. Kırpma sonrasında boş olmamalıdır. | STRING | Evet | 1 - 4096 karakter |
| `seed` | Üretim tekrarlanabilirliğini kontrol etmek için kullanılan rastgele tohum değeri. Değiştirilmesi farklı bir varyasyon üretir. Üretim sonrası kontrol seçeneği içerir. Varsayılan: 42. | INT | Hayır | 0 - 18446744073709551615 |
| `aspect_ratio` | Oluşturulan görüntünün en-boy oranı. Varsayılan: "1:1". | COMBO | Hayır | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Toplam piksel bütçesi. 1.0, kare en-boy oranında yaklaşık 1024x1024'tür. Varsayılan: 1.0. | FLOAT | Hayır | 0.1 - 16.0<br>(0.1 adım) |

Not: Üretim gönderilmeden önce girdi değerleri doğrulanır. `prompt`, boşluklar temizlendikten sonra 1 ile 4096 karakter arasında olmalı; `aspect_ratio`, listelenen seçeneklerden biri olmalı ve `megapixels` 0.1'lik artışlarla girilmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görüntü, daha sonraki görüntü işleme veya kaydetme düğümleri için hazır bir görüntü tensörü olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/tr.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`
