> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/tr.md)

ModelMergeSD3_2B düğümü, iki adet Stable Diffusion 3 2B modelini, bileşenlerini ayarlanabilir ağırlıklarla harmanlayarak birleştirmenize olanak tanır. Gömme katmanları ve transformör blokları üzerinde bireysel kontrol sağlayarak, özel üretim görevleri için ince ayarlı model kombinasyonları oluşturmanıza imkan verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model |
| `pos_embed.` | FLOAT | Evet | 0.0 - 1.0 | Konum gömme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `x_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Giriş gömme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `context_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Bağlam gömme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `y_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Y gömme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `t_embedder.` | FLOAT | Evet | 0.0 - 1.0 | Zaman gömme enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.0.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 0 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.1.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 1 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.2.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 2 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.3.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 3 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.4.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 4 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.5.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 5 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.6.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 6 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.7.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 7 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.8.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 8 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.9.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 9 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.10.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 10 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.11.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 11 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.12.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 12 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.13.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 13 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.14.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 14 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.15.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 15 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.16.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 16 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.17.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 17 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.18.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 18 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.19.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 19 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.20.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 20 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.21.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 21 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.22.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 22 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `joint_blocks.23.` | FLOAT | Evet | 0.0 - 1.0 | Birleşik blok 23 enterpolasyon ağırlığı (varsayılan: 1.0) |
| `final_layer.` | FLOAT | Evet | 0.0 - 1.0 | Son katman enterpolasyon ağırlığı (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Her iki giriş modelinin özelliklerini birleştiren harmanlanmış model |