ModelMergeAdd düğümü, bir modelden diğerine anahtar yamalar ekleyerek iki modeli birleştirmek için tasarlanmıştır. Bu işlem, ilk modeli klonlamayı ve ardından ikinci modelden yamalar uygulamayı içerir; böylece her iki modelin özelliklerinin veya davranışlarının birleştirilmesine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model1` | Klonlanacak ve ikinci modelden yamaların ekleneceği ilk modeldir. Birleştirme işlemi için temel model görevi görür. | `MODEL` |
| `model2` | Anahtar yamaların çıkarıldığı ve ilk modele eklendiği ikinci modeldir. Birleştirilmiş modele ek özellikler veya davranışlar kazandırır. | `MODEL` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | İkinci modelden anahtar yamaların birinci modele eklenmesiyle iki modelin birleştirilmesinin sonucudur. Bu birleştirilmiş model, her iki modelin özelliklerini veya davranışlarını bir araya getirir. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/tr.md)
