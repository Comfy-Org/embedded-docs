# Wan 3.0 Görüntüden Videoya

Bu düğüm, Wan 3.0 modelini kullanarak bir ilk kare görüntüsünden video oluşturur. İsteğe bağlı olarak videonun nasıl biteceğini kontrol etmek için bir son kare görüntüsü sağlayabilirsiniz; model daha sonra ilk kareden son kareye geçiş yapan bir video oluşturur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak Wan 3.0 model varyantını seçer ve aşağıda hangi modele özgü ayarların gösterileceğini belirler. | DYNAMIC_COMBO | Evet | "wan3.0-video"<br>"wan3.0-video-prime" |
| `first_frame` | İlk kare görüntüsü. Tam olarak bir görüntü gereklidir. | IMAGE | Evet | Tek görüntü |
| `last_frame` | Son kare görüntüsü. Model, ilk kareden son kareye geçiş yapan bir video oluşturur. İsteğe bağlıdır; sağlanırsa tam olarak bir görüntü gereklidir. | IMAGE | Hayır | Tek görüntü |
| `seed` | Oluşturma için kullanılacak tohum (varsayılan: 42). | INT | Evet | 0 - 2147483647 |
| `watermark` | Sonuca yapay zekâ tarafından oluşturulan bir filigran eklenip eklenmeyeceği (varsayılan: false). | BOOLEAN | Evet | true<br>false |

### wan3.0-video ve wan3.0-video-prime Girdileri

Bu modele özgü ayarlar, her iki model seçeneğinde ortaktır ve bir model seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler. Boş bırakılabilir (varsayılan: boş). | STRING | Evet | 20.000 karaktere kadar |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Çıktı videosunun en-boy oranı. "adaptive" ile çıktı boyutları ilk kareden türetilir. | COMBO | Evet | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Çıktı süresi saniye cinsinden. "auto" ile model, isteme uyan bir süre seçer. | COMBO | Evet | "auto"<br>"2" - "30" |
| `audio` | Çıktı videosunun bir ses parçası içerip içermeyeceği (varsayılan: true). | BOOLEAN | Evet | true<br>false |
| `prompt_extend` | İstemin yapay zekâ yardımıyla geliştirilip geliştirilmeyeceği (varsayılan: true). | BOOLEAN | Evet | true<br>false |

Not: Düğüm tam olarak bir `first_frame` görüntüsü ve isteğe bağlı olarak bir `last_frame` görüntüsü kabul eder. Girdilerden herhangi birine birden fazla görüntü bağlanırsa bir hata oluşturulur. `last_frame` sağlandığında, oluşturulan video ilk kareden son kareye geçiş yapar. `prompt` 20.000 karakter ile sınırlıdır. Bir çalıştırmanın fiyatı seçilen `model`, `resolution` ve `duration` değerlerine bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video. `audio` seçeneği etkinleştirildiğinde bir ses parçası içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/tr.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
