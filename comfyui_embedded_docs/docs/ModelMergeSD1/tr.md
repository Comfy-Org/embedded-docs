# ModelBirleştirmeSD1

ModelMergeSD1, iki Stable Diffusion 1.x modelini, bireysel bileşenlerinin etkisini ayarlayarak birbirine karıştırmanıza olanak tanır. Zaman gömme, etiket gömme, her giriş bloğu, her orta blok, her çıkış bloğu ve son çıkış katmanı için ayrı bir karıştırma ağırlığı sağlayarak, iki modelin nasıl birleştirileceği üzerinde ince ayarlı kontrol imkânı sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `time_embed.` | Zaman gömme katmanı karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `label_emb.` | Etiket gömme katmanı karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.0.` | Giriş bloğu 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.1.` | Giriş bloğu 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.2.` | Giriş bloğu 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.3.` | Giriş bloğu 3 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.4.` | Giriş bloğu 4 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.5.` | Giriş bloğu 5 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.6.` | Giriş bloğu 6 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.7.` | Giriş bloğu 7 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.8.` | Giriş bloğu 8 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.9.` | Giriş bloğu 9 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.10.` | Giriş bloğu 10 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.11.` | Giriş bloğu 11 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `middle_block.0.` | Orta blok 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `middle_block.1.` | Orta blok 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `middle_block.2.` | Orta blok 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.0.` | Çıkış bloğu 0 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.1.` | Çıkış bloğu 1 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.2.` | Çıkış bloğu 2 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.3.` | Çıkış bloğu 3 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.4.` | Çıkış bloğu 4 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.5.` | Çıkış bloğu 5 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.6.` | Çıkış bloğu 6 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.7.` | Çıkış bloğu 7 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.8.` | Çıkış bloğu 8 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.9.` | Çıkış bloğu 9 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.10.` | Çıkış bloğu 10 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.11.` | Çıkış bloğu 11 karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `out.` | Çıkış katmanı karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Her iki giriş modelinin özelliklerini harmanlayan birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/tr.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
