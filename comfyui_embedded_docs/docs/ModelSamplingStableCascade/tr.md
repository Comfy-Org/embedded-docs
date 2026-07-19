# ModelÖrneklemeStabilKaskad

ModelSamplingStableCascade düğümü, örnekleme parametrelerine bir kaydırma değeri uygulayarak bir modele kararlı basamaklı örnekleme uygular. Giriş modelinin, kararlı basamaklı üretim için özel örnekleme yapılandırmasına sahip değiştirilmiş bir sürümünü oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kararlı basamaklı örneklemenin uygulanacağı giriş modeli | MODEL | Evet | - |
| `kaydırma` | Örnekleme parametrelerine uygulanacak kaydırma değeri (varsayılan: 2.0) | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Kararlı basamaklı örnekleme uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/tr.md)

---
**Source fingerprint (SHA-256):** `2d0a342fff05434c8fe78999187bd31dbee7deb6f4447759a489102a8ce277de`
