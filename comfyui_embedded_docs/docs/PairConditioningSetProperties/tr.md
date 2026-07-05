# Koşul Çifti Özelliklerini Ayarla

**PairConditioningSetProperties** düğümü, hem pozitif hem de negatif koşullandırma çiftlerinin özelliklerini aynı anda değiştirmenize olanak tanır. Her iki koşullandırma girdisine güç ayarlamaları, koşullandırma alanı ayarları ve isteğe bağlı maskeleme veya zamanlama kontrolleri uygulayarak, değiştirilmiş pozitif ve negatif koşullandırma verilerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `yeni_pozitif` | Değiştirilecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `yeni_negatif` | Değiştirilecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `güç` | Koşullandırmaya uygulanan güç çarpanı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `koşul_alanı_ayarla` | Koşullandırma alanının nasıl hesaplanacağını belirler (varsayılan: "default") | STRING | Evet | "default"<br>"mask bounds" |
| `maske` | Koşullandırma alanını sınırlamak için isteğe bağlı maske | MASK | Hayır | - |
| `kancalar` | Gelişmiş koşullandırma değişiklikleri için isteğe bağlı kanca grubu | HOOKS | Hayır | - |
| `zaman_adımları` | Koşullandırmanın ne zaman uygulanacağını sınırlamak için isteğe bağlı zaman adımı aralığı | TIMESTEPS_RANGE | Hayır | - |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Uygulanan özelliklerle birlikte değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Uygulanan özelliklerle birlikte değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/tr.md)

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
