> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/tr.md)

ConditioningConcat düğümü, koşullandırma vektörlerini birleştirmek üzere tasarlanmıştır; özellikle 'conditioning_from' vektörünü 'conditioning_to' vektörüyle birleştirir. Bu işlem, iki kaynaktan gelen koşullandırma bilgisinin tek bir birleşik temsilde birleştirilmesi gereken senaryolarda temel bir öneme sahiptir.

## Girdiler

| Parametre            | Comfy dtype        | Açıklama |
|-----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | 'conditioning_from' vektörlerinin ekleneceği birincil koşullandırma vektörleri kümesini temsil eder. Birleştirme işlemi için temel oluşturur. |
| `conditioning_from`   | `CONDITIONING`     | 'conditioning_to' vektörlerine eklenecek olan koşullandırma vektörlerinden oluşur. Bu parametre, mevcut kümeye ek koşullandırma bilgilerinin entegre edilmesine olanak tanır. |

## Çıktılar

| Parametre            | Comfy dtype        | Açıklama |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | Çıktı, 'conditioning_from' vektörlerinin 'conditioning_to' vektörlerine eklenmesi sonucu oluşan, birleşik bir koşullandırma vektörleri kümesidir. |