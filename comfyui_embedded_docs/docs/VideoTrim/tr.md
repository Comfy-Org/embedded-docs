# VideoTrim

Bu düğüm, başlangıç zamanı ve bir süre belirleyerek videoyu seçilen bir zaman penceresine göre kırpar. Ayrıca, istenen süre elde edilemediğinde hata veren katı bir mod sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Kırpılacak video. | VIDEO | Evet | — |
| `trim` | Başlangıç/bitiş karelerini kullanan kırpma penceresi. Pencere, videonun başlangıcından itibaren saniye cinsinden bir başlangıç zamanına ve saniye cinsinden bir süreye dönüştürülür. Hem başlangıç zamanı hem de süre 0 olduğunda, video herhangi bir kırpma yapılmadan döndürülür. | VIDEO_EDIT | Evet | start_time: >= 0, default 0<br>duration: >= 0, default 0 |
| `strict_duration` | True ise, belirtilen süre mümkün olmadığında bir hata verilir. (varsayılan: False) | BOOLEAN | Hayır | true<br>false |

Not: Kırpma süresi >= 0 olmalıdır; negatif değerler hata verir. İstenen kırpma penceresi, kaynak videonun içine sığmalıdır. Kırpma uygulanamazsa, kaynak süresini, başlangıç zamanını ve hedef süreyi bildiren bir hata verilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Kırpılmış video. Kırpma penceresi boş olduğunda (başlangıç zamanı ve süre ikisi de 0 olduğunda), orijinal video değiştirilmeden döndürülür. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/tr.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`
