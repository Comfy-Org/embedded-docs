**ConditioningSetProperties** düğümü, güç, alan ayarları ve isteğe bağlı maskeler, kancalar veya zaman adımı aralıkları uygulayarak koşullandırma verilerinin özelliklerini değiştirir. Görüntü oluşturma sırasında koşullandırma verilerinin uygulanmasını etkileyen belirli parametreler ayarlayarak, koşullandırmanın üretim sürecini nasıl etkileyeceğini kontrol etmenizi sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `yeni_koşul` | Değiştirilecek koşullandırma verileri | CONDITIONING | Zorunlu | - | - |
| `güç` | Koşullandırma etkisinin yoğunluğunu kontrol eder | FLOAT | Zorunlu | 1.0 | 0.0 - 10.0 (adım: 0.01) |
| `koşul_alanı_ayarla` | Koşullandırma alanının nasıl uygulanacağını belirler. Standart davranış için "default" veya maske bölgesiyle sınırlamak için "mask bounds" seçeneğini kullanın | STRING | Zorunlu | default | ["default", "mask bounds"] |
| `maske` | Koşullandırmanın uygulanacağı alanı kısıtlamak için isteğe bağlı maske | MASK | İsteğe bağlı | - | - |
| `kancalar` | Özel işleme için isteğe bağlı kanca işlevleri | HOOKS | İsteğe bağlı | - | - |
| `zaman_adımları` | Koşullandırmanın ne zaman etkin olacağını sınırlamak için isteğe bağlı zaman adımı aralığı | TIMESTEPS_RANGE | İsteğe bağlı | - | - |

**Not:** Bir `mask` sağlandığında, `set_cond_area` parametresi "mask bounds" olarak ayarlanarak koşullandırma uygulaması yalnızca maskelenmiş bölgeyle sınırlandırılabilir. `hooks` parametresi, kanca işlevleri aracılığıyla özel işlemeye olanak tanır ve `timesteps`, koşullandırma etkisini oluşturma sırasında belirli bir zaman adımı aralığıyla sınırlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Güncellenmiş özelliklere sahip değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/tr.md)

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
