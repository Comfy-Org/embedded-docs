> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/tr.md)

ModelMergeSD1 düğümü, iki Stable Diffusion 1.x modelini farklı model bileşenlerinin etkisini ayarlayarak birleştirmenize olanak tanır. Zaman gömme, etiket gömme ve tüm giriş, orta ve çıkış blokları üzerinde ayrı ayrı kontrol sağlayarak belirli kullanım durumları için hassas ayarlanmış model birleştirme imkanı sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `time_embed.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme katmanı karıştırma ağırlığı (varsayılan: 1.0) |
| `label_emb.` | FLOAT | Evet | 0.0 - 1.0 | Etiket gömme katmanı karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 0 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 1 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 2 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 3 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 4 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 5 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 6 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 7 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 8 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 9 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 10 karıştırma ağırlığı (varsayılan: 1.0) |
| `input_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Giriş bloğu 11 karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.0.` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 0 karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.1.` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 1 karıştırma ağırlığı (varsayılan: 1.0) |
| `middle_block.2.` | FLOAT | Evet | 0.0 - 1.0 | Orta blok 2 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 0 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 1 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 2 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 3 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 4 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 5 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 6 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 7 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 8 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 9 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 10 karıştırma ağırlığı (varsayılan: 1.0) |
| `output_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış bloğu 11 karıştırma ağırlığı (varsayılan: 1.0) |
| `out.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış katmanı karıştırma ağırlığı (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Her iki giriş modelinden özellikleri birleştiren harmanlanmış model |