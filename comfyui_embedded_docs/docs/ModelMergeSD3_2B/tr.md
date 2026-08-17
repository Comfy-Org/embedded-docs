# ModelBirleştirmeSD3_2B

The ModelMergeSD3_2B node allows you to merge two Stable Diffusion 3 2B models by blending their components with adjustable weights. It provides individual control over embedding layers and transformer blocks, enabling fine-tuned model combinations for specialized generation tasks.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embed.` | Konum embedding enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `x_embedder.` | Girdi embedding enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `context_embedder.` | Bağlam embedding enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `y_embedder.` | Y embedding enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `t_embedder.` | Zaman embedding enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.0.` | Ortak blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.1.` | Ortak blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.2.` | Ortak blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.3.` | Ortak blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.4.` | Ortak blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.5.` | Ortak blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.6.` | Ortak blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.7.` | Ortak blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.8.` | Ortak blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.9.` | Ortak blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.10.` | Ortak blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.11.` | Ortak blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.12.` | Ortak blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.13.` | Ortak blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.14.` | Ortak blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.15.` | Ortak blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.16.` | Ortak blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.17.` | Ortak blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.18.` | Ortak blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.19.` | Ortak blok 19 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.20.` | Ortak blok 20 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.21.` | Ortak blok 21 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.22.` | Ortak blok 22 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `joint_blocks.23.` | Ortak blok 23 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |
| `final_layer.` | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/tr.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`
