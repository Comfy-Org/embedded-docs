# VAE Kodlama (Döşemeli)

VAEEncodeTiled, görüntüleri daha küçük karolara bölerek ve bunları bir Varyasyonel Otomatik Kodlayıcı kullanarak kodlayarak işler. Bu karolama yaklaşımı, aksi takdirde bellek sınırlarını aşabilecek büyük görüntülerin işlenmesine olanak tanır. Düğüm, hem görüntü hem de video VAE'lerini destekler; uzamsal ve zamansal boyutlar için ayrı karolama denetimleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pixels` | Kodlanacak girdi görüntü verisi. | IMAGE | Evet | - |
| `vae` | Kodlama için kullanılan Varyasyonel Otomatik Kodlayıcı modeli. | VAE | Evet | - |
| `tile_size` | Uzamsal işleme için her bir karonun boyutu (varsayılan: 512). Gelişmiş ayar. | INT | Evet | 64-4096 (adım: 64) |
| `overlap` | Bitişik karolar arasındaki örtüşme miktarı (varsayılan: 64). Gelişmiş ayar. | INT | Evet | 0-4096 (adım: 32) |
| `temporal_size` | Yalnızca video VAE'leri için kullanılır: Bir seferde kodlanacak kare miktarı (varsayılan: 64). Gelişmiş ayar. | INT | Evet | 8-4096 (adım: 4) |
| `temporal_overlap` | Yalnızca video VAE'leri için kullanılır: Örtüşecek kare miktarı (varsayılan: 8). Gelişmiş ayar. | INT | Evet | 4-4096 (adım: 4) |

**Not:** `temporal_size` ve `temporal_overlap` parametreleri yalnızca video VAE'leri kullanılırken geçerlidir ve standart görüntü VAE'leri üzerinde hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Girdi görüntüsünün kodlanmış gizli temsili. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
