> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/tr.md)

VAEEncodeTiled düğümü, görüntüleri daha küçük karolara bölerek ve bunları bir Varyasyonel Otokodlayıcı kullanarak kodlayarak işler. Bu karo tabanlı yaklaşım, aksi takdirde bellek sınırlarını aşabilecek büyük görüntülerin işlenmesine olanak tanır. Düğüm, hem görüntü hem de video VAE'lerini destekler ve mekansal ve zamansal boyutlar için ayrı karo kontrolü sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pixels` | IMAGE | Evet | - | Kodlanacak giriş görüntü verisi |
| `vae` | VAE | Evet | - | Kodlama için kullanılan Varyasyonel Otokodlayıcı modeli |
| `tile_size` | INT | Evet | 64-4096 (adım: 64) | Mekansal işleme için her bir karonun boyutu (varsayılan: 512) |
| `overlap` | INT | Evet | 0-4096 (adım: 32) | Bitişik karolar arasındaki örtüşme miktarı (varsayılan: 64) |
| `temporal_size` | INT | Evet | 8-4096 (adım: 4) | Sadece video VAE'ler için kullanılır: Aynı anda kodlanacak kare miktarı (varsayılan: 64) |
| `temporal_overlap` | INT | Evet | 4-4096 (adım: 4) | Sadece video VAE'ler için kullanılır: Örtüşecek kare miktarı (varsayılan: 8) |

**Not:** `temporal_size` ve `temporal_overlap` parametreleri sadece video VAE'leri kullanılırken geçerlidir ve standart görüntü VAE'leri üzerinde herhangi bir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Giriş görüntüsünün kodlanmış gizli temsili |