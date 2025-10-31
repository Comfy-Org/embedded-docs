> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/tr.md)

ModelMergeAdd düğümü, bir modelden diğerine anahtar yamalar ekleyerek iki modeli birleştirmek için tasarlanmıştır. Bu işlem, ilk modelin klonlanmasını ve ardından ikinci modelden yamalar uygulanmasını içerir, böylece her iki modelin özelliklerinin veya davranışlarının birleştirilmesine olanak tanır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model1`  | `MODEL`     | Klonlanacak ve ikinci modelden yamaların ekleneceği ilk model. Birleştirme işlemi için temel modeli oluşturur. |
| `model2`  | `MODEL`     | Anahtar yamaların çıkarıldığı ve ilk modele eklendiği ikinci model. Birleşik modele ek özellikler veya davranışlar katar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | İkinci modelden alınan anahtar yamaların ilk modele eklenmesiyle elde edilen birleşik model. Bu birleşik model, her iki modelin özelliklerini veya davranışlarını bir araya getirir. |