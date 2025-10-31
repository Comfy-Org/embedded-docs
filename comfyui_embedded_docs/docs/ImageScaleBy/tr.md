> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/tr.md)

ImageScaleBy düğümü, çeşitli enterpolasyon yöntemleri kullanarak görüntüleri belirli bir ölçek faktörüyle büyütmek için tasarlanmıştır. Görüntü boyutunu esnek bir şekilde ayarlamaya olanak tanır ve farklı büyütme ihtiyaçlarına hitap eder.

## Girdiler

| Parametre       | Veri Tipi    | Açıklama                                                                 |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | Büyütülecek girdi görüntüsü. Bu parametre, büyütme işlemine tabi tutulacak temel görüntüyü sağladığı için çok önemlidir. |
| `upscale_method`| COMBO[STRING] | Büyütme için kullanılacak enterpolasyon yöntemini belirtir. Yöntem seçimi, büyütülmüş görüntünün kalitesini ve özelliklerini etkileyebilir. |
| `scale_by`      | `FLOAT`     | Görüntünün büyütüleceği faktör. Bu, çıktı görüntüsünün boyutunun girdi görüntüsüne göre ne kadar artacağını belirler. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama                                                   |
|-----------|-------------|---------------------------------------------------------------|
| `image`   | `IMAGE`     | Belirtilen ölçek faktörü ve enterpolasyon yöntemine göre girdi görüntüsünden daha büyük olan büyütülmüş görüntü. |