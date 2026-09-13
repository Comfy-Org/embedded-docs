# ModelÖrneklemeStabilKaskad

ModelSamplingStableCascade düğümü, örnekleme parametrelerine bir shift değeri uygulayarak bir modele Stable Cascade örnekleme ayarlarını uygular. Orijinal modeli değiştirmeden, özel Stable Cascade örnekleme yapılandırmasına sahip girdi modelinin yamalı bir kopyasını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Stable Cascade örneklemesinin uygulanacağı girdi modeli | MODEL | Evet | - |
| `shift` | Örnekleme parametrelerine uygulanan shift değeri (varsayılan: 2.0) | FLOAT | Evet | 0.0 - 100.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Stable Cascade örneklemesi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/tr.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
