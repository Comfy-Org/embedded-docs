# VAEEncodeTiled Düğümü

VAEEncodeTiled düğümü, görüntüleri daha küçük parçalara bölerek ve bunları bir Değişken Otomatik Kodlayıcı (VAE) kullanarak kodlayarak işler. Bu parçalama yaklaşımı, aksi takdirde bellek sınırlarını aşabilecek büyük görüntülerin işlenmesine olanak tanır. Düğüm, hem görüntü hem de video VAE'lerini destekler ve uzamsal ve zamansal boyutlar için ayrı parçalama kontrollerine sahiptir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pikseller` | Kodlanacak giriş görüntü verisi | IMAGE | Evet | - |
| `vae` | Kodlama için kullanılan Değişken Otomatik Kodlayıcı modeli | VAE | Evet | - |
| `döşeme_boyutu` | Uzamsal işleme için her bir parçanın boyutu (varsayılan: 512) | INT | Evet | 64-4096 (adım: 64) |
| `örtüşme` | Bitişik parçalar arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (adım: 32) |
| `zamansal_boyut` | Yalnızca video VAE'leri için kullanılır: Bir seferde kodlanacak kare sayısı (varsayılan: 64) | INT | Evet | 8-4096 (adım: 4) |
| `zamansal_örtüşme` | Yalnızca video VAE'leri için kullanılır: Örtüşecek kare sayısı (varsayılan: 8) | INT | Evet | 4-4096 (adım: 4) |

**Not:** `temporal_size` ve `temporal_overlap` parametreleri yalnızca video VAE'leri kullanıldığında geçerlidir ve standart görüntü VAE'leri üzerinde hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Giriş görüntüsünün kodlanmış gizli temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `87420b96ef9b2d5ef18ecb0339a62b6955151e2a9d2c4390758048c00432939a`
