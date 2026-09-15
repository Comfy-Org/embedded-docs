# USOTarzReferansı

USOStyleReference düğümü, CLIP görüntü özelliklerini bir model yamasıyla birleştirerek bir modele stil referansı uygular ve girdi modelinin yamalanmış bir kopyasını döndürür. Görsel stil bilgisi, üretimi etkileyebilmesi için modelin metin koşullandırmasıyla birleştirilir. Bu düğüm Flux modelleri için tasarlanmıştır ve deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Stil referansı yamasının uygulandığı temel model. | MODEL | Evet | - |
| `model_yama` | Referans görüntü özelliklerini kodlamak için kullanılan projeksiyon modelini içeren model yaması. | MODEL_PATCH | Evet | - |
| `clip_vision_çıktısı` | Referans görüntünün CLIP görüntü işlemesinden çıkarılan kodlanmış görsel özellikler. | CLIP_VISION_OUTPUT | Evet | - |

Not: `clip_vision_output`, tam gizli durumları ve sondan bir önceki gizli durumu sağlayan bir CLIP görüntü modelinden gelmelidir. Düğüm, sondan 20., sondan 11. ve sondan bir önceki gizli durumları stil gömülmesinde birleştirir. `model_patch`, bu görüntü özelliklerini stil gömülmesine dönüştüren bir projeksiyon modelini `model` özniteliği aracılığıyla sunmalıdır. Örnekleme sırasında stil gömülmesi, üretimi etkileyebilmesi için metin koşullandırmasının başına eklenir ve eşleşen sıfır konumlu metin kimlikleri, tanımlayıcı dizisi genişletilmiş koşullandırmayla hizalı kalacak şekilde metin kimliklerinin başına eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Stil referansı yaması uygulanmış değiştirilmiş model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/tr.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
