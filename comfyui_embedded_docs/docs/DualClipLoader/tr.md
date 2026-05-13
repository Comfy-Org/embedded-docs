> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/tr.md)

DualCLIPLoader düğümü, iki CLIP modelini aynı anda yüklemek için tasarlanmış olup, her iki modelin özelliklerinin entegrasyonunu veya karşılaştırılmasını gerektiren işlemleri kolaylaştırır.

Bu düğüm, `ComfyUI/models/text_encoders` klasöründe bulunan modelleri algılayacaktır.

## Girişler

| Parametre     | Comfy dtype  | Açıklama                                                                                                                                                          |
| ------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clip_name1`  | COMBO[STRING] | Yüklenecek ilk CLIP modelinin adını belirtir. Bu parametre, mevcut CLIP modellerinin önceden tanımlanmış listesinden doğru modeli tanımlamak ve almak için önemlidir. |
| `clip_name2`  | COMBO[STRING] | Yüklenecek ikinci CLIP modelinin adını belirtir. Bu parametre, ilk modelin yanında karşılaştırmalı veya bütünleşik analiz için ikinci bir farklı CLIP modelinin yüklenmesini sağlar. |
| `type`        | `option`     | Farklı modellere uyum sağlamak için "sdxl", "sd3", "flux" arasından seçim yapın.                                                                                    |

* Yükleme sırası çıktı etkisini etkilemez

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                                                                      |
| --------- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `clip`    | CLIP      | Çıktı, belirtilen iki CLIP modelinin özelliklerini veya işlevlerini entegre eden birleşik bir CLIP modelidir.                 |