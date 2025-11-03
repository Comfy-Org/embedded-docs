> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/tr.md)

SDTurboScheduler, görüntü örneklemesi için bir sigma değerleri dizisi oluşturmak üzere tasarlanmıştır ve diziyi, belirtilen gürültü giderme seviyesi ve adım sayısına göre ayarlar. Görüntü oluşturma sırasında gürültü giderme işlemini kontrol etmek için çok önemli olan bu sigma değerlerini üretmek amacıyla belirli bir modelin örnekleme yeteneklerinden yararlanır.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
| --- | --- | --- |
| `model` | `MODEL` | Model parametresi, sigma değeri üretimi için kullanılacak olan üretken modeli belirtir. Zamanlayıcının belirli örnekleme davranışını ve yeteneklerini belirlemede çok önemlidir. |
| `adımlar` | `INT` | Adımlar parametresi, oluşturulacak sigma dizisinin uzunluğunu belirler ve gürültü giderme işleminin detay seviyesini doğrudan etkiler. |
| `gürültü_azaltma` | `FLOAT` | Gürültü giderme parametresi, sigma dizisinin başlangıç noktasını ayarlayarak, görüntü oluşturma sırasında uygulanan gürültü giderme seviyesi üzerinde daha hassas kontrol sağlar. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Belirtilen model, adım sayısı ve gürültü giderme seviyesine dayalı olarak oluşturulmuş bir sigma değerleri dizisi. Bu değerler, görüntü oluşturmada gürültü giderme işlemini kontrol etmek için esastır. |