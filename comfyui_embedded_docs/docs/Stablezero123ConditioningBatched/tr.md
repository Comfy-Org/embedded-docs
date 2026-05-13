> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/tr.md)

Bu düğüm, koşullandırma bilgilerini StableZero123 modeline özel olarak toplu bir şekilde işlemek üzere tasarlanmıştır. Toplu işlemenin kritik olduğu senaryolarda iş akışını optimize ederek, birden fazla koşullandırma veri kümesini aynı anda verimli bir şekilde işlemeye odaklanır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|----------------------|--------------|-------------|
| `clip_vision` | `CLIP_VISION` | Koşullandırma sürecine görsel bağlam sağlayan CLIP görsel yerleştirmeleri. |
| `init_image` | `IMAGE` | Üretim süreci için başlangıç noktası görevi gören, koşullandırılacak başlangıç görüntüsü. |
| `vae` | `VAE` | Koşullandırma sürecinde görüntüleri kodlamak ve kodunu çözmek için kullanılan varyasyonel otomatik kodlayıcı. |
| `width` | `INT` | Çıktı görüntüsünün genişliği. |
| `height` | `INT` | Çıktı görüntüsünün yüksekliği. |
| `batch_size` | `INT` | Tek bir toplu işlemde işlenecek koşullandırma kümesi sayısı. |
| `elevation` | `FLOAT` | 3B model koşullandırması için yükseklik açısı; oluşturulan görüntünün perspektifini etkiler. |
| `azimuth` | `FLOAT` | 3B model koşullandırması için azimut açısı; oluşturulan görüntünün yönünü etkiler. |
| `elevation_batch_increment` | `FLOAT` | Toplu işlem boyunca yükseklik açısındaki kademeli değişim; farklı perspektiflere olanak tanır. |
| `azimuth_batch_increment` | `FLOAT` | Toplu işlem boyunca azimut açısındaki kademeli değişim; farklı yönlere olanak tanır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|---------------|--------------|-------------|
| `positive` | `CONDITIONING` | Oluşturulan içerikte belirli özellikleri veya yönleri teşvik etmek için uyarlanmış pozitif koşullandırma çıktısı. |
| `negative` | `CONDITIONING` | Oluşturulan içerikte belirli özellikleri veya yönleri bastırmak için uyarlanmış negatif koşullandırma çıktısı. |
| `latent` | `LATENT` | Koşullandırma sürecinden türetilen, daha sonraki işleme veya üretim adımlarına hazır gizli temsil. |