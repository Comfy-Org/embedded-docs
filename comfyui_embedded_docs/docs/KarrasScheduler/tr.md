> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/tr.md)

KarrasScheduler düğümü, Karras ve diğerlerinin (2022) gürültü zamanlamasına dayalı olarak bir gürültü seviyeleri (sigmas) dizisi oluşturmak için tasarlanmıştır. Bu zamanlayıcı, üretim modellerindeki difüzyon sürecini kontrol etmek için kullanışlı olup, üretim sürecinin her adımında uygulanan gürültü seviyelerine ince ayarlı düzenlemeler yapılmasına olanak tanır.

## Girdiler

| Parametre   | Veri Türü | Açıklama                                                                                      |
|-------------|-------------|------------------------------------------------------------------------------------------------|
| `steps`     | INT         | Gürültü zamanlamasındaki adım sayısını belirtir, oluşturulan sigmas dizisinin ayrıntı düzeyini etkiler. |
| `sigma_max` | FLOAT       | Gürültü zamanlamasındaki maksimum sigma değeri, gürültü seviyelerinin üst sınırını belirler.                    |
| `sigma_min` | FLOAT       | Gürültü zamanlamasındaki minimum sigma değeri, gürültü seviyelerinin alt sınırını belirler.                    |
| `rho`       | FLOAT       | Gürültü zamanlama eğrisinin şeklini kontrol eden bir parametredir, gürültü seviyelerinin sigma_min'den sigma_max'ya nasıl ilerlediğini etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
|-----------|-------------|-----------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | Karras ve diğerlerinin (2022) gürültü zamanlamasını izleyen oluşturulmuş gürültü seviyeleri (sigmas) dizisi. |