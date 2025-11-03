> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/tr.md)

Bu düğüm, StableZero123 modeli için özel olarak tasarlanmış şekilde gruplandırılmış koşullandırma bilgilerini işlemek üzere tasarlanmıştır. Toplu işlemenin kritik olduğu senaryolar için iş akışını optimize ederek, birden fazla koşullandırma veri setinin aynı anda verimli bir şekilde işlenmesine odaklanır.

## Girdiler

| Parametre             | Veri Tipi    | Açıklama |
|----------------------|--------------|-------------|
| `clip_vision`         | `CLIP_VISION` | Koşullandırma süreci için görsel bağlam sağlayan CLIP görüntü yerleştirmeleri. |
| `init_image`          | `IMAGE`      | Üretim süreci için bir başlangıç noktası olarak hizmet eden, koşullandırılacak başlangıç görseli. |
| `vae`                 | `VAE`        | Koşullandırma sürecinde görüntüleri kodlamak ve kodunu çözmek için kullanılan varyasyonel otokodlayıcı. |
| `width`               | `INT`        | Çıktı görselinin genişliği. |
| `height`              | `INT`        | Çıktı görselinin yüksekliği. |
| `batch_size`          | `INT`        | Tek bir grup içinde işlenecek koşullandırma setlerinin sayısı. |
| `elevation`           | `FLOAT`      | 3B model koşullandırması için yükseklik açısı; oluşturulan görselin perspektifini etkiler. |
| `azimuth`             | `FLOAT`      | 3B model koşullandırması için azimut açısı; oluşturulan görselin yönelimini etkiler. |
| `elevation_batch_increment` | `FLOAT` | Grup boyunca yükseklik açısındaki artış; çeşitli perspektiflere olanak tanır. |
| `azimuth_batch_increment` | `FLOAT` | Grup boyunca azimut açısındaki artış; çeşitli yönelimlere olanak tanır. |

## Çıktılar

| Parametre     | Veri Tipi    | Açıklama |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | Oluşturulan içerikte belirli özellikleri veya yönleri desteklemek için uyarlanmış pozitif koşullandırma çıktısı. |
| `negative`    | `CONDITIONING` | Oluşturulan içerikte belirli özellikleri veya yönleri bastırmak için uyarlanmış negatif koşullandırma çıktısı. |
| `latent`      | `LATENT`     | Koşullandırma sürecinden türetilen, daha fazla işleme veya üretim adımlarına hazır olan gizli temsil. |