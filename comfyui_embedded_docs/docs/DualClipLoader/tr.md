> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/tr.md)

DualCLIPLoader düğümü, iki CLIP modelini aynı anda yüklemek için tasarlanmıştır ve her iki modelin özelliklerinin entegrasyonunu veya karşılaştırılmasını gerektiren işlemleri kolaylaştırır.

Bu düğüm, `ComfyUI/models/text_encoders` klasöründe bulunan modelleri tespit edecektir.

## Girdiler

| Parametre   | Comfy Veri Türü | Açıklama                                                                                                                                                                                   |
| ----------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `clip_adı1` | COMBO[STRING] | Yüklenecek ilk CLIP modelinin adını belirtir. Bu parametre, önceden tanımlanmış mevcut CLIP modelleri listesinden doğru modelin tanımlanması ve alınması için çok önemlidir.               |
| `clip_adı2` | COMBO[STRING] | Yüklenecek ikinci CLIP modelinin adını belirtir. Bu parametre, ilk modelin yanında karşılaştırmalı veya bütünleştirici analiz için ikinci bir farklı CLIP modelinin yüklenmesini sağlar. |
| `tür`      | `option`        | Farklı modellere uyum sağlamak için "sdxl", "sd3", "flux" arasından seçim yapın.                                                                                                           |

* Yükleme sırası çıktı etkisini etkilemez

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                                                                              |
| --------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `clip`    | CLIP      | Çıktı, belirtilen iki CLIP modelinin özelliklerini veya işlevselliğini birleştiren birleşik bir CLIP modelidir.                       |