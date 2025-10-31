> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/tr.md)

Bu düğüm, gelişmiş model birleştirme işlemleri için tasarlanmıştır ve özellikle bir modelin parametrelerini belirtilen bir çarpan değerine göre başka bir modelden çıkarmak için kullanılır. Bir modelin parametrelerinin diğeri üzerindeki etkisini ayarlayarak model davranışlarının özelleştirilmesine olanak tanır ve bu sayede yeni, hibrit modellerin oluşturulmasını kolaylaştırır.

## Girdiler

| Parametre     | Veri Türü | Açıklama |
|---------------|-----------|-------------|
| `model1`      | `MODEL`   | Parametrelerin çıkarılacağı temel model. |
| `model2`      | `MODEL`   | Temel modelden çıkarılacak parametrelere sahip model. |
| `çarpan`  | `FLOAT`   | Temel modelin parametreleri üzerindeki çıkarma etkisini ölçeklendiren kayan noktalı değer. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `model`   | MODEL     | Bir modelin parametrelerini diğerinden çıkarıp çarpan değeri ile ölçeklendirdikten sonra elde edilen model. |