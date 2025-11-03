> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/tr.md)

ModelMergeSDXL düğümü, mimarinin farklı bölümlerinde her bir modelin etkisini ayarlayarak iki SDXL modelini birleştirmenize olanak tanır. Zaman gömme katmanları, etiket gömme katmanları ve model yapısı içindeki çeşitli bloklara her bir modelin ne kadar katkıda bulunacağını kontrol edebilirsiniz. Bu, her iki giriş modelinden özellikleri birleştiren melez bir model oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk SDXL modeli |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci SDXL modeli |
| `time_embed.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme katmanları için karıştırma ağırlığı (varsayılan: 1.0) |
| `label_emb.` | FLOAT | Evet | 0.0 - 1.0 | Etiket gömme katmanları için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.0` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.1` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.2` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.3` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 3 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.4` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 4 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.5` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 5 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.6` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 6 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.7` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 7 için karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.8` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 8 için karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.0` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.1` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.2` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.0` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 0 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.1` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 1 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.2` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 2 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.3` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 3 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.4` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 4 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.5` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 5 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.6` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 6 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.7` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 7 için karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.8` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 8 için karıştırma ağırlığı (varsayılan: 1.0) |
| `out.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış katmanları için karıştırma ağırlığı (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki giriş modelinden özellikleri birleştiren birleştirilmiş SDXL modeli |