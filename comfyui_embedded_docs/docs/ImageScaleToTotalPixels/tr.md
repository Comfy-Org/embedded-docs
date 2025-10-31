> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/tr.md)

ImageScaleToTotalPixels düğümü, görüntüleri en-boy oranını koruyarak belirli bir toplam piksel sayısına yeniden boyutlandırmak için tasarlanmıştır. İstenen piksel sayısına ulaşmak için görüntüyü yukarı ölçeklendirmek üzere çeşitli yöntemler sunar.

## Girdiler

| Parametre       | Veri Türü    | Açıklama                                                                |
|-----------------|-------------|----------------------------------------------------------------------------|
| `image`         | `IMAGE`     | Belirtilen toplam piksel sayısına yükseltilecek olan girdi görüntüsü.    |
| `upscale_method`| COMBO[STRING] | Görüntüyü yukarı ölçeklendirmek için kullanılan yöntem. Bu, yükseltilmiş görüntünün kalitesini ve özelliklerini etkiler. |
| `megapixels`    | `FLOAT`     | Görüntünün megapiksel cinsinden hedef boyutu. Bu, yükseltilmiş görüntüdeki toplam piksel sayısını belirler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                           |
|-----------|-------------|-----------------------------------------------------------------------|
| `image`   | `IMAGE`     | Orijinal en-boy oranı korunarak, belirtilen toplam piksel sayısına sahip yükseltilmiş görüntü. |