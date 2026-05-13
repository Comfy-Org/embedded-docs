> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/tr.md)

**PairConditioningSetProperties** düğümü, hem pozitif hem de negatif koşullandırma çiftlerinin özelliklerini aynı anda değiştirmenize olanak tanır. Her iki koşullandırma girdisine güç ayarlamaları, koşullandırma alanı ayarları ve isteğe bağlı maskeleme veya zamanlama kontrolleri uygulayarak, değiştirilmiş pozitif ve negatif koşullandırma verilerini döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `yeni_pozitif` | CONDITIONING | Evet | - | Değiştirilecek pozitif koşullandırma girdisi |
| `yeni_negatif` | CONDITIONING | Evet | - | Değiştirilecek negatif koşullandırma girdisi |
| `güç` | FLOAT | Evet | 0.0 - 10.0 | Koşullandırmaya uygulanan güç çarpanı (varsayılan: 1.0) |
| `koşul_alanı_ayarla` | STRING | Evet | "default"<br>"mask bounds" | Koşullandırma alanının nasıl hesaplanacağını belirler (varsayılan: "default") |
| `maske` | MASK | Hayır | - | Koşullandırma alanını sınırlamak için isteğe bağlı maske |
| `kancalar` | HOOKS | Hayır | - | Gelişmiş koşullandırma değişiklikleri için isteğe bağlı kanca grubu |
| `zaman_adımları` | TIMESTEPS_RANGE | Hayır | - | Koşullandırmanın ne zaman uygulanacağını sınırlamak için isteğe bağlı zaman adımı aralığı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Uygulanan özelliklerle birlikte değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Uygulanan özelliklerle birlikte değiştirilmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
