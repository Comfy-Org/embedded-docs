# Görüntüleri Normalleştir

Bu düğüm, girdi görüntüsünün piksel değerlerini matematiksel bir normalizasyon süreci kullanarak ayarlar. Her pikselden belirtilen ortalama (mean) değerini çıkarır ve sonucu belirtilen standart sapmaya (std) böler. Bu, görüntü verilerini diğer makine öğrenimi modelleri için hazırlamak amacıyla yapılan yaygın bir ön işleme adımıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Normalize edilecek girdi görüntüsü. | IMAGE | Evet | - |
| `ortalama` | Normalizasyon için ortalama değeri (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `std` | Normalizasyon için standart sapma (varsayılan: 0.5). | FLOAT | Hayır | 0.001 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | Normalizasyon süreci uygulandıktan sonra elde edilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
