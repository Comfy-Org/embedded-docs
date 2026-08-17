# ModelBirleştirmeCosmos7B

The ModelMergeCosmos7B node merges two AI models together using weighted blending of specific components. It allows fine-grained control over how different parts of the models are combined by adjusting individual weights for position embeddings, transformer blocks, and final layers.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embedder.` | Konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `extra_pos_embedder.` | Ek konum yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | x yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | t yerleştirici bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `affline_norm.` | Afin normalizasyon bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block0.` | Transformer bloğu 0 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block1.` | Transformer bloğu 1 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block2.` | Transformer bloğu 2 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block3.` | Transformer bloğu 3 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block4.` | Transformer bloğu 4 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block5.` | Transformer bloğu 5 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block6.` | Transformer bloğu 6 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block7.` | Transformer bloğu 7 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block8.` | Transformer bloğu 8 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block9.` | Transformer bloğu 9 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block10.` | Transformer bloğu 10 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block11.` | Transformer bloğu 11 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block12.` | Transformer bloğu 12 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block13.` | Transformer bloğu 13 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block14.` | Transformer bloğu 14 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block15.` | Transformer bloğu 15 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block16.` | Transformer bloğu 16 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block17.` | Transformer bloğu 17 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block18.` | Transformer bloğu 18 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block19.` | Transformer bloğu 19 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block20.` | Transformer bloğu 20 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block21.` | Transformer bloğu 21 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block22.` | Transformer bloğu 22 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block23.` | Transformer bloğu 23 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block24.` | Transformer bloğu 24 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block25.` | Transformer bloğu 25 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block26.` | Transformer bloğu 26 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `blocks.block27.` | Transformer bloğu 27 için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman bileşeni için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/tr.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`
