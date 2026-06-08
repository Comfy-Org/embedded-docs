LatentCompositeMasked düğümü, iki gizli temsilin (latent representation) belirtilen koordinatlarda, isteğe bağlı olarak bir maske kullanılarak daha kontrollü bir şekilde harmanlanması için tasarlanmıştır. Bu düğüm, bir görüntünün parçalarını başka bir görüntünün üzerine yerleştirerek ve kaynak görüntüyü mükemmel uyum için yeniden boyutlandırma imkanı sunarak karmaşık gizli görüntülerin oluşturulmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `hedef` | Üzerine başka bir gizli temsilin yerleştirileceği temel gizli temsili ifade eder. Birleştirme işlemi için alt katman görevi görür. | `LATENT` |
| `kaynak` | Hedef (destination) üzerine yerleştirilecek olan gizli temsili ifade eder. Bu kaynak katman, belirtilen parametrelere göre yeniden boyutlandırılabilir ve konumlandırılabilir. | `LATENT` |
| `x` | Kaynağın yerleştirileceği hedef gizli temsilindeki x koordinatını belirtir. Kaynak katmanın hassas bir şekilde konumlandırılmasını sağlar. | `INT` |
| `y` | Kaynağın yerleştirileceği hedef gizli temsilindeki y koordinatını belirtir ve doğru bindirme konumlandırmasına olanak tanır. | `INT` |
| `kaynağı_yeniden_boyutlandır` | Kaynak gizli temsilinin, birleştirme öncesinde hedefin boyutlarına uyacak şekilde yeniden boyutlandırılıp boyutlandırılmayacağını belirten bir boolean bayrağıdır. | `BOOLEAN` |
| `maske` | Kaynağın hedef üzerine harmanlanmasını kontrol etmek için kullanılabilecek isteğe bağlı bir maskedir. Maske, nihai birleşimde kaynağın hangi bölümlerinin görünür olacağını tanımlar. | `MASK` |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Kaynağın hedef üzerine, potansiyel olarak seçici harmanlama için bir maske kullanılarak birleştirilmesi sonucu elde edilen gizli temsildir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/tr.md)
