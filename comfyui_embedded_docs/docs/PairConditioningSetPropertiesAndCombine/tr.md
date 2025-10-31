> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/tr.md)

PairConditioningSetPropertiesAndCombine düğümü, mevcut pozitif ve negatif koşullandırma girişlerine yeni koşullandırma verileri uygulayarak koşullandırma çiftlerini değiştirir ve birleştirir. Uygulanan koşullandırmanın gücünü ayarlamanıza ve koşullandırma alanının nasıl ayarlanacağını kontrol etmenize olanak tanır. Bu düğüm, birden fazla koşullandırma kaynağını bir araya getirmeniz gereken gelişmiş koşullandırma manipülasyon iş akışları için özellikle kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Orijinal pozitif koşullandırma girişi |
| `negative` | CONDITIONING | Evet | - | Orijinal negatif koşullandırma girişi |
| `positive_NEW` | CONDITIONING | Evet | - | Uygulanacak yeni pozitif koşullandırma |
| `negative_NEW` | CONDITIONING | Evet | - | Uygulanacak yeni negatif koşullandırma |
| `strength` | FLOAT | Evet | 0.0 - 10.0 | Yeni koşullandırmanın uygulanma gücü faktörü (varsayılan: 1.0) |
| `set_cond_area` | STRING | Evet | "default"<br>"mask bounds" | Koşullandırma alanının nasıl uygulanacağını kontrol eder |
| `mask` | MASK | Hayır | - | Koşullandırma uygulama alanını kısıtlamak için isteğe bağlı maske |
| `hooks` | HOOKS | Hayır | - | Gelişmiş kontrol için isteğe bağlı kanca grubu |
| `timesteps` | TIMESTEPS_RANGE | Hayır | - | İsteğe bağlı zaman adımı aralığı belirtimi |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Birleştirilmiş pozitif koşullandırma çıkışı |
| `negative` | CONDITIONING | Birleştirilmiş negatif koşullandırma çıkışı |