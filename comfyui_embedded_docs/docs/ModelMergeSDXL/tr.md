> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/tr.md)

ModelMergeSDXL düğümü, iki SDXL modelini birleştirerek her bir modelin mimarinin farklı bölümleri üzerindeki etkisini ayarlamanıza olanak tanır. Zaman gömmeleri, etiket gömmeleri ve model yapısındaki çeşitli bloklar üzerinde her bir modelin ne kadar katkıda bulunacağını kontrol edebilirsiniz. Bu, her iki girdi modelinin özelliklerini birleştiren hibrit bir model oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk SDXL modeli |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci SDXL modeli |
| `time_embed.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme katmanları için karıştırma ağırlığı (varsayılan: 1.0) |
| `label_emb.` | FLOAT | Evet | 0.0 - 1.0 | Etiket gömme katmanları için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.0` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.1` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.2` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.3` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 3 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.4` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 4 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.5` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 5 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.6` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 6 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.7` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 7 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.8` | FLOAT | Evet | 0.0 - 1.0 | Girdi bloğu 8 için karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.0` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.1` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.2` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.0` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.1` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.2` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.3` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 3 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.4` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 4 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.5` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 5 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.6` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 6 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.7` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 7 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.8` | FLOAT | Evet | 0.0 - 1.0 | Çıktı bloğu 8 için karıştırma ağırlığı (varsayılan: 1.0) |
| `out.` | FLOAT | Evet | 0.0 - 1.0 | Çıktı katmanları için karıştırma ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `model` | MODEL | Her iki girdi modelinin özelliklerini birleştiren birleştirilmiş SDXL modeli |

---
**Source fingerprint (SHA-256):** `6c7572a6ed50534f2d9ad6f499146763457da58f0c9dd4b85204e67f7d3e9660`
