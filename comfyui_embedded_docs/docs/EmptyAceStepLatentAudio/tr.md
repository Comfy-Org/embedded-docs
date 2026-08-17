# BoşAceAdımGizliSes

EmptyAceStepLatentAudio düğümü, belirtilen sürede boş latent ses örnekleri oluşturur. Girdi saniyelerine ve ses işleme parametrelerine göre hesaplanan uzunlukta, sıfırlarla doldurulmuş sessiz ses latentlerinden oluşan bir grup üretir. Bu düğüm, latent temsiller gerektiren ses işleme iş akışlarını başlatmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `seconds` | Sesin saniye cinsinden süresi (varsayılan: 120.0) | FLOAT | Evet | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | Gruptaki latent görüntü sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Sıfırlarla dolu boş latent ses örneklerini döndürür. Çıktı, bir `samples` tensörü ve "audio" olarak ayarlanmış bir `type` alanı içerir. | LATENT |

Not: Latent uzunluğu, `seconds` değerinden dahili 44100 Hz örnekleme hızı kullanılarak `int(seconds × 44100 / 512 / 8)` çerçeve olarak hesaplanır. Elde edilen latent tensörü tamamen sıfırlarla doldurulur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
