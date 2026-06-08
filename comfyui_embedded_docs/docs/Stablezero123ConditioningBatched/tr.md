Bu düğüm, koşullandırma bilgilerini StableZero123 modeline özel olarak toplu bir şekilde işlemek üzere tasarlanmıştır. Toplu işlemenin kritik olduğu senaryolarda iş akışını optimize ederek, birden fazla koşullandırma veri kümesini aynı anda verimli bir şekilde işlemeye odaklanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip_vision` | Koşullandırma sürecine görsel bağlam sağlayan CLIP görsel yerleştirmeleri. | `CLIP_VISION` |
| `init_image` | Üretim süreci için başlangıç noktası görevi gören, koşullandırılacak başlangıç görüntüsü. | `IMAGE` |
| `vae` | Koşullandırma sürecinde görüntüleri kodlamak ve kodunu çözmek için kullanılan varyasyonel otomatik kodlayıcı. | `VAE` |
| `width` | Çıktı görüntüsünün genişliği. | `INT` |
| `height` | Çıktı görüntüsünün yüksekliği. | `INT` |
| `batch_size` | Tek bir toplu işlemde işlenecek koşullandırma kümesi sayısı. | `INT` |
| `elevation` | 3B model koşullandırması için yükseklik açısı; oluşturulan görüntünün perspektifini etkiler. | `FLOAT` |
| `azimuth` | 3B model koşullandırması için azimut açısı; oluşturulan görüntünün yönünü etkiler. | `FLOAT` |
| `elevation_batch_increment` | Toplu işlem boyunca yükseklik açısındaki kademeli değişim; farklı perspektiflere olanak tanır. | `FLOAT` |
| `azimuth_batch_increment` | Toplu işlem boyunca azimut açısındaki kademeli değişim; farklı yönlere olanak tanır. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Oluşturulan içerikte belirli özellikleri veya yönleri teşvik etmek için uyarlanmış pozitif koşullandırma çıktısı. | `CONDITIONING` |
| `negative` | Oluşturulan içerikte belirli özellikleri veya yönleri bastırmak için uyarlanmış negatif koşullandırma çıktısı. | `CONDITIONING` |
| `latent` | Koşullandırma sürecinden türetilen, daha sonraki işleme veya üretim adımlarına hazır gizli temsil. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/tr.md)
