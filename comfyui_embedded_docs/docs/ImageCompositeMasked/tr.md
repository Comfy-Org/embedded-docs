`ImageCompositeMasked` düğümü, görüntülerin birleştirilmesi (kompozit) için tasarlanmıştır; kaynak görüntünün, hedef görüntü üzerine belirtilen koordinatlarda, isteğe bağlı yeniden boyutlandırma ve maskeleme ile yerleştirilmesine olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `hedef` | Kaynak görüntünün üzerine yerleştirileceği hedef görüntü. Birleştirme işlemi için arka plan görevi görür. | `IMAGE` |
| `kaynak` | Hedef görüntü üzerine yerleştirilecek kaynak görüntü. Bu görüntü, isteğe bağlı olarak hedef görüntünün boyutlarına uyacak şekilde yeniden boyutlandırılabilir. | `IMAGE` |
| `x` | Kaynak görüntünün sol üst köşesinin hedef görüntüde yerleştirileceği x koordinatı. | `INT` |
| `y` | Kaynak görüntünün sol üst köşesinin hedef görüntüde yerleştirileceği y koordinatı. | `INT` |
| `kaynağı_yeniden_boyutlandır` | Kaynak görüntünün, hedef görüntünün boyutlarına uyacak şekilde yeniden boyutlandırılıp boyutlandırılmayacağını belirten bir boolean bayrağı. | `BOOLEAN` |
| `maske` | Kaynak görüntünün hangi bölümlerinin hedef görüntü üzerine yerleştirileceğini belirten isteğe bağlı bir maske. Bu, karıştırma veya kısmi yerleştirme gibi daha karmaşık birleştirme işlemlerine olanak tanır. | `MASK` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Birleştirme işlemi sonucunda elde edilen, her iki görüntünün öğelerini birleştiren nihai görüntü. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/tr.md)
