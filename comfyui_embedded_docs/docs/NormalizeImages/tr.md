# Görüntüleri Normalleştir

Bu düğüm, girdi görüntüsünü her pikselden belirtilen ortalama değeri çıkararak ve ardından sonucu belirtilen standart sapmaya bölerek normalleştirir. Bu, piksel değerlerini standartlaştırmak ve görüntü verilerini daha sonraki işlemler için hazırlamak amacıyla yapılan yaygın bir ön işleme adımıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Normalleştirilecek girdi görüntüsü. | IMAGE | Evet | - |
| `mean` | Normalleştirme için ortalama değer (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `std` | Normalleştirme için standart sapma (varsayılan: 0.5). | FLOAT | Hayır | 0.001 - 1.0 |

Not: Normalleştirme, tüm görüntü grubuna aynı anda uygulanır ve herhangi bir grup boyutu desteklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Normalleştirme işlemi uygulandıktan sonra elde edilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
