PairConditioningSetPropertiesAndCombine düğümü, mevcut pozitif ve negatif koşullandırma girdilerine yeni koşullandırma verileri uygulayarak koşullandırma çiftlerini değiştirir ve birleştirir. Uygulanan koşullandırmanın gücünü ayarlamanıza ve koşullandırma alanının nasıl ayarlanacağını kontrol etmenize olanak tanır. Bu düğüm, birden fazla koşullandırma kaynağını bir arada harmanlamanız gereken gelişmiş koşullandırma manipülasyon iş akışları için özellikle kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Orijinal pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Orijinal negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `yeni_pozitif` | Uygulanacak yeni pozitif koşullandırma | CONDITIONING | Evet | - |
| `yeni_negatif` | Uygulanacak yeni negatif koşullandırma | CONDITIONING | Evet | - |
| `güç` | Yeni koşullandırmanın uygulanması için güç faktörü (varsayılan: 1,0) | FLOAT | Evet | 0,0 ila 10,0 |
| `koşul_alanı_ayarla` | Koşullandırma alanının nasıl uygulanacağını kontrol eder (varsayılan: "default") | STRING | Evet | "default"<br>"mask bounds" |
| `maske` | Koşullandırma uygulama alanını sınırlamak için isteğe bağlı maske | MASK | Hayır | - |
| `kancalar` | Gelişmiş kontrol için isteğe bağlı kanca grubu | HOOKS | Hayır | - |
| `zaman_adımları` | İsteğe bağlı zaman adımı aralığı belirtimi | TIMESTEPS_RANGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Birleştirilmiş pozitif koşullandırma çıktısı | CONDITIONING |
| `negatif` | Birleştirilmiş negatif koşullandırma çıktısı | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/tr.md)

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
