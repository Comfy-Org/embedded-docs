> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/tr.md)

EmptyHunyuanImageLatent düğümü, Hunyuan görüntü oluşturma modelleriyle kullanılmak üzere belirli boyutlarda boş bir latent tensör oluşturur. İş akışındaki sonraki düğümlerde işlenebilecek boş bir başlangıç noktası oluşturur. Bu düğüm, latent uzayın genişlik, yükseklik ve batch boyutunu belirtmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Evet | 64 - MAX_RESOLUTION | Oluşturulan latent görüntünün piksel cinsinden genişliği (varsayılan: 2048, adım: 32) |
| `height` | INT | Evet | 64 - MAX_RESOLUTION | Oluşturulan latent görüntünün piksel cinsinden yüksekliği (varsayılan: 2048, adım: 32) |
| `batch_size` | INT | Evet | 1 - 4096 | Bir batch içinde oluşturulacak latent örneklerinin sayısı (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Hunyuan görüntü işleme için belirtilen boyutlarda boş bir latent tensör |