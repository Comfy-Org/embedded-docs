> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/tr.md)

ModelMergeCosmos14B düğümü, Cosmos 14B model mimarisi için özel olarak tasarlanmış blok tabanlı bir yaklaşım kullanarak iki yapay zeka modelini birleştirir. Her model bloğu ve gömme katmanı için 0.0 ile 1.0 arasında ağırlık değerlerini ayarlayarak modellerin farklı bileşenlerini harmanlamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Konum gömücü ağırlığı (varsayılan: 1.0) |
| `extra_pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Ek konum gömücü ağırlığı (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | X gömücü ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | T gömücü ağırlığı (varsayılan: 1.0) |
| `affline_norm.` | FLOAT | Evet | 0.0 - 1.0 | Afin normalizasyon ağırlığı (varsayılan: 1.0) |
| `blocks.block0.` | FLOAT | Evet | 0.0 - 1.0 | Blok 0 ağırlığı (varsayılan: 1.0) |
| `blocks.block1.` | FLOAT | Evet | 0.0 - 1.0 | Blok 1 ağırlığı (varsayılan: 1.0) |
| `blocks.block2.` | FLOAT | Evet | 0.0 - 1.0 | Blok 2 ağırlığı (varsayılan: 1.0) |
| `blocks.block3.` | FLOAT | Evet | 0.0 - 1.0 | Blok 3 ağırlığı (varsayılan: 1.0) |
| `blocks.block4.` | FLOAT | Evet | 0.0 - 1.0 | Blok 4 ağırlığı (varsayılan: 1.0) |
| `blocks.block5.` | FLOAT | Evet | 0.0 - 1.0 | Blok 5 ağırlığı (varsayılan: 1.0) |
| `blocks.block6.` | FLOAT | Evet | 0.0 - 1.0 | Blok 6 ağırlığı (varsayılan: 1.0) |
| `blocks.block7.` | FLOAT | Evet | 0.0 - 1.0 | Blok 7 ağırlığı (varsayılan: 1.0) |
| `blocks.block8.` | FLOAT | Evet | 0.0 - 1.0 | Blok 8 ağırlığı (varsayılan: 1.0) |
| `blocks.block9.` | FLOAT | Evet | 0.0 - 1.0 | Blok 9 ağırlığı (varsayılan: 1.0) |
| `blocks.block10.` | FLOAT | Evet | 0.0 - 1.0 | Blok 10 ağırlığı (varsayılan: 1.0) |
| `blocks.block11.` | FLOAT | Evet | 0.0 - 1.0 | Blok 11 ağırlığı (varsayılan: 1.0) |
| `blocks.block12.` | FLOAT | Evet | 0.0 - 1.0 | Blok 12 ağırlığı (varsayılan: 1.0) |
| `blocks.block13.` | FLOAT | Evet | 0.0 - 1.0 | Blok 13 ağırlığı (varsayılan: 1.0) |
| `blocks.block14.` | FLOAT | Evet | 0.0 - 1.0 | Blok 14 ağırlığı (varsayılan: 1.0) |
| `blocks.block15.` | FLOAT | Evet | 0.0 - 1.0 | Blok 15 ağırlığı (varsayılan: 1.0) |
| `blocks.block16.` | FLOAT | Evet | 0.0 - 1.0 | Blok 16 ağırlığı (varsayılan: 1.0) |
| `blocks.block17.` | FLOAT | Evet | 0.0 - 1.0 | Blok 17 ağırlığı (varsayılan: 1.0) |
| `blocks.block18.` | FLOAT | Evet | 0.0 - 1.0 | Blok 18 ağırlığı (varsayılan: 1.0) |
| `blocks.block19.` | FLOAT | Evet | 0.0 - 1.0 | Blok 19 ağırlığı (varsayılan: 1.0) |
| `blocks.block20.` | FLOAT | Evet | 0.0 - 1.0 | Blok 20 ağırlığı (varsayılan: 1.0) |
| `blocks.block21.` | FLOAT | Evet | 0.0 - 1.0 | Blok 21 ağırlığı (varsayılan: 1.0) |
| `blocks.block22.` | FLOAT | Evet | 0.0 - 1.0 | Blok 22 ağırlığı (varsayılan: 1.0) |
| `blocks.block23.` | FLOAT | Evet | 0.0 - 1.0 | Blok 23 ağırlığı (varsayılan: 1.0) |
| `blocks.block24.` | FLOAT | Evet | 0.0 - 1.0 | Blok 24 ağırlığı (varsayılan: 1.0) |
| `blocks.block25.` | FLOAT | Evet | 0.0 - 1.0 | Blok 25 ağırlığı (varsayılan: 1.0) |
| `blocks.block26.` | FLOAT | Evet | 0.0 - 1.0 | Blok 26 ağırlığı (varsayılan: 1.0) |
| `blocks.block27.` | FLOAT | Evet | 0.0 - 1.0 | Blok 27 ağırlığı (varsayılan: 1.0) |
| `blocks.block28.` | FLOAT | Evet | 0.0 - 1.0 | Blok 28 ağırlığı (varsayılan: 1.0) |
| `blocks.block29.` | FLOAT | Evet | 0.0 - 1.0 | Blok 29 ağırlığı (varsayılan: 1.0) |
| `blocks.block30.` | FLOAT | Evet | 0.0 - 1.0 | Blok 30 ağırlığı (varsayılan: 1.0) |
| `blocks.block31.` | FLOAT | Evet | 0.0 - 1.0 | Blok 31 ağırlığı (varsayılan: 1.0) |
| `blocks.block32.` | FLOAT | Evet | 0.0 - 1.0 | Blok 32 ağırlığı (varsayılan: 1.0) |
| `blocks.block33.` | FLOAT | Evet | 0.0 - 1.0 | Blok 33 ağırlığı (varsayılan: 1.0) |
| `blocks.block34.` | FLOAT | Evet | 0.0 - 1.0 | Blok 34 ağırlığı (varsayılan: 1.0) |
| `blocks.block35.` | FLOAT | Evet | 0.0 - 1.0 | Blok 35 ağırlığı (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki giriş modelinin özelliklerini birleştiren birleştirilmiş model |