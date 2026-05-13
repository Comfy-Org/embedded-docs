> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/tr.md)

LoadImage düğümü, belirtilen bir yoldan görüntüleri yüklemek ve ön işlemek için tasarlanmıştır. Çoklu kare içeren görüntü formatlarını işler, EXIF verilerine dayalı döndürme gibi gerekli dönüşümleri uygular, piksel değerlerini normalleştirir ve isteğe bağlı olarak alfa kanalına sahip görüntüler için bir maske oluşturur. Bu düğüm, görüntüleri bir iş akışı içinde daha ileri işleme veya analiz için hazırlamada önemli bir rol oynar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|--------------|-------------|
| `görüntü`   | COMBO[STRING] | 'image' parametresi, yüklenecek ve işlenecek görüntünün tanımlayıcısını belirtir. Görüntü dosyasının yolunu belirleme ve ardından dönüşüm ve normalleştirme için görüntüyü yükleme açısından kritik öneme sahiptir. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | Piksel değerleri normalleştirilmiş ve gerekli dönüşümler uygulanmış işlenmiş görüntü. Daha ileri işleme veya analiz için hazırdır. |
| `mask`    | `MASK`      | Görüntü için bir maske sağlayan isteğe bağlı çıktı. Görüntünün şeffaflık için bir alfa kanalı içerdiği durumlarda kullanışlıdır. |