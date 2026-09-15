# Boş YuE2 Latent Ses

Bu düğüm, YuE2 için seçilen süre ve toplu iş sayısına göre boyutlandırılmış boş bir ses latent'i oluşturur. Daha sonraki düğümlerin ses üretimi sırasında doldurabileceği sessiz yer tutucu ses verisi üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Oluşturulacak ses latent'inin saniye cinsinden uzunluğu (varsayılan: 120.0). Latent kare sayısı bu değerden hesaplanır; en az 1 karedir. | FLOAT | Evet | 0.04 - 1000.0 (adım 0.04) |
| `batch_size` | Tek bir toplu işte oluşturulacak ses latent'i sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `LATENT` | `batch_size` ve `seconds` değerinden türetilen kare sayısına göre boyutlandırılmış, sıfırlardan oluşan bir tensör içeren boş bir ses latent'i. 1920 zamansal küçültme oranıyla ses türü olarak etiketlenir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/tr.md)

---
**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`
