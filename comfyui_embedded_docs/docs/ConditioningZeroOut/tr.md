# KoşullandırmaSıfırla

Bu düğüm, koşullandırma veri yapısı içindeki belirli öğeleri sıfırlayarak, bunların sonraki işleme adımlarındaki etkisini etkili bir şekilde ortadan kaldırır. Koşullandırmanın dahili temsilinin doğrudan manipülasyonunun gerektiği ileri düzey koşullandırma işlemleri için tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `CONDITIONING` | Değiştirilecek koşullandırma veri yapısı. Bu düğüm, varsa her koşullandırma girişindeki 'pooled_output' öğelerini sıfırlar. | CONDITIONING |

## Çıkışlar

| Parametre | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `CONDITIONING` | 'pooled_output' öğelerinin uygun yerlerde sıfırlandığı, değiştirilmiş koşullandırma veri yapısı. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/tr.md)
