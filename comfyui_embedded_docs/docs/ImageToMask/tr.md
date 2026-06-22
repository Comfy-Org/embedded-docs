# Görüntüyü Maskeye Dönüştür

ImageToMask düğümü, bir görüntüyü belirtilen bir renk kanalına göre maskeye dönüştürmek için tasarlanmıştır. Bu düğüm, bir görüntünün kırmızı, yeşil, mavi veya alfa kanallarına karşılık gelen maske katmanlarının çıkarılmasını sağlayarak, kanala özgü maskeleme veya işleme gerektiren işlemleri kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' parametresi, belirtilen renk kanalına göre bir maske oluşturulacak giriş görüntüsünü temsil eder. Ortaya çıkan maskenin içeriğini ve özelliklerini belirlemede önemli bir rol oynar. | `IMAGE` |
| `kanal` | 'channel' parametresi, maskeyi oluşturmak için giriş görüntüsünün hangi renk kanalının (kırmızı, yeşil, mavi veya alfa) kullanılacağını belirtir. Bu seçim, maskenin görünümünü ve görüntünün hangi bölümlerinin vurgulanacağını veya maskeleneceğini doğrudan etkiler. | COMBO[STRING] |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `mask` | Çıktı 'maskesi', giriş görüntüsündeki belirtilen renk kanalının ikili veya gri tonlamalı bir temsilidir ve daha ileri görüntü işleme veya maskeleme işlemleri için kullanışlıdır. | `MASK` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/tr.md)
