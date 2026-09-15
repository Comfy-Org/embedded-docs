# ModelBirleştirmeSD3_2B

ModelMergeSD3_2B düğümü, iki Stable Diffusion 3 2B modelini bileşenlerini ayarlanabilir ağırlıklarla harmanlayarak birleştirmenizi sağlar. Gömme katmanları, transformer blokları ve son katman üzerinde ayrı ayrı kontrol sunarak iki modelin ince ayarlı kombinasyonlarını oluşturmayı mümkün kılar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embed.` | Konum gömme enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | Girdi gömme enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `context_embedder.` | Bağlam gömme enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `y_embedder.` | Y gömme enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömme enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.0.` | Birleşik blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.1.` | Birleşik blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.2.` | Birleşik blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.3.` | Birleşik blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.4.` | Birleşik blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.5.` | Birleşik blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.6.` | Birleşik blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.7.` | Birleşik blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.8.` | Birleşik blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.9.` | Birleşik blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.10.` | Birleşik blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.11.` | Birleşik blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.12.` | Birleşik blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.13.` | Birleşik blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.14.` | Birleşik blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.15.` | Birleşik blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.16.` | Birleşik blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.17.` | Birleşik blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.18.` | Birleşik blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.19.` | Birleşik blok 19 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.20.` | Birleşik blok 20 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.21.` | Birleşik blok 21 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.22.` | Birleşik blok 22 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.23.` | Birleşik blok 23 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/tr.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`
