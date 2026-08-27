# ModelBirleştirmeCosmos7B

ModelMergeCosmos7B düğümü, belirli bileşenlerin ağırlıklı harmanlanmasını kullanarak iki yapay zeka modelini birleştirir. Konum yerleştirmeleri, transformatör blokları ve son katmanlar için bireysel ağırlıkları ayarlayarak modellerin farklı bölümlerinin nasıl birleştirileceği üzerinde ince ayar kontrolü sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embedder.` | Konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `extra_pos_embedder.` | Ek konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | x yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | t yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `affline_norm.` | Affine normalizasyon bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok0.` | Transformatör bloğu 0 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok1.` | Transformatör bloğu 1 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok2.` | Transformatör bloğu 2 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok3.` | Transformatör bloğu 3 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok4.` | Transformatör bloğu 4 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok5.` | Transformatör bloğu 5 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok6.` | Transformatör bloğu 6 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok7.` | Transformatör bloğu 7 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok8.` | Transformatör bloğu 8 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok9.` | Transformatör bloğu 9 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok10.` | Transformatör bloğu 10 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok11.` | Transformatör bloğu 11 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok12.` | Transformatör bloğu 12 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok13.` | Transformatör bloğu 13 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok14.` | Transformatör bloğu 14 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok15.` | Transformatör bloğu 15 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok16.` | Transformatör bloğu 16 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok17.` | Transformatör bloğu 17 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok18.` | Transformatör bloğu 18 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok19.` | Transformatör bloğu 19 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok20.` | Transformatör bloğu 20 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok21.` | Transformatör bloğu 21 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok22.` | Transformatör bloğu 22 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok23.` | Transformatör bloğu 23 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok24.` | Transformatör bloğu 24 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok25.` | Transformatör bloğu 25 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok26.` | Transformatör bloğu 26 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bloklar.blok27.` | Transformatör bloğu 27 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

Tüm ağırlık parametreleri 0.0 ile 1.0 arasında 0.01 adımlarla değer kabul eder ve varsayılan olarak 1.0 değerini alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/tr.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`
