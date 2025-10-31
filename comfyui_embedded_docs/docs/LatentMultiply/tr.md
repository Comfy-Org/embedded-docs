> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/tr.md)

LatentMultiply düğümü, örneklerin gizli temsilini belirtilen bir çarpanla ölçeklendirmek için tasarlanmıştır. Bu işlem, gizli uzay içindeki özelliklerin yoğunluğunun veya büyüklüğünün ayarlanmasına olanak tanıyarak, üretilen içeriğin ince ayarını yapmayı veya belirli bir gizli yöndeki çeşitlemelerin keşfedilmesini sağlar.

## Girdiler

| Parametre    | Veri Türü   | Açıklama |
|--------------|-------------|-------------|
| `örnekler`    | `LATENT`    | 'samples' parametresi, ölçeklendirilecek gizli temsilleri ifade eder. Çarpma işleminin gerçekleştirileceği girdi verisini tanımlamak için çok önemlidir. |
| `çarpan` | `FLOAT`     | 'multiplier' parametresi, gizli örneklere uygulanacak ölçeklendirme faktörünü belirtir. Gizli özelliklerin büyüklüğünü ayarlayarak, üretilen çıktı üzerinde nüanslı kontrol sağlamada kilit rol oynar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen çarpanla ölçeklendirilmiş, girdi gizli örneklerinin değiştirilmiş bir versiyonudur. Bu, gizli uzay içindeki çeşitlemelerin, özelliklerinin yoğunluğunu ayarlayarak keşfedilmesine olanak tanır. |