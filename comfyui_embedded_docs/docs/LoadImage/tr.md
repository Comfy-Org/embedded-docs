# Görüntü Yükle

LoadImage düğümü, belirtilen bir yoldan görüntüleri yüklemek ve ön işlemek için tasarlanmıştır. Çoklu kare içeren görüntü formatlarını işler, EXIF verilerine dayalı döndürme gibi gerekli dönüşümleri uygular, piksel değerlerini normalleştirir ve isteğe bağlı olarak alfa kanalına sahip görüntüler için bir maske oluşturur. Bu düğüm, görüntüleri bir iş akışı içinde daha ileri işleme veya analiz için hazırlamada önemli bir rol oynar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | 'image' parametresi, yüklenecek ve işlenecek görüntünün tanımlayıcısını belirtir. Görüntü dosyasının yolunu belirleme ve ardından dönüşüm ve normalleştirme için görüntüyü yükleme açısından kritik öneme sahiptir. | COMBO[STRING] |

## Çıkışlar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Piksel değerleri normalleştirilmiş ve gerekli dönüşümler uygulanmış işlenmiş görüntü. Daha ileri işleme veya analiz için hazırdır. | `IMAGE` |
| `mask` | Görüntü için bir maske sağlayan isteğe bağlı çıktı. Görüntünün şeffaflık için bir alfa kanalı içerdiği durumlarda kullanışlıdır. | `MASK` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/tr.md)
