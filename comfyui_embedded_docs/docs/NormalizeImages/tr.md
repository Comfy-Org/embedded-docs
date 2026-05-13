> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

Bu düğüm, bir giriş görüntüsünün piksel değerlerini matematiksel bir normalleştirme işlemi kullanarak ayarlar. Her pikselden belirtilen bir ortalama değeri çıkarır ve ardından sonucu belirtilen bir standart sapmaya böler. Bu, görüntü verilerini diğer makine öğrenimi modelleri için hazırlamak amacıyla yapılan yaygın bir ön işleme adımıdır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image` | IMAGE | Evet | - | Normalleştirilecek giriş görüntüsü. |
| `ortalama` | FLOAT | Hayır | 0.0 - 1.0 | Normalleştirme için ortalama değeri (varsayılan: 0.5). |
| `std` | FLOAT | Hayır | 0.001 - 1.0 | Normalleştirme için standart sapma (varsayılan: 0.5). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Normalleştirme işlemi uygulandıktan sonra elde edilen sonuç görüntüsü. |

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
