# ModelBirleştirmeCosmos14B

**ModelMergeCosmos14B** düğümü, Cosmos 14B model mimarisi için özel olarak tasarlanmış blok tabanlı bir yaklaşım kullanarak iki yapay zeka modelini birleştirir. Her model bloğu ve katman gömme (embedding) katmanı için ağırlık değerlerini 0.0 ile 1.0 arasında ayarlayarak modellerin farklı bileşenlerini harmanlamanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embedder.` | Konum katman gömücü (position embedder) bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `extra_pos_embedder.` | Ek konum katman gömücü (extra position embedder) bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | x katman gömücü (x embedder) bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | t katman gömücü (t embedder) bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `affline_norm.` | Afin normalizasyon (affine normalization) bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block0.` | Blok 0 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block1.` | Blok 1 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block2.` | Blok 2 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block3.` | Blok 3 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block4.` | Blok 4 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block5.` | Blok 5 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block6.` | Blok 6 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block7.` | Blok 7 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block8.` | Blok 8 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block9.` | Blok 9 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block10.` | Blok 10 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block11.` | Blok 11 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block12.` | Blok 12 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block13.` | Blok 13 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block14.` | Blok 14 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block15.` | Blok 15 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block16.` | Blok 16 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block17.` | Blok 17 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block18.` | Blok 18 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block19.` | Blok 19 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block20.` | Blok 20 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block21.` | Blok 21 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block22.` | Blok 22 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block23.` | Blok 23 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block24.` | Blok 24 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block25.` | Blok 25 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block26.` | Blok 26 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block27.` | Blok 27 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block28.` | Blok 28 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block29.` | Blok 29 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block30.` | Blok 30 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block31.` | Blok 31 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block32.` | Blok 32 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block33.` | Blok 33 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block34.` | Blok 34 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block35.` | Blok 35 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman (final layer) için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/tr.md)

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
