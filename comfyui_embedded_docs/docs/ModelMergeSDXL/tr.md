# ModelBirleştirmeSDXL

The ModelMergeSDXL düğümü, iki SDXL modelini mimarinin farklı bölümleri üzerindeki her modelin etkisini ayarlayarak birbirine karıştırmanızı sağlar. Her modelin zaman gömmelerine, etiket gömmelerine ve model yapısı içindeki çeşitli bloklara ne kadar katkıda bulunacağını kontrol edebilirsiniz. Bu, her iki girdi modelinin özelliklerini birleştiren hibrit bir model oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk SDXL modeli | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci SDXL modeli | MODEL | Evet | - |
| `time_embed.` | Zaman gömmesi katmanları için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `label_emb.` | Etiket gömmesi katmanları için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.0` | Girdi bloğu 0 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.1` | Girdi bloğu 1 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.2` | Girdi bloğu 2 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.3` | Girdi bloğu 3 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.4` | Girdi bloğu 4 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.5` | Girdi bloğu 5 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.6` | Girdi bloğu 6 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.7` | Girdi bloğu 7 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `input_blocks.8` | Girdi bloğu 8 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `middle_block.0` | Orta blok 0 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `middle_block.1` | Orta blok 1 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `middle_block.2` | Orta blok 2 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.0` | Çıktı bloğu 0 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.1` | Çıktı bloğu 1 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.2` | Çıktı bloğu 2 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.3` | Çıktı bloğu 3 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.4` | Çıktı bloğu 4 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.5` | Çıktı bloğu 5 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.6` | Çıktı bloğu 6 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.7` | Çıktı bloğu 7 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `output_blocks.8` | Çıktı bloğu 8 için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `out.` | Çıktı katmanları için karıştırma ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

Tüm karıştırma ağırlığı parametreleri, 0.0 ile 1.0 arasında zorunlu FLOAT değerleridir, varsayılan olarak 1.0'dır ve 0.01 adımlarla ayarlanabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş SDXL modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/tr.md)

---
**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`
