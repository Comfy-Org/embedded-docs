# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent, video üretimi için görüntülerden video latent temsilleri oluşturur. Boş bir video latent'i üretebilir veya başlangıç ve bitiş görüntülerini dahil ederek belirtilen boyut ve süreye sahip video dizileri oluşturabilir. Düğüm, görüntülerin video işleme için uygun latent uzay formatına kodlanmasını yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 93, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_iş_boyutu` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `başlangıç_görseli` | Video dizisi için isteğe bağlı başlangıç görüntüsü | IMAGE | Hayır | - |
| `bitiş_görseli` | Video dizisi için isteğe bağlı bitiş görüntüsü | IMAGE | Hayır | - |

**Not:** Ne `start_image` ne de `end_image` sağlandığında, düğüm boş bir video latent'i üretir. Görüntülerden biri veya her ikisi sağlandığında, bunlar `width` ve `height` boyutlarına yeniden boyutlandırılır, latent uzaya kodlanır ve video dizisinin başına ve/veya sonuna yerleştirilir; ilgili bölgeler, üretim sırasında korunmaları için noise maskesinde işaretlenir. Elde edilen latent ve maske `batch_size` kez tekrarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Kodlanmış video dizisini içeren oluşturulmuş video latent temsili | LATENT |
| `noise_mask` | Üretim sırasında latent'in hangi bölümlerinin korunması gerektiğini gösteren bir maske. Yalnızca `start_image` veya `end_image` girdilerinden en az biri sağlandığında mevcuttur. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
