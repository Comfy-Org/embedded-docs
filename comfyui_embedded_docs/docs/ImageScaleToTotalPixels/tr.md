> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/tr.md)

ImageScaleToTotalPixels düğümü, görüntüleri en-boy oranını koruyarak belirtilen toplam piksel sayısına yeniden boyutlandırmak için tasarlanmıştır. İstenen piksel sayısına ulaşmak için görüntüyü büyütmek üzere çeşitli yöntemler sunar.

## Girişler

| Parametre        | Veri Türü    | Açıklama                                                                 |
|------------------|--------------|--------------------------------------------------------------------------|
| `görüntü`          | `IMAGE`      | Belirtilen toplam piksel sayısına büyütülecek giriş görüntüsü.          |
| `büyütme_yöntemi` | COMBO[STRING] | Görüntüyü büyütmek için kullanılan yöntem. Büyütülmüş görüntünün kalitesini ve özelliklerini etkiler. |
| `megapiksel`     | `FLOAT`      | Görüntünün megapiksel cinsinden hedef boyutu. Büyütülmüş görüntüdeki toplam piksel sayısını belirler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
|-----------|-----------|--------------------------------------------------------------------------|
| `görüntü`   | `IMAGE`   | Orijinal en-boy oranını koruyarak, belirtilen toplam piksel sayısına sahip büyütülmüş görüntü. |