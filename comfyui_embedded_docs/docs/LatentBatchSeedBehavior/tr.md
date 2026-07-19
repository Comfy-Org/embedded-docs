# GizliTopluTohumDavranışı

LatentBatchSeedBehavior düğümü, bir grup gizli (latent) örneğin tohum (seed) davranışını değiştirmek için tasarlanmıştır. Bu düğüm, tohumu grup genelinde rastgeleleştirmeye veya sabitlemeye olanak tanıyarak, üretilen çıktılarda çeşitlilik sağlama veya tutarlılığı koruma yoluyla üretim sürecini etkiler.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | 'samples' parametresi, işlenecek gizli örnek grubunu temsil eder. Bu parametredeki değişiklik, seçilen tohum davranışına bağlıdır ve üretilen çıktıların tutarlılığını veya çeşitliliğini etkiler. | `LATENT` |
| `tohum_davranışı` | 'seed_behavior' parametresi, gizli örnek grubu için tohumun rastgeleleştirilip rastgeleleştirilmeyeceğini veya sabitlenip sabitlenmeyeceğini belirler. Bu seçim, grup genelinde çeşitlilik sağlayarak veya tutarlılığı garanti ederek üretim sürecini önemli ölçüde etkiler. | COMBO[STRING] |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıktı, belirtilen tohum davranışına göre ayarlamalar yapılmış, giriş gizli örneklerinin değiştirilmiş bir sürümüdür. Seçilen tohum davranışını yansıtmak için grup indeksini ya korur ya da değiştirir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/tr.md)
