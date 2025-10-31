> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/tr.md)

StableCascade_EmptyLatentImage düğümü, Stable Cascade modelleri için boş latent tensörleri oluşturur. Girdi çözünürlüğü ve sıkıştırma ayarlarına bağlı olarak uygun boyutlarda, biri C aşaması diğeri B aşaması için olmak üzere iki ayrı latent temsil üretir. Bu düğüm, Stable Cascade üretim işlem hattı için başlangıç noktasını sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 256 - MAX_RESOLUTION | Çıktı görselinin piksel cinsinden genişliği (varsayılan: 1024, adım: 8) |
| `height` | INT | Evet | 256 - MAX_RESOLUTION | Çıktı görselinin piksel cinsinden yüksekliği (varsayılan: 1024, adım: 8) |
| `compression` | INT | Evet | 4 - 128 | C aşaması için latent boyutları belirleyen sıkıştırma faktörü (varsayılan: 42, adım: 1) |
| `batch_size` | INT | Hayır | 1 - 4096 | Bir toplu işte üretilecek latent örnek sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `stage_c` | LATENT | [batch_size, 16, height//compression, width//compression] boyutlarında C aşaması latent tensörü |
| `stage_b` | LATENT | [batch_size, 4, height//4, width//4] boyutlarında B aşaması latent tensörü |