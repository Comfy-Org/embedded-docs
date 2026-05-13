> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/tr.md)

Bu düğüm, sürekli EDM (Enerji Tabanlı Difüzyon Modelleri) örnekleme tekniklerini entegre ederek bir modelin örnekleme yeteneklerini geliştirmek için tasarlanmıştır. Modelin örnekleme sürecindeki gürültü seviyelerinin dinamik olarak ayarlanmasına olanak tanıyarak, üretim kalitesi ve çeşitliliği üzerinde daha hassas bir kontrol sunar.

## Girişler

| Parametre    | Veri Türü | Python dtype        | Açıklama |
|--------------|--------------|----------------------|-------------|
| `model`      | `MODEL`      | `torch.nn.Module`   | Sürekli EDM örnekleme yetenekleriyle geliştirilecek model. Gelişmiş örnekleme tekniklerinin uygulanması için temel oluşturur. |
| `sampling`   | COMBO[STRING] | `str`             | Uygulanacak örnekleme türünü belirtir: epsilon örneklemesi için 'eps' veya hız tahmini için 'v_prediction'. Örnekleme sürecinde modelin davranışını etkiler. |
| `sigma_max`  | `FLOAT`      | `float`             | Gürültü seviyesi için maksimum sigma değeri. Örnekleme sırasında gürültü enjeksiyon sürecinde üst sınır kontrolü sağlar. |
| `sigma_min`  | `FLOAT`      | `float`             | Gürültü seviyesi için minimum sigma değeri. Gürültü enjeksiyonu için alt sınırı belirleyerek modelin örnekleme hassasiyetini etkiler. |

## Çıkışlar

| Parametre | Veri Türü | Python dtype        | Açıklama |
|-----------|-------------|----------------------|-------------|
| `model`   | MODEL       | `torch.nn.Module`   | Entegre sürekli EDM örnekleme yetenekleriyle geliştirilmiş model. Üretim görevlerinde kullanıma hazırdır. |