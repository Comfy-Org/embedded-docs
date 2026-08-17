# VAE Kodlama (Döşemeli)

VAEEncodeTiled düğümü, görüntüleri daha küçük döşemelere bölerek ve bir Varyasyonel Otomatik Kodlayıcı kullanarak kodlayarak işler. Bu döşemeli yaklaşım, aksi takdirde bellek sınırlamalarını aşabilecek büyük görüntülerin işlenmesine olanak tanır. Düğüm, hem görüntü hem de video VAE'lerini destekler ve uzamsal ve zamansal boyutlar için ayrı döşeme kontrolleri sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pixels` | Kodlanacak girdi görüntü verisi | IMAGE | Evet | - |
| `vae` | Kodlama için kullanılan Varyasyonel Otomatik Kodlayıcı modeli | VAE | Evet | - |
| `tile_size` | Uzamsal işleme için her döşemenin boyutu (varsayılan: 512) | INT | Evet | 64-4096 (adım: 64) |
| `overlap` | Bitişik döşemeler arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (adım: 32) |
| `temporal_size` | Yalnızca video VAE'leri için kullanılır: Aynı anda kodlanacak kare sayısı (varsayılan: 64) | INT | Evet | 8-4096 (adım: 4) |
| `temporal_overlap` | Yalnızca video VAE'leri için kullanılır: Örtüşecek kare sayısı (varsayılan: 8) | INT | Evet | 4-4096 (adım: 4) |

**Not:** `temporal_size` ve `temporal_overlap` parametreleri yalnızca video VAE'leri kullanılırken geçerlidir ve standart görüntü VAE'leri üzerinde hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Girdi görüntüsünün kodlanmış gizli temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
