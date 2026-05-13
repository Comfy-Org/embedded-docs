> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/tr.md)

SDTurboScheduler, görüntü örneklemesi için bir sigma değerleri dizisi oluşturmak üzere tasarlanmıştır; bu dizi, belirtilen arındırma seviyesine ve adım sayısına göre ayarlanır. Bu sigma değerlerini üretmek için belirli bir modelin örnekleme yeteneklerinden yararlanır ve bu değerler, görüntü oluşturma sırasında arındırma sürecini kontrol etmek için kritik öneme sahiptir.

## Girişler

| Parametre | Veri Türü | Açıklama |
| --- | --- | --- |
| `model` | `MODEL` | Model parametresi, sigma değeri üretimi için kullanılacak üretici modeli belirtir. Zamanlayıcının belirli örnekleme davranışını ve yeteneklerini belirlemede kritiktir. |
| `steps` | `INT` | Adımlar parametresi, oluşturulacak sigma dizisinin uzunluğunu belirler ve arındırma sürecinin ayrıntı düzeyini doğrudan etkiler. |
| `denoise` | `FLOAT` | Arındırma parametresi, sigma dizisinin başlangıç noktasını ayarlayarak görüntü oluşturma sırasında uygulanan arındırma seviyesi üzerinde daha hassas kontrol sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Belirtilen model, adımlar ve arındırma seviyesine göre oluşturulan sigma değerleri dizisi. Bu değerler, görüntü oluşturmada arındırma sürecini kontrol etmek için gereklidir. |