DualCLIPLoader düğümü, iki CLIP modelini aynı anda yüklemek için tasarlanmış olup, her iki modelin özelliklerinin entegrasyonunu veya karşılaştırılmasını gerektiren işlemleri kolaylaştırır.

Bu düğüm, `ComfyUI/models/text_encoders` klasöründe bulunan modelleri algılayacaktır.

## Girişler

| Parametre | Açıklama | Comfy dtype |
| --- | --- | --- |
| `clip_adı1` | Yüklenecek ilk CLIP modelinin adını belirtir. Bu parametre, mevcut CLIP modellerinin önceden tanımlanmış listesinden doğru modeli tanımlamak ve almak için önemlidir. | COMBO[STRING] |
| `clip_adı2` | Yüklenecek ikinci CLIP modelinin adını belirtir. Bu parametre, ilk modelin yanında karşılaştırmalı veya bütünleşik analiz için ikinci bir farklı CLIP modelinin yüklenmesini sağlar. | COMBO[STRING] |
| `tür` | Farklı modellere uyum sağlamak için "sdxl", "sd3", "flux" arasından seçim yapın. | `option` |

* Yükleme sırası çıktı etkisini etkilemez

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `clip` | Çıktı, belirtilen iki CLIP modelinin özelliklerini veya işlevlerini entegre eden birleşik bir CLIP modelidir. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/tr.md)
