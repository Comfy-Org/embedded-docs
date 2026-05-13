> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/tr.md)

Bu düğüm, gelişmiş model birleştirme işlemleri için tasarlanmış olup, özellikle bir modelin parametrelerini belirtilen bir çarpan doğrultusunda diğer modelden çıkarmaya yarar. Bir modelin parametrelerinin diğeri üzerindeki etkisini ayarlayarak model davranışlarının özelleştirilmesini sağlar ve yeni, hibrit modellerin oluşturulmasını kolaylaştırır.

## Girişler

| Parametre     | Veri Türü | Açıklama |
|---------------|--------------|-------------|
| `model1`      | `MODEL`     | Parametrelerin çıkarılacağı temel model. |
| `model2`      | `MODEL`     | Parametreleri temel modelden çıkarılacak olan model. |
| `çarpan`  | `FLOAT`     | Temel modelin parametreleri üzerindeki çıkarma etkisini ölçekleyen ondalıklı sayı değeri. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Bir modelin parametrelerinin diğer modelden çıkarılması ve çarpan ile ölçeklenmesi sonucu elde edilen model. |