> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/tr.md)

ConditioningSetProperties düğümü, koşullandırma verilerinin özelliklerini güç, alan ayarlarını ayarlayarak ve isteğe bağlı maskeler veya zaman adımı aralıkları uygulayarak değiştirir. Görüntü oluşturma sırasında koşullandırma verilerinin uygulanmasını etkileyen belirli parametreleri ayarlayarak koşullandırmanın üretim sürecini nasıl etkilediğini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `yeni_koşul` | CONDITIONING | Gerekli | - | - | Değiştirilecek koşullandırma verisi |
| `güç` | FLOAT | Gerekli | 1.0 | 0.0-10.0 | Koşullandırma etkisinin yoğunluğunu kontrol eder |
| `koşul_alanı_ayarla` | STRING | Gerekli | default | ["default", "mask bounds"] | Koşullandırma alanının nasıl uygulanacağını belirler |
| `maske` | MASK | İsteğe Bağlı | - | - | Koşullandırmanın nerede uygulanacağını kısıtlamak için isteğe bağlı maske |
| `kancalar` | HOOKS | İsteğe Bağlı | - | - | Özel işleme için isteğe bağlı kanca fonksiyonları |
| `zaman_adımları` | TIMESTEPS_RANGE | İsteğe Bağlı | - | - | Koşullandırmanın ne zaman aktif olacağını sınırlamak için isteğe bağlı zaman adımı aralığı |

**Not:** Bir `mask` sağlandığında, `set_cond_area` parametresi, koşullandırma uygulamasını yalnızca maskelenmiş bölgeyle kısıtlamak için "mask bounds" olarak ayarlanabilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Güncellenmiş özelliklere sahip değiştirilmiş koşullandırma verisi |