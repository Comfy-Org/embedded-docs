> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/tr.md)

ModelMergeQwenImage düğümü, iki yapay zeka modelini bileşenlerini ayarlanabilir ağırlıklarla birleştirerek birleştirir. Qwen görüntü modellerinin belirli bölümlerini (dönüştürücü blokları, konumsal yerleştirmeler ve metin işleme bileşenleri dahil) harmanlamanıza olanak tanır. Birleştirilmiş sonucun farklı bölümlerinde her bir modelin ne kadar etkili olacağını kontrol edebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Evet | - | Birleştirilecek ilk model (varsayılan: yok) |
| `model2` | MODEL | Evet | - | Birleştirilecek ikinci model (varsayılan: yok) |
| `pos_embeds.` | FLOAT | Evet | 0.0 - 1.0 | Konumsal yerleştirmelerin harmanlanması için ağırlık (varsayılan: 1.0) |
| `img_in.` | FLOAT | Evet | 0.0 - 1.0 | Görüntü girişi işleme harmanlaması için ağırlık (varsayılan: 1.0) |
| `txt_norm.` | FLOAT | Evet | 0.0 - 1.0 | Metin normalleştirme harmanlaması için ağırlık (varsayılan: 1.0) |
| `txt_in.` | FLOAT | Evet | 0.0 - 1.0 | Metin girişi işleme harmanlaması için ağırlık (varsayılan: 1.0) |
| `time_text_embed.` | FLOAT | Evet | 0.0 - 1.0 | Zaman ve metin yerleştirme harmanlaması için ağırlık (varsayılan: 1.0) |
| `transformer_blocks.0.` - `transformer_blocks.59.` | FLOAT | Evet | 0.0 - 1.0 | Her bir dönüştürücü bloğun harmanlanması için ağırlık (varsayılan: 1.0) |
| `proj_out.` | FLOAT | Evet | 0.0 - 1.0 | Çıkış projeksiyonu harmanlaması için ağırlık (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Belirtilen ağırlıklarla her iki girdi modelinden bileşenlerin birleştirildiği birleştirilmiş model |