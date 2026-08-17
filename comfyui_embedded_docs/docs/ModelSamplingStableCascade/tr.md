# ModelÖrneklemeStabilKaskad

ModelSamplingStableCascade düğümü, örnekleme parametrelerini bir kaydırma (shift) değeriyle ayarlayarak bir modele Stable Cascade örneklemesi uygular. Giriş modelinin, Stable Cascade üretimi için özel bir örnekleme yapılandırmasına sahip değiştirilmiş bir kopyasını oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Stable Cascade örneklemesinin uygulanacağı giriş modeli | MODEL | Evet | - |
| `shift` | Örnekleme parametrelerine uygulanacak kaydırma değeri (varsayılan: 2.0) | FLOAT | Evet | 0.0 - 100.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Stable Cascade örneklemesi uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/tr.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
