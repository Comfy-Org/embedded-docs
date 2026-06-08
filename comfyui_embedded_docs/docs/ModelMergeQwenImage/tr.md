ModelMergeQwenImage düğümü, iki yapay zeka modelini bileşenlerini ayarlanabilir ağırlıklarla birleştirerek birleştirir. Transformer blokları, konumsal gömme (positional embedding) ve metin işleme bileşenleri dahil olmak üzere Qwen görüntü modellerinin belirli bölümlerini harmanlamanıza olanak tanır. Her bir modelin, birleştirilmiş sonucun farklı bölümleri üzerinde ne kadar etkili olacağını kontrol edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model (varsayılan: yok) | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model (varsayılan: yok) | MODEL | Evet | - |
| `pos_embeds.` | Konumsal gömme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `img_in.` | Görüntü giriş işleme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `txt_norm.` | Metin normalizasyonu harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `txt_in.` | Metin giriş işleme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `time_text_embed.` | Zaman ve metin gömme harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `transformer_blocks.0.` ile `transformer_blocks.59.` arası | Her bir transformer bloğu harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `proj_out.` | Çıktı projeksiyonu harmanlama ağırlığı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklarla her iki giriş modelinin bileşenlerini birleştiren birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/tr.md)

---
**Source fingerprint (SHA-256):** `a0424a3f4d4ffe170471ba463350d741f67ff1b1f5a8a016ad844c111033f97c`
