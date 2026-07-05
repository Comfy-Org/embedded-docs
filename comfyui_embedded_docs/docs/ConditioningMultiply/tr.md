# ConditioningMultiply

Bu düğüm, koşullandırma değerlerini belirtilen bir faktörle çarparak, koşullandırmanın üretim süreci üzerindeki etkisini ölçeklendirmenizi sağlar. Çarpanı hem ana koşullandırma tensörüne hem de havuzlanmış çıktı değerlerine uygulayarak çalışır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Ölçeklendirilecek koşullandırma verisi | CONDITIONING | Evet | - |
| `multiplier` | Koşullandırma değerlerinin çarpılacağı faktör (varsayılan: 1.0) | FLOAT | Evet | -100.0 ile 100.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Değerleri çarpılmış, ölçeklendirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/tr.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
