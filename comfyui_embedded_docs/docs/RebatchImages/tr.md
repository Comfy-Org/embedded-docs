# Görüntüleri Yeniden Grupla

RebatchImages düğümü, bir grup görseli belirtilen toplu iş boyutuna göre yeniden düzenleyerek yeni bir toplu iş yapılandırması oluşturmak üzere tasarlanmıştır. Bu işlem, toplu işlemlerde görsel verilerinin yönetilmesi ve optimize edilmesi için önemlidir; görsellerin verimli bir şekilde işlenmesi amacıyla istenen toplu iş boyutuna göre gruplandırılmasını sağlar.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | Yeniden toplu işlenecek görsellerin listesi. Bu parametre, yeniden toplu işleme sürecine girecek giriş verilerini belirlemek için kritiktir. | `IMAGE` |
| `toplu_boyut` | Çıktı toplu işlerinin istenen boyutunu belirtir. Bu parametre, giriş görsellerinin nasıl gruplandırılacağını ve işleneceğini doğrudan etkileyerek çıktının yapısını şekillendirir. | `INT` |

## Çıktılar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Çıktı, belirtilen toplu iş boyutuna göre yeniden düzenlenmiş görsel toplu işlerinin bir listesinden oluşur. Bu, toplu işlemlerde görsel verilerinin esnek ve verimli bir şekilde işlenmesine olanak tanır. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/tr.md)
