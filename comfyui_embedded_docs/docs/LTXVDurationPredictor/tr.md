# LTXV Süre Tahmin Edici

Bu düğüm, bir istem için doğal çekim süresini LTX 2.4 süre başını kullanarak tahmin eder. Tahmin edilen süreyi, VAE'nin kare ızgarasına uyan bir kare sayısına dönüştürür; bu işlemde sağlanan kare hızı ve minimum/maksimum süre sınırları kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Metin yerleştirmelerini ön işlemek ve süre başını çalıştırmak için kullanılan model. | MODEL | Evet | N/A |
| `pozitif` | Süre tahmini için istemin metin yerleştirmelerini ve meta verilerini sağlayan koşullandırma. | CONDITIONING | Evet | N/A |
| `duration_head` | ModelPatchLoader ile yüklenen LTX 2.4 süre başı. Bir LTX süre başı olmalıdır. | MODEL_PATCH | Evet | N/A |
| `kare_hızı` | Saniyeleri karelere dönüştürmek için kullanılan saniye başına kare hızı (varsayılan: 24.0). | FLOAT | Evet | 1.0 ile 120.0 |
| `min_saniye` | Tahmini bir kare sayısına dönüştürürken kullanılan saniye cinsinden minimum süre (varsayılan: 1.0). | FLOAT | Evet | 0.5 ile 120.0 |
| `maks_saniye` | Tahmini bir kare sayısına dönüştürürken kullanılan saniye cinsinden maksimum süre (varsayılan: 20.0). | FLOAT | Evet | 0.5 ile 120.0 |

Not: `duration_head` girdisi, ModelPatchLoader ile yüklenmiş bir LTX 2.4 süre başı olmalıdır. Bağlı model yaması bir LTX süre başı değilse, düğüm bir ValueError hatası oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `kare_sayısı` | Tahmin edilen sürenin kare sayısına dönüştürülmüş ve VAE'nin 8k+1 kare ızgarasına oturtulmuş hali. | INT |
| `saniye` | Ham (sınırlandırılmamış) tahmini süre. Kare ızgarasına oturtulmadan önceki değerdir. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/tr.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
