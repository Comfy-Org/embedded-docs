# ModelBirleştirmeÇıkarma

Bu düğüm, gelişmiş model birleştirme işlemleri için tasarlanmış olup, özellikle bir modelin parametrelerini belirtilen bir çarpan doğrultusunda diğer modelden çıkarmaya yarar. Bir modelin parametrelerinin diğeri üzerindeki etkisini ayarlayarak model davranışlarının özelleştirilmesini sağlar ve yeni, hibrit modellerin oluşturulmasını kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model1` | Parametrelerin çıkarılacağı temel model. | `MODEL` |
| `model2` | Parametreleri temel modelden çıkarılacak olan model. | `MODEL` |
| `çarpan` | Temel modelin parametreleri üzerindeki çıkarma etkisini ölçekleyen ondalıklı sayı değeri. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Bir modelin parametrelerinin diğer modelden çıkarılması ve çarpan ile ölçeklenmesi sonucu elde edilen model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/tr.md)
