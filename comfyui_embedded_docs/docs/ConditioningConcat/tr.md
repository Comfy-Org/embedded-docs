# Koşullandırma (Birleştir)

ConditioningConcat düğümü, koşullandırma vektörlerini birleştirmek, özellikle 'conditioning_from' vektörünü 'conditioning_to' vektörüne eklemek için tasarlanmıştır. Bu işlem, iki kaynaktan gelen koşullandırma bilgilerinin tek bir birleşik temsilde birleştirilmesi gereken senaryolarda temel bir rol oynar.

## Girişler

| Parametre | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `hedef_koşullandırma` | 'conditioning_from' vektörlerinin ekleneceği birincil koşullandırma vektörleri kümesini temsil eder. Birleştirme işlemi için temel görevi görür. | `CONDITIONING` |
| `kaynak_koşullandırma` | 'conditioning_to' vektörlerine eklenecek koşullandırma vektörlerinden oluşur. Bu parametre, mevcut kümeye ek koşullandırma bilgilerinin entegre edilmesini sağlar. | `CONDITIONING` |

## Çıktılar

| Parametre | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `conditioning` | Çıktı, 'conditioning_from' vektörlerinin 'conditioning_to' vektörlerine eklenmesiyle elde edilen birleşik bir koşullandırma vektörleri kümesidir. | `CONDITIONING` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/tr.md)
