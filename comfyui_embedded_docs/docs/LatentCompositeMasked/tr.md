> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/tr.md)

LatentCompositeMasked düğümü, iki gizli temsili belirtilen koordinatlarda birleştirmek ve isteğe bağlı olarak daha kontrollü bir birleştirme için maske kullanmak üzere tasarlanmıştır. Bu düğüm, bir görüntünün parçalarını başka bir görüntünün üzerine, kaynak görüntüyü mükemmel bir uyum için yeniden boyutlandırma yeteneğiyle yerleştirerek karmaşık gizli görüntüler oluşturmayı sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `hedef` | `LATENT`    | Üzerine başka bir gizli temsilin birleştirileceği gizli temsil. Birleştirme işlemi için temel katman olarak işlev görür. |
| `kaynak` | `LATENT`    | Hedef üzerine birleştirilecek gizli temsil. Bu kaynak katman, belirtilen parametrelere göre yeniden boyutlandırılabilir ve konumlandırılabilir. |
| `x` | `INT`       | Kaynağın yerleştirileceği, hedef gizli temsil içindeki x koordinatı. Kaynak katmanın hassas konumlandırılmasına olanak tanır. |
| `y` | `INT`       | Kaynağın yerleştirileceği, hedef gizli temsil içindeki y koordinatı. Doğru yerleştirme pozisyonu sağlar. |
| `kaynağı_yeniden_boyutlandır` | `BOOLEAN` | Kaynak gizli temsilin, birleştirmeden önce hedefin boyutlarına uyacak şekilde yeniden boyutlandırılıp boyutlandırılmayacağını belirten bir bayrak. |
| `maske` | `MASK`     | Kaynağın hedef üzerinde nasıl karıştırılacağını kontrol etmek için kullanılabilecek isteğe bağlı bir maske. Maske, kaynağın hangi kısımlarının nihai birleşimde görüneceğini tanımlar. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Kaynağı hedef üzerine, seçici birleştirme için potansiyel olarak bir maske kullanarak birleştirdikten sonra ortaya çıkan gizli temsil. |