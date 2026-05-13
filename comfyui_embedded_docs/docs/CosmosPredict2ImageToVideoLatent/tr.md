> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/tr.md)

CosmosPredict2ImageToVideoLatent düğümü, video oluşturma için görüntülerden video gizil (latent) temsilleri oluşturur. Belirtilen boyut ve süreye sahip video dizileri oluşturmak için boş bir video gizili oluşturabilir veya başlangıç ve bitiş görüntülerini dahil edebilir. Düğüm, görüntüleri video işleme için uygun gizil uzay formatına kodlama işlemini gerçekleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `vae` | VAE | Evet | - | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalıdır) |
| `yükseklik` | INT | Hayır | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalıdır) |
| `uzunluk` | INT | Hayır | 1 ile MAX_RESOLUTION | Video dizisindeki kare sayısı (varsayılan: 93, adım: 4) |
| `toplu_iş_boyutu` | INT | Hayır | 1 ile 4096 | Oluşturulacak video dizisi sayısı (varsayılan: 1) |
| `başlangıç_görseli` | IMAGE | Hayır | - | Video dizisi için isteğe bağlı başlangıç görüntüsü |
| `bitiş_görseli` | IMAGE | Hayır | - | Video dizisi için isteğe bağlı bitiş görüntüsü |

**Not:** Ne `start_image` ne de `end_image` sağlanmadığında, düğüm boş bir video gizili oluşturur. Görüntüler sağlandığında, uygun maskeleme ile video dizisinin başına ve/veya sonuna konumlandırılarak kodlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `samples` | LATENT | Kodlanmış video dizisini içeren oluşturulan video gizil temsili |
| `noise_mask` | LATENT | Oluşturma sırasında gizilin hangi bölümlerinin korunması gerektiğini belirten maske |

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`
