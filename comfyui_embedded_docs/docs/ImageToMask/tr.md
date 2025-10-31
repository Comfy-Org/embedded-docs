> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/tr.md)

ImageToMask düğümü, bir görüntüyü belirli bir renk kanalına dayalı olarak maskeye dönüştürmek için tasarlanmıştır. Bir görüntünün kırmızı, yeşil, mavi veya alfa kanallarına karşılık gelen maske katmanlarının çıkarılmasına olanak tanıyarak, kanala özgü maskeleme veya işleme gerektiren operasyonları kolaylaştırır.

## Girdiler

| Parametre   | Veri Tipi   | Açıklama                                                                                                          |
|-------------|-------------|----------------------------------------------------------------------------------------------------------------------|
| `image`     | `IMAGE`     | 'image' parametresi, belirtilen renk kanalına dayalı olarak bir maske oluşturulacak girdi görüntüsünü temsil eder. Ortaya çıkan maskenin içeriğini ve özelliklerini belirlemede çok önemli bir rol oynar. |
| `channel`   | COMBO[STRING] | 'channel' parametresi, maskeyi oluşturmak için girdi görüntüsünün hangi renk kanalının (kırmızı, yeşil, mavi veya alfa) kullanılacağını belirtir. Bu seçim, maskenin görünümünü ve görüntünün hangi kısımlarının vurgulandığını veya maskelendiğini doğrudan etkiler. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Çıktı olan 'mask', girdi görüntüsünden belirtilen renk kanalının ikili veya gri tonlamalı bir temsilidir ve daha fazla görüntü işleme veya maskeleme işlemleri için kullanışlıdır. |