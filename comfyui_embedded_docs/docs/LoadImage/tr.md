> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/tr.md)

LoadImage düğümü, belirli bir yoldan görüntüleri yüklemek ve ön işlemek üzere tasarlanmıştır. Çoklu kare içeren görüntü formatlarını işler, EXIF verilerine dayalı döndürme gibi gerekli dönüşümleri uygular, piksel değerlerini normalleştirir ve isteğe bağlı olarak alfa kanalı içeren görüntüler için bir maske oluşturur. Bu düğüm, bir işlem hattı içinde görüntülerin ileri işleme veya analiz için hazırlanmasında esastır.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `image`   | COMBO[STRING] | 'image' parametresi, yüklenecek ve işlenecek görüntünün tanımlayıcısını belirtir. Görüntü dosyasının yolunun belirlenmesi ve ardından görüntünün dönüşüm ve normalleştirme için yüklenmesinde çok önemlidir. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|-------------|
| `image`   | `IMAGE`   | Piksel değerleri normalleştirilmiş ve gerekli dönüşümler uygulanmış işlenmiş görüntü. İleri işleme veya analiz için hazırdır. |
| `mask`    | `MASK`    | Görüntünün şeffaflık için bir alfa kanalı içerdiği senaryolarda kullanışlı olan, görüntü için isteğe bağlı bir maske çıktısı sağlar. |