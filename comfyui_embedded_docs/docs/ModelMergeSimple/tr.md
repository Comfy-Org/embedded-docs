# BasitModelBirleştirme

ModelMergeSimple düğümü, iki modelin parametrelerini belirtilen bir orana göre harmanlayarak birleştirmek için tasarlanmıştır. Bu düğüm, her iki girdi modelinin güçlü yönlerini veya özelliklerini birleştiren hibrit modellerin oluşturulmasını kolaylaştırır.

`ratio` parametresi, iki model arasındaki harmanlama oranını belirler. Bu değer 1 olduğunda çıktı modeli %100 `model1`, 0 olduğunda ise çıktı modeli %100 `model2` olur.

## Girdiler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model1` | Birleştirilecek ilk model. İkinci modelden gelen yamaların uygulandığı temel model olarak işlev görür. | `MODEL` |
| `model2` | Yamaları belirtilen orana bağlı olarak ilk modele uygulanan ikinci model. | `MODEL` |
| `oran` | Bu değer 1 olduğunda çıktı modeli %100 `model1`, 0 olduğunda ise çıktı modeli %100 `model2` olur. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen orana göre her iki girdi modelinden öğeler içeren, birleştirilmiş sonuç modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/tr.md)
