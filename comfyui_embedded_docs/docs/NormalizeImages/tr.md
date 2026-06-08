Bu düğüm, bir giriş görüntüsünün piksel değerlerini matematiksel bir normalleştirme işlemi kullanarak ayarlar. Her pikselden belirtilen bir ortalama değeri çıkarır ve ardından sonucu belirtilen bir standart sapmaya böler. Bu, görüntü verilerini diğer makine öğrenimi modelleri için hazırlamak amacıyla yapılan yaygın bir ön işleme adımıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Normalleştirilecek giriş görüntüsü. | IMAGE | Evet | - |
| `ortalama` | Normalleştirme için ortalama değeri (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `std` | Normalleştirme için standart sapma (varsayılan: 0.5). | FLOAT | Hayır | 0.001 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Normalleştirme işlemi uygulandıktan sonra elde edilen sonuç görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
