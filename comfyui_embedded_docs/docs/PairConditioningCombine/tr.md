# Koşul Çifti Birleştir

PairConditioningCombine düğümü, iki ayrı koşullandırma çiftini (her biri bir pozitif ve bir negatif koşullandırmadan oluşur) tek bir birleşik çift halinde birleştirir. İki farklı kaynaktan gelen pozitif ve negatif koşullandırmaları alır ve ComfyUI'nin dahili mantığını kullanarak birleştirir; çıktı olarak tek bir nihai pozitif ve tek bir nihai negatif koşullandırma üretir. Bu düğüm deneyseldir ve ileri düzey koşullandırma manipülasyonu iş akışları için tasarlanmıştır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif_A` | Birinci pozitif koşullandırma girişi | CONDITIONING | Evet | - |
| `negatif_A` | Birinci negatif koşullandırma girişi | CONDITIONING | Evet | - |
| `pozitif_B` | İkinci pozitif koşullandırma girişi | CONDITIONING | Evet | - |
| `negatif_B` | İkinci negatif koşullandırma girişi | CONDITIONING | Evet | - |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Birleştirilmiş pozitif koşullandırma çıktısı | CONDITIONING |
| `negative` | Birleştirilmiş negatif koşullandırma çıktısı | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/tr.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
