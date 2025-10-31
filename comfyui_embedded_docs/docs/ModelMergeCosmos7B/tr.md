> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/tr.md)

ModelMergeCosmos7B düğümü, iki AI modelini belirli bileşenlerin ağırlıklı harmanlanması yoluyla birleştirir. Konum yerleştirmeleri, transformatör blokları ve son katmanlar için bireysel ağırlıkları ayarlayarak modellerin farklı bölümlerinin nasıl birleştirileceği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) |
| `extra_pos_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Ek konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | X yerleştirici bileşeni için ağırlık (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | T yerleştirici bileşeni için ağırlık (varsayılan: 1.0) |
| `affline_norm.` | FLOAT | Evet | 0.0 - 1.0 | Afin normalizasyon bileşeni için ağırlık (varsayılan: 1.0) |
| `blocks.block0.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 0 için ağırlık (varsayılan: 1.0) |
| `blocks.block1.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 1 için ağırlık (varsayılan: 1.0) |
| `blocks.block2.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 2 için ağırlık (varsayılan: 1.0) |
| `blocks.block3.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 3 için ağırlık (varsayılan: 1.0) |
| `blocks.block4.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 4 için ağırlık (varsayılan: 1.0) |
| `blocks.block5.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 5 için ağırlık (varsayılan: 1.0) |
| `blocks.block6.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 6 için ağırlık (varsayılan: 1.0) |
| `blocks.block7.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 7 için ağırlık (varsayılan: 1.0) |
| `blocks.block8.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 8 için ağırlık (varsayılan: 1.0) |
| `blocks.block9.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 9 için ağırlık (varsayılan: 1.0) |
| `blocks.block10.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 10 için ağırlık (varsayılan: 1.0) |
| `blocks.block11.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 11 için ağırlık (varsayılan: 1.0) |
| `blocks.block12.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 12 için ağırlık (varsayılan: 1.0) |
| `blocks.block13.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 13 için ağırlık (varsayılan: 1.0) |
| `blocks.block14.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 14 için ağırlık (varsayılan: 1.0) |
| `blocks.block15.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 15 için ağırlık (varsayılan: 1.0) |
| `blocks.block16.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 16 için ağırlık (varsayılan: 1.0) |
| `blocks.block17.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 17 için ağırlık (varsayılan: 1.0) |
| `blocks.block18.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 18 için ağırlık (varsayılan: 1.0) |
| `blocks.block19.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 19 için ağırlık (varsayılan: 1.0) |
| `blocks.block20.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 20 için ağırlık (varsayılan: 1.0) |
| `blocks.block21.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 21 için ağırlık (varsayılan: 1.0) |
| `blocks.block22.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 22 için ağırlık (varsayılan: 1.0) |
| `blocks.block23.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 23 için ağırlık (varsayılan: 1.0) |
| `blocks.block24.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 24 için ağırlık (varsayılan: 1.0) |
| `blocks.block25.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 25 için ağırlık (varsayılan: 1.0) |
| `blocks.block26.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 26 için ağırlık (varsayılan: 1.0) |
| `blocks.block27.` | FLOAT | Evet | 0.0 - 1.0 | Transformatör bloğu 27 için ağırlık (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman bileşeni için ağırlık (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki girdi modelinden özellikleri birleştiren birleştirilmiş model |