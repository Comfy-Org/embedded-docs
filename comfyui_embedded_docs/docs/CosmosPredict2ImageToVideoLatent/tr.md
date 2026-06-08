CosmosPredict2ImageToVideoLatent düğümü, video oluşturma için görüntülerden video gizil (latent) temsilleri oluşturur. Belirtilen boyut ve süreye sahip video dizileri oluşturmak için boş bir video gizili oluşturabilir veya başlangıç ve bitiş görüntülerini dahil edebilir. Düğüm, görüntüleri video işleme için uygun gizil uzay formatına kodlama işlemini gerçekleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) | INT | Hayır | 16 ile MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) | INT | Hayır | 16 ile MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 93, adım: 4) | INT | Hayır | 1 ile MAX_RESOLUTION |
| `toplu_iş_boyutu` | Oluşturulacak video dizisi sayısı (varsayılan: 1) | INT | Hayır | 1 ile 4096 |
| `başlangıç_görseli` | Video dizisi için isteğe bağlı başlangıç görüntüsü | IMAGE | Hayır | - |
| `bitiş_görseli` | Video dizisi için isteğe bağlı bitiş görüntüsü | IMAGE | Hayır | - |

**Not:** Ne `start_image` ne de `end_image` sağlanmadığında, düğüm boş bir video gizili oluşturur. Görüntüler sağlandığında, uygun maskeleme ile video dizisinin başına ve/veya sonuna konumlandırılarak kodlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Kodlanmış video dizisini içeren oluşturulan video gizil temsili | LATENT |
| `noise_mask` | Oluşturma sırasında gizilin hangi bölümlerinin korunması gerektiğini belirten maske | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`
