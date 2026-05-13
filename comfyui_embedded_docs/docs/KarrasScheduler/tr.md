> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/tr.md)

KarrasScheduler düğümü, Karras ve diğerleri (2022) gürültü planlamasına dayalı bir dizi gürültü seviyesi (sigma) oluşturmak için tasarlanmıştır. Bu planlayıcı, üretken modellerdeki yayılma sürecini kontrol etmek için kullanışlıdır ve üretim sürecinin her adımında uygulanan gürültü seviyelerinde ince ayarlı düzenlemeler yapılmasına olanak tanır.

## Girişler

| Parametre   | Veri Türü | Açıklama                                                                                      |
|-------------|-------------|------------------------------------------------------------------------------------------------|
| `adımlar`     | INT         | Gürültü planlamasındaki adım sayısını belirtir; oluşturulan sigma dizisinin ayrıntı düzeyini etkiler. |
| `sigma_maks` | FLOAT       | Gürültü planlamasındaki maksimum sigma değeridir; gürültü seviyelerinin üst sınırını belirler.                    |
| `sigma_min` | FLOAT       | Gürültü planlamasındaki minimum sigma değeridir; gürültü seviyelerinin alt sınırını belirler.                    |
| `rho`       | FLOAT       | Gürültü planlaması eğrisinin şeklini kontrol eden bir parametredir; gürültü seviyelerinin sigma_min'den sigma_max'a nasıl ilerlediğini etkiler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | Karras ve diğerleri (2022) gürültü planlamasını takip eden oluşturulmuş gürültü seviyeleri (sigma) dizisidir. |