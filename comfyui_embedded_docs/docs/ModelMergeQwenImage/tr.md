# ModelBirleştirmeQwenGörsel

Bu düğüm, iki Qwen görüntü modelini, tek tek bileşenlerini ayarlanabilir ağırlıklarla harmanlayarak birleştirir. Her ağırlık, ikinci modelin karşılık gelen bölümünün birleştirilmiş sonuca ne kadar katkıda bulunacağını kontrol eder; böylece konumsal gömmeleri, metin işleme katmanlarını, görüntü girdisi katmanlarını, 60 transformer bloğunun tamamını ve çıktı projeksiyonunu ayrı ayrı karıştırabilirsiniz. Nihai sonuç, normal bir modelin beklendiği her yerde kullanabileceğiniz tek bir MODEL'dir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `pos_embeds.` | Konumsal gömmelerin harmanlanması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `img_in.` | Görüntü girdisi işlemenin harmanlanması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `txt_norm.` | Metin normalleştirmenin harmanlanması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `txt_in.` | Metin girdisi işlemenin harmanlanması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `time_text_embed.` | Zaman ve metin gömmesinin harmanlanması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `transformer_blocks.0.` ile `transformer_blocks.59.` | Her transformer bloğunun harmanlanması için ağırlık (varsayılan: 1.0). Düğüm, 60 transformer bloğunun her biri için bir ağırlık sunar. | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |
| `proj_out.` | Çıktı projeksiyonunun harmanlanması için ağırlık (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (step: 0.01) |

Not: Tüm ağırlık girdileri gereklidir ve aynı sınırları paylaşır — varsayılan 1.0, geçerli aralık 0.0 ile 1.0 arasıdır ve 0.01 adımlarla ayarlanabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Belirtilen ağırlıklarla her iki girdi modelinin bileşenlerini birleştiren harmanlanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/tr.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
