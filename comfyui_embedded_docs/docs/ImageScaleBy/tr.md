> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/tr.md)

ImageScaleBy düğümü, belirtilen bir ölçek faktörü kullanarak çeşitli enterpolasyon yöntemleriyle görüntüleri büyütmek için tasarlanmıştır. Farklı büyütme ihtiyaçlarına hitap ederek görüntü boyutunun esnek bir şekilde ayarlanmasına olanak tanır.

## Girişler

| Parametre        | Veri Türü   | Açıklama                                                                 |
|------------------|-------------|--------------------------------------------------------------------------|
| `görüntü`          | `IMAGE`     | Büyütülecek giriş görüntüsü. Bu parametre, büyütme işlemine tabi tutulacak temel görüntüyü sağladığı için kritik öneme sahiptir. |
| `büyütme_yöntemi` | COMBO[STRING] | Büyütme için kullanılacak enterpolasyon yöntemini belirtir. Yöntem seçimi, büyütülmüş görüntünün kalitesini ve özelliklerini etkileyebilir. |
| `oranla_büyüt`       | `FLOAT`     | Görüntünün büyütüleceği faktör. Bu, çıktı görüntüsünün boyutundaki artışı giriş görüntüsüne göre belirler. |

## Çıktılar

| Parametre | Veri Türü   | Açıklama                                                   |
|-----------|-------------|------------------------------------------------------------|
| `görüntü`   | `IMAGE`     | Belirtilen ölçek faktörü ve enterpolasyon yöntemine göre giriş görüntüsünden daha büyük olan büyütülmüş görüntü. |