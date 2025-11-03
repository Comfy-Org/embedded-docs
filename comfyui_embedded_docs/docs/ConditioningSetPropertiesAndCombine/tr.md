> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/tr.md)

ConditioningSetPropertiesAndCombine düğümü, yeni bir koşullandırma girişinden gelen özellikleri mevcut bir koşullandırma girişine uygulayarak koşullandırma verilerini değiştirir. İki koşullandırma kümesini birleştirirken, yeni koşullandırmanın gücünü kontrol eder ve koşullandırma alanının nasıl uygulanacağını belirtir.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `koşul` | CONDITIONING | Gerekli | - | - | Değiştirilecek orijinal koşullandırma verisi |
| `yeni_koşul` | CONDITIONING | Gerekli | - | - | Uygulanacak özellikleri sağlayan yeni koşullandırma verisi |
| `güç` | FLOAT | Gerekli | 1.0 | 0.0 - 10.0 | Yeni koşullandırma özelliklerinin yoğunluğunu kontrol eder |
| `koşul_alanı_ayarla` | STRING | Gerekli | default | ["default", "mask bounds"] | Koşullandırma alanının nasıl uygulanacağını belirler |
| `maske` | MASK | İsteğe Bağlı | - | - | Koşullandırma için belirli alanları tanımlayan isteğe bağlı maske |
| `kancalar` | HOOKS | İsteğe Bağlı | - | - | Özel işleme için isteğe bağlı kanca fonksiyonları |
| `zaman_adımları` | TIMESTEPS_RANGE | İsteğe Bağlı | - | - | Koşullandırmanın ne zaman uygulanacağını kontrol etmek için isteğe bağlı zaman adımı aralığı |

**Not:** `mask` sağlandığında, `set_cond_area` parametresi, koşullandırma uygulamasını maskelenmiş bölgelere sınırlamak için "mask bounds" kullanabilir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Değiştirilmiş özelliklere sahip birleştirilmiş koşullandırma verisi |