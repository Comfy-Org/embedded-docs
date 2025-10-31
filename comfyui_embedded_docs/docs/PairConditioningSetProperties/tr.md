> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/tr.md)

PairConditioningSetProperties düğümü, hem pozitif hem de negatif koşullandırma çiftlerinin özelliklerini aynı anda değiştirmenize olanak tanır. Her iki koşullandırma girişine güç ayarlamaları, koşullandırma alanı ayarları ve isteğe bağlı maskeleme veya zamanlama kontrolleri uygular ve değiştirilmiş pozitif ve negatif koşullandırma verilerini döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive_NEW` | CONDITIONING | Evet | - | Değiştirilecek pozitif koşullandırma girişi |
| `negative_NEW` | CONDITIONING | Evet | - | Değiştirilecek negatif koşullandırma girişi |
| `strength` | FLOAT | Evet | 0.0 - 10.0 | Koşullandırmaya uygulanan güç çarpanı (varsayılan: 1.0) |
| `set_cond_area` | STRING | Evet | "default"<br>"mask bounds" | Koşullandırma alanının nasıl hesaplandığını belirler |
| `mask` | MASK | Hayır | - | Koşullandırma alanını kısıtlamak için isteğe bağlı maske |
| `hooks` | HOOKS | Hayır | - | Gelişmiş koşullandırma değişiklikleri için isteğe bağlı kanca grubu |
| `timesteps` | TIMESTEPS_RANGE | Hayır | - | Koşullandırmanın ne zaman uygulanacağını sınırlamak için isteğe bağlı zaman adımı aralığı |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Uygulanan özelliklere sahip değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Uygulanan özelliklere sahip değiştirilmiş negatif koşullandırma |