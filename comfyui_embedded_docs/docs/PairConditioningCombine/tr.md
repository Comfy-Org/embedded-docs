> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/tr.md)

PairConditioningCombine düğümü, iki ayrı koşullandırma çiftini (her biri bir pozitif ve bir negatif koşullandırmadan oluşur) tek bir birleşik çift halinde birleştirir. İki farklı kaynaktan gelen pozitif ve negatif koşullandırmaları alır ve ComfyUI'nin dahili mantığını kullanarak birleştirir; çıktı olarak tek bir nihai pozitif ve tek bir nihai negatif koşullandırma üretir. Bu düğüm deneyseldir ve ileri düzey koşullandırma manipülasyonu iş akışları için tasarlanmıştır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif_A` | CONDITIONING | Evet | - | Birinci pozitif koşullandırma girişi |
| `negatif_A` | CONDITIONING | Evet | - | Birinci negatif koşullandırma girişi |
| `pozitif_B` | CONDITIONING | Evet | - | İkinci pozitif koşullandırma girişi |
| `negatif_B` | CONDITIONING | Evet | - | İkinci negatif koşullandırma girişi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `negatif` | CONDITIONING | Birleştirilmiş pozitif koşullandırma çıktısı |
| `negative` | CONDITIONING | Birleştirilmiş negatif koşullandırma çıktısı |

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
