> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/tr.md)

EmptyAceStepLatentAudio düğümü, belirtilen sürede boş latent ses örnekleri oluşturur. Giriş saniyeleri ve ses işleme parametrelerine göre hesaplanan uzunlukta, sıfırlarla dolu bir sessiz latent ses grubu üretir. Bu düğüm, latent temsiller gerektiren ses işleme iş akışlarını başlatmak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Evet | 1.0 - 1000.0 | Sesin saniye cinsinden süresi (varsayılan: 120.0) |
| `batch_size` | INT | Evet | 1 - 4096 | Gruptaki latent görüntü sayısı (varsayılan: 1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Sıfırlarla dolu boş latent ses örneklerini döndürür. Çıkış, bir `samples` tensörü ve "audio" olarak ayarlanmış bir `type` alanı içerir. |

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
