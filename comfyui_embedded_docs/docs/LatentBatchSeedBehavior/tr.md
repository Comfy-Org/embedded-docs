> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/tr.md)

LatentBatchSeedBehavior düğümü, bir grup gizli örneğin tohum davranışını değiştirmek için tasarlanmıştır. Topluluk genelinde tohumun rastgeleleştirilmesini veya sabitlenmesini sağlayarak, oluşturulan çıktılarda ya çeşitlilik eklenmesini ya da tutarlılığın korunmasını etkiler.

## Girdiler

| Parametre       | Veri Tipi    | Açıklama |
|-----------------|--------------|-------------|
| `örnekler`       | `LATENT`     | 'samples' parametresi, işlenecek gizli örnek grubunu temsil eder. Değişikliği, seçilen tohum davranışına bağlıdır ve oluşturulan çıktıların tutarlılığını veya değişkenliğini etkiler. |
| `tohum_davranışı`  | COMBO[STRING] | 'seed_behavior' parametresi, gizli örnek grubu için tohumun rastgeleleştirilmesi mi yoksa sabitlenmesi mi gerektiğini belirler. Bu seçim, topluluk genelinde ya çeşitlilik ekleyerek ya da tutarlılığı sağlayarak oluşturma sürecini önemli ölçüde etkiler. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, girdi olarak verilen gizli örneklerin, belirtilen tohum davranışına dayalı olarak yapılan ayarlamalarla değiştirilmiş bir versiyonudur. Seçilen tohum davranışını yansıtmak için grup indeksini ya korur ya da değiştirir. |