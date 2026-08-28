# ModelBirleştirmeCosmos14B

**ModelMergeCosmos14B** düğümü, Cosmos 14B model mimarisi için özel olarak tasarlanmış blok tabanlı bir yaklaşım kullanarak iki yapay zeka modelini birleştirir. Her model bloğu ve yerleştirme katmanı için 0.0 ile 1.0 arasındaki ağırlık değerlerini ayarlayarak modellerin farklı bileşenlerini harmanlamanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embedder.` | Konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `extra_pos_embedder.` | Ekstra konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `x_embedder.` | x yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `t_embedder.` | t yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `affline_norm.` | Afin normalizasyon bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok0.` | Blok 0 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok1.` | Blok 1 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok2.` | Blok 2 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok3.` | Blok 3 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok4.` | Blok 4 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok5.` | Blok 5 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok6.` | Blok 6 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok7.` | Blok 7 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok8.` | Blok 8 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok9.` | Blok 9 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok10.` | Blok 10 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok11.` | Blok 11 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok12.` | Blok 12 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok13.` | Blok 13 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok14.` | Blok 14 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok15.` | Blok 15 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok16.` | Blok 16 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok17.` | Blok 17 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok18.` | Blok 18 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok19.` | Blok 19 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok20.` | Blok 20 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok21.` | Blok 21 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok22.` | Blok 22 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok23.` | Blok 23 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok24.` | Blok 24 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok25.` | Blok 25 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok26.` | Blok 26 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok27.` | Blok 27 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok28.` | Blok 28 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok29.` | Blok 29 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok30.` | Blok 30 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok31.` | Blok 31 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok32.` | Blok 32 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok33.` | Blok 33 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok34.` | Blok 34 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `bloklar.blok35.` | Blok 35 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `final_layer.` | Son katman için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/tr.md)

---
**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`
