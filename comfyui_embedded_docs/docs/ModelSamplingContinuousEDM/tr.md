# ModelÖrneklemeSürekliEDM

Bu düğüm, sürekli EDM (Enerji Tabanlı Difüzyon Modelleri) örnekleme tekniklerini entegre ederek bir modelin örnekleme yeteneklerini geliştirmek için tasarlanmıştır. Modelin örnekleme sürecindeki gürültü seviyelerinin dinamik olarak ayarlanmasına olanak tanıyarak, üretim kalitesi ve çeşitliliği üzerinde daha hassas bir kontrol sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Python dtype |
| --- | --- | --- | --- |
| `model` | Sürekli EDM örnekleme yetenekleriyle geliştirilecek model. Gelişmiş örnekleme tekniklerinin uygulanması için temel oluşturur. | `MODEL` | `torch.nn.Module` |
| `örnekleme` | Uygulanacak örnekleme türünü belirtir: epsilon örneklemesi için 'eps' veya hız tahmini için 'v_prediction'. Örnekleme sürecinde modelin davranışını etkiler. | COMBO[STRING] | `str` |
| `sigma_maks` | Gürültü seviyesi için maksimum sigma değeri. Örnekleme sırasında gürültü enjeksiyon sürecinde üst sınır kontrolü sağlar. | `FLOAT` | `float` |
| `sigma_min` | Gürültü seviyesi için minimum sigma değeri. Gürültü enjeksiyonu için alt sınırı belirleyerek modelin örnekleme hassasiyetini etkiler. | `FLOAT` | `float` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü | Python dtype |
| --- | --- | --- | --- |
| `model` | Entegre sürekli EDM örnekleme yetenekleriyle geliştirilmiş model. Üretim görevlerinde kullanıma hazırdır. | MODEL | `torch.nn.Module` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/tr.md)
