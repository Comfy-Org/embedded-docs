> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/tr.md)

ModelMergeAdd düğümü, bir modelden diğerine anahtar yamalar ekleyerek iki modeli birleştirmek için tasarlanmıştır. Bu işlem, ilk modeli klonlamayı ve ardından ikinci modelden yamalar uygulamayı içerir; böylece her iki modelin özelliklerinin veya davranışlarının birleştirilmesine olanak tanır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Klonlanacak ve ikinci modelden yamaların ekleneceği ilk modeldir. Birleştirme işlemi için temel model görevi görür. |
| `model2`  | `MODEL`     | Anahtar yamaların çıkarıldığı ve ilk modele eklendiği ikinci modeldir. Birleştirilmiş modele ek özellikler veya davranışlar kazandırır. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | İkinci modelden anahtar yamaların birinci modele eklenmesiyle iki modelin birleştirilmesinin sonucudur. Bu birleştirilmiş model, her iki modelin özelliklerini veya davranışlarını bir araya getirir. |