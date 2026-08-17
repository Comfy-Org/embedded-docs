# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent düğümü, video oluşturma için görüntülerden video latent gösterimleri oluşturur. Boş bir video latent'i oluşturabilir veya başlangıç ve bitiş görüntülerini dahil ederek belirtilen boyut ve sürede video dizileri oluşturabilir. Düğüm, görüntülerin video işleme için uygun latent uzay biçimine kodlanmasını yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `length` | Video dizisindeki kare sayısı (varsayılan: 93) | INT | Evet | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `start_image` | Video dizisi için isteğe bağlı başlangıç görüntüsü | IMAGE | Hayır | - |
| `end_image` | Video dizisi için isteğe bağlı bitiş görüntüsü | IMAGE | Hayır | - |

**Not:** `start_image` ve `end_image` parametrelerinden hiçbiri sağlanmadığında düğüm boş bir video latent'i oluşturur. Görüntüler sağlandığında, bunlar kodlanır ve uygun maskeleme ile video dizisinin başına ve/veya sonuna yerleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Kodlanmış video dizisini içeren oluşturulan video latent gösterimi | LATENT |
| `noise_mask` | Oluşturma sırasında latent'in hangi bölümlerinin korunması gerektiğini belirten bir maske | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
