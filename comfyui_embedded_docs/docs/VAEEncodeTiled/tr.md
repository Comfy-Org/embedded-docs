# VAE Kodlama (Döşemeli)

VAEEncodeTiled, görüntüleri daha küçük parçalara bölerek ve bir Değişken Otomatik Kodlayıcı (VAE) kullanarak kodlayarak işler. Bu parçalı yaklaşım, aksi takdirde bellek sınırlamalarını aşabilecek büyük görüntülerin işlenmesine olanak tanır. Düğüm, hem görüntü hem de video VAE'lerini destekler ve uzamsal ve zamansal boyutlar için ayrı parçalama kontrolleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pikseller` | Kodlanacak giriş görüntüsü verisi | IMAGE | Evet | - |
| `vae` | Kodlama için kullanılan Değişken Otomatik Kodlayıcı modeli | VAE | Evet | - |
| `döşeme_boyutu` | Uzamsal işleme için her parçanın boyutu (varsayılan: 512) | INT | Evet | 64-4096 (adım: 64) |
| `örtüşme` | Bitişik parçalar arasındaki örtüşme miktarı (varsayılan: 64) | INT | Evet | 0-4096 (adım: 32) |
| `zamansal_boyut` | Yalnızca video VAE'leri için kullanılır: Aynı anda kodlanacak kare sayısı (varsayılan: 64) | INT | Evet | 8-4096 (adım: 4) |
| `zamansal_örtüşme` | Yalnızca video VAE'leri için kullanılır: Örtüşecek kare sayısı (varsayılan: 8) | INT | Evet | 4-4096 (adım: 4) |

**Not:** `temporal_size` ve `temporal_overlap` parametreleri yalnızca video VAE'leri kullanıldığında geçerlidir ve standart görüntü VAE'leri üzerinde hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Giriş görüntüsünün kodlanmış latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/tr.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
