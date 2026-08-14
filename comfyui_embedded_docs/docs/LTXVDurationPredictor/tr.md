# LTXVDurationPredictor

Bu düğüm, bir prompt için LTX 2.4 süre başlığını (duration head) kullanarak çekimin doğal süresini tahmin eder. Tahmin edilen süreyi, VAE'nin kare ızgarasına uyan kare sayısına dönüştürür; kare hızı ile minimum/maksimum süre sınırlarını kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Metin gömmelerini ön işlemede ve süre başlığını çalıştırmada kullanılan model. | MODEL | Evet | N/A |
| `positive` | Süre tahmini için prompt'un metin gömmelerini ve meta verilerini sağlayan koşullandırma. | CONDITIONING | Evet | N/A |
| `duration_head` | ModelPatchLoader ile yüklenen LTX 2.4 süre başlığı. Bir LTX süre başlığı olmalıdır. | MODEL_PATCH | Evet | N/A |
| `frame_rate` | Saniyeyi kareye dönüştürmek için kullanılan saniyedeki kare sayısı cinsinden kare hızı (varsayılan: 24.0). | FLOAT | Evet | 1.0 ila 120.0 |
| `min_seconds` | Tahmini bir kare sayısına dönüştürürken kullanılan saniye cinsinden minimum süre (varsayılan: 1.0). | FLOAT | Evet | 0.5 ila 120.0 |
| `max_seconds` | Tahmini bir kare sayısına dönüştürürken kullanılan saniye cinsinden maksimum süre (varsayılan: 20.0). | FLOAT | Evet | 0.5 ila 120.0 |

Not: `duration_head` girdisi, ModelPatchLoader ile yüklenmiş bir LTX 2.4 süre başlığı olmalıdır. Bağlı model yaması bir LTX süre başlığı değilse, düğüm bir ValueError hatası oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `num_frames` | Tahmin edilen sürenin kare sayısına dönüştürülmüş ve VAE'nin 8k+1 kare ızgarasına hizalanmış hali. | INT |
| `seconds` | Ham (sınırlanmamış) tahmin edilen süre. Kare ızgarasına hizalanmadan önceki değerdir. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/tr.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
