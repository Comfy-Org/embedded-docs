> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

Bu düğüm, bir giriş görüntüsünün piksel değerlerini matematiksel bir normalleştirme işlemi kullanarak ayarlar. Her pikselden belirtilen bir ortalama değeri çıkarır ve ardından sonucu belirtilen bir standart sapma değerine böler. Bu, görüntü verilerini diğer makine öğrenimi modelleri için hazırlamak amacıyla yaygın bir ön işleme adımıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Normalleştirilecek giriş görüntüsü. |
| `mean` | FLOAT | Hayır | 0.0 - 1.0 | Görüntü piksellerinden çıkarılacak ortalama değer (varsayılan: 0.5). |
| `std` | FLOAT | Hayır | 0.001 - 1.0 | Görüntü piksellerinin bölüneceği standart sapma değeri (varsayılan: 0.5). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Normalleştirme işlemi uygulandıktan sonra elde edilen görüntü. |
