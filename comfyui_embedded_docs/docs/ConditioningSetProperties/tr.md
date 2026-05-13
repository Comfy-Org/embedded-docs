> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/tr.md)

**ConditioningSetProperties** düğümü, güç, alan ayarları ve isteğe bağlı maskeler, kancalar veya zaman adımı aralıkları uygulayarak koşullandırma verilerinin özelliklerini değiştirir. Görüntü oluşturma sırasında koşullandırma verilerinin uygulanmasını etkileyen belirli parametreler ayarlayarak, koşullandırmanın üretim sürecini nasıl etkileyeceğini kontrol etmenizi sağlar.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `cond_NEW` | CONDITIONING | Zorunlu | - | - | Değiştirilecek koşullandırma verileri |
| `strength` | FLOAT | Zorunlu | 1.0 | 0.0 - 10.0 (adım: 0.01) | Koşullandırma etkisinin yoğunluğunu kontrol eder |
| `set_cond_area` | STRING | Zorunlu | default | ["default", "mask bounds"] | Koşullandırma alanının nasıl uygulanacağını belirler. Standart davranış için "default" veya maske bölgesiyle sınırlamak için "mask bounds" seçeneğini kullanın |
| `mask` | MASK | İsteğe bağlı | - | - | Koşullandırmanın uygulanacağı alanı kısıtlamak için isteğe bağlı maske |
| `hooks` | HOOKS | İsteğe bağlı | - | - | Özel işleme için isteğe bağlı kanca işlevleri |
| `timesteps` | TIMESTEPS_RANGE | İsteğe bağlı | - | - | Koşullandırmanın ne zaman etkin olacağını sınırlamak için isteğe bağlı zaman adımı aralığı |

**Not:** Bir `mask` sağlandığında, `set_cond_area` parametresi "mask bounds" olarak ayarlanarak koşullandırma uygulaması yalnızca maskelenmiş bölgeyle sınırlandırılabilir. `hooks` parametresi, kanca işlevleri aracılığıyla özel işlemeye olanak tanır ve `timesteps`, koşullandırma etkisini oluşturma sırasında belirli bir zaman adımı aralığıyla sınırlar.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Güncellenmiş özelliklere sahip değiştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
