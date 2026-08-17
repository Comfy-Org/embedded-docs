# ModelBirleştirmeQwenGörsel

ModelMergeQwenImage düğümü, iki yapay zeka modelini, bileşenlerini ayarlanabilir ağırlıklarla harmanlayarak birleştirir. Qwen görüntü modellerinin transformer blokları, konumsal gömme ve metin işleme bileşenleri dahil belirli bölümlerini harmanlamanıza olanak tanır. Her modelin, birleştirilmiş sonucun farklı bölümleri üzerindeki etki düzeyini kontrol edebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model (varsayılan: yok) | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model (varsayılan: yok) | MODEL | Evet | - |
| `pos_embeds.` | Konumsal gömme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `img_in.` | Görüntü girişi işleme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `txt_norm.` | Metin normalizasyonu harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `txt_in.` | Metin girişi işleme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `time_text_embed.` | Zaman ve metin gömme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `transformer_blocks.0.` ile `transformer_blocks.59.` arası | Her bir transformer bloğu için harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `proj_out.` | Çıktı projeksiyonu harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |

Not: Modeldeki her transformer bloğu için bir tane olmak üzere 60 ayrı transformer bloğu ağırlık girdisi vardır (`transformer_blocks.0.` ile `transformer_blocks.59.` arası).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklarla her iki girdi modelinin bileşenlerini harmanlayan birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/tr.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
