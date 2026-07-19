# Görüntü Yükle (Maske olarak)

LoadImageMask düğümü, belirtilen bir yoldan görüntüleri ve bunlara ait maskeleri yüklemek, bunları daha ileri düzey görüntü işleme veya analiz görevleriyle uyumlu hale getirmek için işlemek üzere tasarlanmıştır. Maskeleme için alfa kanalının varlığı gibi çeşitli görüntü formatlarını ve koşullarını ele alır ve görüntüleri ve maskeleri standart bir formata dönüştürerek sonraki işlemlere hazırlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' parametresi, yüklenecek ve işlenecek görüntü dosyasını belirtir. Maske çıkarma ve format dönüştürme için kaynak görüntüyü sağlayarak çıktının belirlenmesinde önemli bir rol oynar. | COMBO[STRING] |
| `kanal` | 'channel' parametresi, maskeyi oluşturmak için kullanılacak görüntünün renk kanalını belirtir. Bu, farklı renk kanallarına dayalı olarak maske oluşturmada esneklik sağlayarak düğümün çeşitli görüntü işleme senaryolarındaki kullanışlılığını artırır. | COMBO[STRING] |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `mask` | Bu düğüm, belirtilen görüntü ve kanaldan oluşturulan, görüntü işleme görevlerinde daha ileri düzey işlemler için uygun, standart bir formatta hazırlanmış maskeyi çıktı olarak verir. | `MASK` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/tr.md)
