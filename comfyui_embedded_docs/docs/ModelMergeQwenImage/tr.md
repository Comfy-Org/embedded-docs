# ModelBirleştirmeQwenGörsel

ModelMergeQwenImage, iki yapay zeka modelini bileşenlerini ayarlanabilir ağırlıklarla birleştirerek harmanlar. Qwen görüntü modellerinin transformer blokları, konumsal gömmeler ve metin işleme bileşenleri dahil belirli bölümlerini karıştırmanıza olanak tanır. Her modelin harmanlanmış sonucun farklı bölümleri üzerindeki etkisini kontrol edebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embeds.` | Konumsal gömme harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `img_in.` | Görüntü girişi işleme harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `txt_norm.` | Metin normalizasyonu harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `txt_in.` | Metin girişi işleme harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `time_text_embed.` | Zaman ve metin gömme harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `transformer_blocks.0.` ile `transformer_blocks.59.` | Her bir transformer bloğu harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `proj_out.` | Çıktı projeksiyonu harmanlaması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklarla her iki girdi modelinin bileşenlerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/tr.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
