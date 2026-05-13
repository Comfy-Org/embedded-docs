> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/tr.md)

LatentMultiply düğümü, örneklerin gizli (latent) temsillerini belirtilen bir çarpanla ölçeklendirmek için tasarlanmıştır. Bu işlem, gizli uzaydaki özelliklerin yoğunluğunu veya büyüklüğünü ayarlamaya olanak tanıyarak, oluşturulan içeriğin ince ayarını yapmayı veya belirli bir gizli yön içindeki varyasyonları keşfetmeyi sağlar.

## Girişler

| Parametre    | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `örnekler`    | `LATENT`    | 'samples' parametresi, ölçeklendirilecek gizli temsilleri temsil eder. Çarpma işleminin gerçekleştirileceği giriş verilerini tanımlamak için kritik öneme sahiptir. |
| `çarpan` | `FLOAT`     | 'multiplier' parametresi, gizli örneklere uygulanacak ölçeklendirme faktörünü belirtir. Gizli özelliklerin büyüklüğünü ayarlamada önemli bir rol oynar ve oluşturulan çıktı üzerinde ince ayarlı kontrol sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen çarpanla ölçeklendirilmiş, giriş gizli örneklerinin değiştirilmiş bir sürümüdür. Bu, özelliklerinin yoğunluğunu ayarlayarak gizli uzay içindeki varyasyonların keşfedilmesine olanak tanır. |