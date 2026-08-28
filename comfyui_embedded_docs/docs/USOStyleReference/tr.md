# USOTarzReferansı

USOStyleReference düğümü, CLIP görüş özelliklerini bir model yamasıyla birleştirerek modele stil referansı uygular ve girdi modelinin yamalı bir kopyasını döndürür. Flux modelleri için tasarlanmıştır ve deneysel olarak işaretlenmiştir. Görsel stil bilgisi, modelin metin koşullandırmasıyla birleştirilir, böylece üretimi etkileyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Stil referans yamasının uygulandığı temel model. | MODEL | Evet | - |
| `model_yama` | Referans görüntü özelliklerini kodlamak için kullanılan projeksiyon modelini içeren model yaması. | MODEL_PATCH | Evet | - |
| `clip_vision_çıktısı` | Referans görüntünün CLIP vision işlemesinden çıkarılan kodlanmış görsel özellikler. | CLIP_VISION_OUTPUT | Evet | - |

Not: `clip_vision_output`, tam gizli durumları ve sondan bir önceki gizli durumu sağlayan bir CLIP vision modelinden gelmelidir. Düğüm, sondan 20., sondan 11. ve sondan bir önceki gizli durumları stil yerleştirmesinde birleştirir. `model_patch`, bu görüntü özelliklerini stil yerleştirmesine dönüştüren bir projeksiyon modelini `model` özniteliği aracılığıyla açığa çıkarmalıdır. Örnekleme sırasında, stil yerleştirmesi metin koşullandırmasının başına eklenir, böylece üretimi etkileyebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Stil referans yaması uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/tr.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
