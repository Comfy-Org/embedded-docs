# Koşullandırma (Çarpma)

Bu düğüm, koşullandırma vektörlerini bir skaler faktörle çarparak bir koşullandırma girdisinin etkisini ölçeklendirmenizi sağlar. Çarpanı, ana koşullandırma tensörüne ve varsa havuzlanmış çıktıya uygular.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Ölçeklendirilecek koşullandırma verisi | CONDITIONING | Evet | - |
| `multiplier` | Koşullandırmaya uygulanacak ölçeklendirme faktörü (varsayılan: 1.0) | FLOAT | Evet | -100.0 ila 100.0 (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Çarpanın hem ana tensöre hem de havuzlanmış çıktıya uygulanmasıyla elde edilen ölçeklendirilmiş koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/tr.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
