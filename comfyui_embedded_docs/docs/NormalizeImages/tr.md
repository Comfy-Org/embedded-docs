# Görüntüleri Normalleştir

Bu düğüm, bir girdi görüntüsünün renklerini, piksel değerlerini belirtilen ortalama ve standart sapmaya göre ayarlayarak normalleştirir. Her pikselden ortalama çıkarılır ve ardından standart sapmaya bölünür; bu, diğer işlemlerden önce görüntü verilerini standart hale getirmek için yaygın bir adımdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Normalleştirilecek girdi görüntüsü. | IMAGE | Evet | - |
| `ortalama` | Normalleştirme için ortalama değeri (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `std` | Normalleştirme için standart sapma (varsayılan: 0.5). | FLOAT | Hayır | 0.001 - 1.0 |

`mean` ve `std` parametreleri, girdi görüntüsüne uygulanan normalleştirmeyi kontrol eder. Her iki parametrenin varsayılan değeri 0.5'tir.

Not: Girdi görüntüsünde bir alfa (saydamlık) kanalı varsa, bu kanal normalleştirilmez. Alfa, renk yerine saydamlığı depoladığı için çıktıya değiştirilmeden kopyalanır.

Not: Düğüm herhangi bir toplu iş boyutuyla çalışır, bu nedenle birden fazla görüntü aynı anda işlenebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Normalleştirme işlemi uygulandıktan sonra elde edilen görüntü. Piksel değerleri belirtilen ortalama ve standart sapma kullanılarak ayarlanır ve alfa kanalı (varsa) korunur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
