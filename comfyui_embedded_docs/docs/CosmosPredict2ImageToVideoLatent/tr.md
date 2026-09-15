# CosmosPredict2ImageToVideoLatent

Cosmos Predict2 görüntüden videoya iş akışı için video latentleri oluşturur. Düğüm, belirtilen boyut ve uzunlukta boş bir video latenti üretebilir veya kodlanmış başlangıç ve/veya bitiş görüntülerini diziye ekleyerek bu karelerin üretim sırasında korunmasını sağlayabilir. Sağlanan herhangi bir görüntü, istenen `width` ve `height` değerlerine yeniden boyutlandırılır ve latent dizisinin başına ve/veya sonuna yerleştirilmeden önce sağlanan VAE ile kodlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Başlangıç ve bitiş görüntülerini latent uzayına kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, 16'nın katı olmalıdır) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'nın katı olmalıdır) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 93) | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_iş_boyutu` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `başlangıç_görseli` | Video dizisi için isteğe bağlı başlangıç görüntüsü | IMAGE | Hayır | - |
| `bitiş_görseli` | Video dizisi için isteğe bağlı bitiş görüntüsü | IMAGE | Hayır | - |

**Not:** `start_image` veya `end_image` sağlanmadığında, düğüm yalnızca istenen boyut ve uzunlukta boş bir latent döndürür. Bir veya her iki görüntü sağlandığında, bunlar `width` ve `height` değerlerine yeniden boyutlandırılır, `vae` ile kodlanır ve latent dizisinin başına ve/veya sonuna yerleştirilir. İlgili bölgeler, üretim sırasında korunmaları için gürültü maskesinde işaretlenir. Kodlanan latentler Wan 2.1 latent formatına dönüştürülür ve ortaya çıkan latent ile maske `batch_size` kez yinelenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Oluşturulan video latenti; `samples` (video latent dizisi) içerir ve `start_image` veya `end_image`'den en az biri sağlandığında, üretim sırasında korunması gereken kareleri işaretleyen bir `noise_mask` içerir | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
