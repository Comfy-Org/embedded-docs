> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/tr.md)

`ImageCompositeMasked` düğümü, görüntüleri birleştirmek için tasarlanmıştır ve bir kaynak görüntünün belirli koordinatlarda bir hedef görüntünün üzerine yerleştirilmesine, isteğe bağlı olarak yeniden boyutlandırma ve maskeleme imkanı sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `destination` | `IMAGE` | Kaynak görüntünün üzerine yerleştirileceği hedef görüntü. Birleştirme işlemi için arka planı oluşturur. |
| `source` | `IMAGE` | Hedef görüntünün üzerine yerleştirilecek kaynak görüntü. Bu görüntü, isteğe bağlı olarak hedef görüntünün boyutlarına sığacak şekilde yeniden boyutlandırılabilir. |
| `x` | `INT` | Kaynak görüntünün sol üst köşesinin, hedef görüntüde yerleştirileceği x koordinatı. |
| `y` | `INT` | Kaynak görüntünün sol üst köşesinin, hedef görüntüde yerleştirileceği y koordinatı. |
| `resize_source` | `BOOLEAN` | Kaynak görüntünün hedef görüntünün boyutlarına sığacak şekilde yeniden boyutlandırılıp boyutlandırılmayacağını belirten bir boolean bayrağı. |
| `mask` | `MASK` | Kaynak görüntünün hangi kısımlarının hedef görüntüye birleştirileceğini belirten isteğe bağlı bir maske. Bu, karıştırma veya kısmi yerleştirmeler gibi daha karmaşık birleştirme işlemlerine olanak tanır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image` | `IMAGE` | Birleştirme işlemi sonrasında, her iki görüntünün de unsurlarını bir araya getiren sonuç görüntüsü. |