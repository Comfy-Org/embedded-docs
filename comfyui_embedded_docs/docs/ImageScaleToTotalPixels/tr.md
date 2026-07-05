# Görüntüyü Toplam Piksele Göre Ölçekle

ImageScaleToTotalPixels düğümü, görüntüleri en-boy oranını koruyarak belirtilen toplam piksel sayısına yeniden boyutlandırmak için tasarlanmıştır. İstenen piksel sayısına ulaşmak için görüntüyü büyütmek üzere çeşitli yöntemler sunar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Belirtilen toplam piksel sayısına büyütülecek giriş görüntüsü. | `IMAGE` |
| `büyütme_yöntemi` | Görüntüyü büyütmek için kullanılan yöntem. Büyütülmüş görüntünün kalitesini ve özelliklerini etkiler. | COMBO[STRING] |
| `megapiksel` | Görüntünün megapiksel cinsinden hedef boyutu. Büyütülmüş görüntüdeki toplam piksel sayısını belirler. | `FLOAT` |


| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Orijinal en-boy oranını koruyarak, belirtilen toplam piksel sayısına sahip büyütülmüş görüntü. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/tr.md)
