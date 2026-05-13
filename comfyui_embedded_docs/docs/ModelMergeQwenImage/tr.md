> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/tr.md)

ModelMergeQwenImage düğümü, iki yapay zeka modelini bileşenlerini ayarlanabilir ağırlıklarla birleştirerek birleştirir. Transformer blokları, konumsal gömme (positional embedding) ve metin işleme bileşenleri dahil olmak üzere Qwen görüntü modellerinin belirli bölümlerini harmanlamanıza olanak tanır. Her bir modelin, birleştirilmiş sonucun farklı bölümleri üzerinde ne kadar etkili olacağını kontrol edebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model (varsayılan: yok) |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model (varsayılan: yok) |
| `pos_embeds.` | FLOAT | Evet | 0.0 ile 1.0 arası | Konumsal gömme harmanlama ağırlığı (varsayılan: 1.0) |
| `img_in.` | FLOAT | Evet | 0.0 ile 1.0 arası | Görüntü giriş işleme harmanlama ağırlığı (varsayılan: 1.0) |
| `txt_norm.` | FLOAT | Evet | 0.0 ile 1.0 arası | Metin normalizasyonu harmanlama ağırlığı (varsayılan: 1.0) |
| `txt_in.` | FLOAT | Evet | 0.0 ile 1.0 arası | Metin giriş işleme harmanlama ağırlığı (varsayılan: 1.0) |
| `time_text_embed.` | FLOAT | Evet | 0.0 ile 1.0 arası | Zaman ve metin gömme harmanlama ağırlığı (varsayılan: 1.0) |
| `transformer_blocks.0.` ile `transformer_blocks.59.` arası | FLOAT | Evet | 0.0 ile 1.0 arası | Her bir transformer bloğu harmanlama ağırlığı (varsayılan: 1.0) |
| `proj_out.` | FLOAT | Evet | 0.0 ile 1.0 arası | Çıktı projeksiyonu harmanlama ağırlığı (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `model` | MODEL | Belirtilen ağırlıklarla her iki giriş modelinin bileşenlerini birleştiren birleştirilmiş model |

---
**Source fingerprint (SHA-256):** `a0424a3f4d4ffe170471ba463350d741f67ff1b1f5a8a016ad844c111033f97c`
