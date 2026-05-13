> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/tr.md)

ConditioningSetPropertiesAndCombine düğümü, mevcut bir koşullandırma girdisine yeni bir koşullandırma girdisinden özellikler uygulayarak koşullandırma verilerini değiştirir. Yeni koşullandırmanın gücünü kontrol ederken ve koşullandırma alanının nasıl uygulanacağını belirtirken iki koşullandırma kümesini birleştirir.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `koşul` | CONDITIONING | Zorunlu | - | - | Değiştirilecek orijinal koşullandırma verileri |
| `yeni_koşul` | CONDITIONING | Zorunlu | - | - | Uygulanacak özellikleri sağlayan yeni koşullandırma verileri |
| `güç` | FLOAT | Zorunlu | 1.0 | 0.0 - 10.0 | Yeni koşullandırma özelliklerinin yoğunluğunu kontrol eder |
| `koşul_alanı_ayarla` | STRING | Zorunlu | default | ["default", "mask bounds"] | Koşullandırma alanının nasıl uygulanacağını belirler |
| `maske` | MASK | İsteğe bağlı | - | - | Koşullandırma için belirli alanları tanımlamak üzere isteğe bağlı maske |
| `kancalar` | HOOKS | İsteğe bağlı | - | - | Özel işleme için isteğe bağlı kanca işlevleri |
| `zaman_adımları` | TIMESTEPS_RANGE | İsteğe bağlı | - | - | Koşullandırmanın ne zaman uygulanacağını kontrol etmek için isteğe bağlı zaman adımı aralığı |

**Not:** `mask` sağlandığında, `set_cond_area` parametresi "mask bounds" kullanarak koşullandırma uygulamasını maskelenmiş bölgelerle sınırlayabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilmiş özelliklerle birleştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
