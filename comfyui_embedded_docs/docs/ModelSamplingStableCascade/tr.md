> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/tr.md)

ModelSamplingStableCascade düğümü, örnekleme parametrelerine bir kaydırma değeri uygulayarak bir modele kararlı basamaklı örnekleme uygular. Giriş modelinin, kararlı basamaklı üretim için özel örnekleme yapılandırmasına sahip değiştirilmiş bir sürümünü oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-----------|
| `model` | MODEL | Evet | - | Kararlı basamaklı örneklemenin uygulanacağı giriş modeli |
| `kaydırma` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme parametrelerine uygulanacak kaydırma değeri (varsayılan: 2.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Kararlı basamaklı örnekleme uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `2d0a342fff05434c8fe78999187bd31dbee7deb6f4447759a489102a8ce277de`
