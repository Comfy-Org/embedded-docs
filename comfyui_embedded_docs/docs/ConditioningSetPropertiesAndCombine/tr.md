# Koşul Özelliklerini Ayarla ve Birleştir

ConditioningSetPropertiesAndCombine düğümü, mevcut bir koşullandırma girdisine yeni bir koşullandırma girdisinden özellikler uygulayarak koşullandırma verilerini değiştirir. Yeni koşullandırmanın gücünü kontrol ederken ve koşullandırma alanının nasıl uygulanacağını belirtirken iki koşullandırma kümesini birleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `koşul` | Değiştirilecek orijinal koşullandırma verileri | CONDITIONING | Zorunlu | - | - |
| `yeni_koşul` | Uygulanacak özellikleri sağlayan yeni koşullandırma verileri | CONDITIONING | Zorunlu | - | - |
| `güç` | Yeni koşullandırma özelliklerinin yoğunluğunu kontrol eder | FLOAT | Zorunlu | 1.0 | 0.0 - 10.0 |
| `koşul_alanı_ayarla` | Koşullandırma alanının nasıl uygulanacağını belirler | STRING | Zorunlu | default | ["default", "mask bounds"] |
| `maske` | Koşullandırma için belirli alanları tanımlamak üzere isteğe bağlı maske | MASK | İsteğe bağlı | - | - |
| `kancalar` | Özel işleme için isteğe bağlı kanca işlevleri | HOOKS | İsteğe bağlı | - | - |
| `zaman_adımları` | Koşullandırmanın ne zaman uygulanacağını kontrol etmek için isteğe bağlı zaman adımı aralığı | TIMESTEPS_RANGE | İsteğe bağlı | - | - |

**Not:** `mask` sağlandığında, `set_cond_area` parametresi "mask bounds" kullanarak koşullandırma uygulamasını maskelenmiş bölgelerle sınırlayabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Değiştirilmiş özelliklerle birleştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/tr.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
