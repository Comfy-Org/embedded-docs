> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/tr.md)

PairConditioningSetPropertiesAndCombine düğümü, mevcut pozitif ve negatif koşullandırma girdilerine yeni koşullandırma verileri uygulayarak koşullandırma çiftlerini değiştirir ve birleştirir. Uygulanan koşullandırmanın gücünü ayarlamanıza ve koşullandırma alanının nasıl ayarlanacağını kontrol etmenize olanak tanır. Bu düğüm, birden fazla koşullandırma kaynağını bir arada harmanlamanız gereken gelişmiş koşullandırma manipülasyon iş akışları için özellikle kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|-----------|
| `pozitif` | CONDITIONING | Evet | - | Orijinal pozitif koşullandırma girdisi |
| `negatif` | CONDITIONING | Evet | - | Orijinal negatif koşullandırma girdisi |
| `yeni_pozitif` | CONDITIONING | Evet | - | Uygulanacak yeni pozitif koşullandırma |
| `yeni_negatif` | CONDITIONING | Evet | - | Uygulanacak yeni negatif koşullandırma |
| `güç` | FLOAT | Evet | 0,0 ila 10,0 | Yeni koşullandırmanın uygulanması için güç faktörü (varsayılan: 1,0) |
| `koşul_alanı_ayarla` | STRING | Evet | "default"<br>"mask bounds" | Koşullandırma alanının nasıl uygulanacağını kontrol eder (varsayılan: "default") |
| `maske` | MASK | Hayır | - | Koşullandırma uygulama alanını sınırlamak için isteğe bağlı maske |
| `kancalar` | HOOKS | Hayır | - | Gelişmiş kontrol için isteğe bağlı kanca grubu |
| `zaman_adımları` | TIMESTEPS_RANGE | Hayır | - | İsteğe bağlı zaman adımı aralığı belirtimi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-----------|
| `negatif` | CONDITIONING | Birleştirilmiş pozitif koşullandırma çıktısı |
| `negatif` | CONDITIONING | Birleştirilmiş negatif koşullandırma çıktısı |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
