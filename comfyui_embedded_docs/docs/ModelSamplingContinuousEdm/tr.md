> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/tr.md)

Bu düğüm, sürekli EDM (Enerji Tabanlı Yayılım Modelleri) örnekleme tekniklerini entegre ederek bir modelin örnekleme yeteneklerini geliştirmek üzere tasarlanmıştır. Modelin örnekleme sürecindeki gürültü seviyelerinin dinamik olarak ayarlanmasına olanak tanıyarak, üretim kalitesi ve çeşitliliği üzerinde daha hassas bir kontrol sunar.

## Girdiler

| Parametre   | Veri Türü   | Python dtype        | Açıklama |
|-------------|-------------|---------------------|-------------|
| `model`     | `MODEL`     | `torch.nn.Module`   | Sürekli EDM örnekleme yetenekleri ile geliştirilecek model. Gelişmiş örnekleme tekniklerinin uygulanması için temel oluşturur. |
| `sampling`  | COMBO[STRING] | `str`             | Uygulanacak örnekleme türünü belirtir; örnekleme sürecinde modelin davranışını etkileyen, epsilon örneklemesi için 'eps' veya hız tahmini için 'v_prediction' değerini alır. |
| `sigma_max` | `FLOAT`     | `float`             | Örnekleme sırasındaki gürültü enjeksiyonu sürecinde üst sınır kontrolüne olanak tanıyan, gürültü seviyesi için maksimum sigma değeri. |
| `sigma_min` | `FLOAT`     | `float`             | Gürültü enjeksiyonu için alt sınırı belirleyen ve böylece modelin örnekleme hassasiyetini etkileyen, gürültü seviyesi için minimum sigma değeri. |

## Çıktılar

| Parametre | Veri Türü | Python dtype        | Açıklama |
|-----------|-------------|---------------------|-------------|
| `model`   | MODEL     | `torch.nn.Module`   | Entegre sürekli EDM örnekleme yeteneklerine sahip, geliştirilmiş model; üretim görevlerinde kullanıma hazır. |