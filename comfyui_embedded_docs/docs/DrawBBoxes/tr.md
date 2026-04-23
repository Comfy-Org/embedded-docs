> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/tr.md)

DrawBBoxes düğümü, bir görüntü üzerine sınırlayıcı kutular, etiketler ve güven skorları çizerek nesne tespit sonuçlarını görselleştirir. Giriş görüntüsü sağlanmazsa, çizilen tüm kutuları içerecek kadar büyük boş bir tuval oluşturur. Toplu işlemeyi destekleyerek birden fazla görüntü için farklı tespit kümeleri çizmenize veya aynı tespitleri bir toplu iş boyunca tekrarlamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Hayır | - | Sınırlayıcı kutuların çizileceği giriş görüntüsü(leri). Sağlanmazsa boş bir tuval oluşturulur. |
| `bboxes` | BOUNDINGBOX | Evet | - | Sınırlayıcı kutu sözlüklerinin bir listesi. Her sözlük `x`, `y`, `width`, `height` anahtarlarını ve isteğe bağlı olarak `label` ile `score` anahtarlarını içermelidir. |

**Giriş Kısıtlamaları:**
*   `bboxes` girişi zorunludur ve sağlanmalıdır.
*   Düğüm, `bboxes` için farklı giriş formatlarını otomatik olarak işler. Tek bir sözlük, toplu işteki tüm görüntülere uygulanır. Düz bir sözlük listesi, her görüntü için aynı tespit kümesi olarak ele alınır. Bir liste listesi, toplu işteki her görüntü için farklı tespitler belirtmenize olanak tanır.
*   Bir `image` sağlanmazsa, düğüm, varsayılan minimum 640x640 boyutunda, sağlanan tüm sınırlayıcı kutuları sığdıracak kadar büyük boş bir görüntü oluşturur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `out_image` | IMAGE | Üzerine çizilmiş sınırlayıcı kutular, etiketler ve güven skorları bulunan çıktı görüntüsü(leri). |