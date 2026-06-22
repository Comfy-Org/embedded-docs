# ModelBirleştirmeSD3_2B

ModelMergeSD3_2B düğümü, iki Stable Diffusion 3 2B modelini bileşenlerini ayarlanabilir ağırlıklarla harmanlayarak birleştirmenizi sağlar. Gömm katmanları ve dönüştürücü blokları üzerinde bireysel kontrol sağlayarak, özel üretim görevleri için ince ayarlanmış model kombinasyonları oluşturulmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embed.` | Konum gömm enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x_embedder.` | Giriş gömm enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `context_embedder.` | Bağlam gömm enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `y_embedder.` | Y gömm enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `t_embedder.` | Zaman gömm enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.0.` | Ortak blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.1.` | Ortak blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.2.` | Ortak blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.3.` | Ortak blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.4.` | Ortak blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.5.` | Ortak blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.6.` | Ortak blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.7.` | Ortak blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.8.` | Ortak blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.9.` | Ortak blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.10.` | Ortak blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.11.` | Ortak blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.12.` | Ortak blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.13.` | Ortak blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.14.` | Ortak blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.15.` | Ortak blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.16.` | Ortak blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.17.` | Ortak blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.18.` | Ortak blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.19.` | Ortak blok 19 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.20.` | Ortak blok 20 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.21.` | Ortak blok 21 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.22.` | Ortak blok 22 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `joint_blocks.23.` | Ortak blok 23 enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `final_layer.` | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki giriş modelinin özelliklerini birleştiren harmanlanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/tr.md)

---
**Source fingerprint (SHA-256):** `5b0c28c66e1828742873191be424956a9006e59ea1167a5941069ba0b7bc390b`
