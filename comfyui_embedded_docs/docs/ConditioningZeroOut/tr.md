> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/tr.md)

Bu düğüm, koşullandırma veri yapısı içindeki belirli öğeleri sıfırlayarak, bunların sonraki işlem adımlarındaki etkisini etkisiz hale getirir. Koşullandırmanın dahili temsilinin doğrudan manipülasyonunun gerekli olduğu gelişmiş koşullandırma işlemleri için tasarlanmıştır.

## Girdiler

| Parametre | Comfy dtype                | Açıklama |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilecek koşullandırma veri yapısı. Bu düğüm, her bir koşullandırma girişi içindeki 'pooled_output' öğelerini, eğer mevcutsa, sıfırlar. |

## Çıktılar

| Parametre | Comfy dtype                | Açıklama |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilmiş koşullandırma veri yapısı; uygulanabilir olduğu durumlarda 'pooled_output' öğeleri sıfıra ayarlanmış halde. |