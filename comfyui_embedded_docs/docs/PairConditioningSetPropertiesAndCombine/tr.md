> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/tr.md)

PairConditioningSetPropertiesAndCombine düğümü, mevcut pozitif ve negatif koşullandırma girişlerine yeni koşullandırma verileri uygulayarak koşullandırma çiftlerini değiştirir ve birleştirir. Uygulanan koşullandırmanın gücünü ayarlamanıza ve koşullandırma alanının nasıl ayarlanacağını kontrol etmenize olanak tanır. Bu düğüm, birden fazla koşullandırma kaynağını bir araya getirmeniz gereken gelişmiş koşullandırma manipülasyon iş akışları için özellikle kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Orijinal pozitif koşullandırma girişi |
| `negatif` | CONDITIONING | Evet | - | Orijinal negatif koşullandırma girişi |
| `yeni_pozitif` | CONDITIONING | Evet | - | Uygulanacak yeni pozitif koşullandırma |
| `yeni_negatif` | CONDITIONING | Evet | - | Uygulanacak yeni negatif koşullandırma |
| `güç` | FLOAT | Evet | 0.0 - 10.0 | Yeni koşullandırmanın uygulanma gücü faktörü (varsayılan: 1.0) |
| `koşul_alanı_ayarla` | STRING | Evet | "default"<br>"mask bounds" | Koşullandırma alanının nasıl uygulanacağını kontrol eder |
| `maske` | MASK | Hayır | - | Koşullandırma uygulama alanını kısıtlamak için isteğe bağlı maske |
| `kancalar` | HOOKS | Hayır | - | Gelişmiş kontrol için isteğe bağlı kanca grubu |
| `zaman_adımları` | TIMESTEPS_RANGE | Hayır | - | İsteğe bağlı zaman adımı aralığı belirtimi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `pozitif` | CONDITIONING | Birleştirilmiş pozitif koşullandırma çıkışı |
| `negatif` | CONDITIONING | Birleştirilmiş negatif koşullandırma çıkışı |