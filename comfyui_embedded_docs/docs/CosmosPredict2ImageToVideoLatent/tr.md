> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/tr.md)

CosmosPredict2ImageToVideoLatent düğümü, video oluşturma için görüntülerden video latent temsilleri oluşturur. Boş bir video latent oluşturabilir veya başlangıç ve bitiş görüntülerini dahil ederek belirli boyutlarda ve sürede video dizileri oluşturabilir. Düğüm, görüntülerin video işleme için uygun latent uzay formatına kodlanmasını işler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Evet | - | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 848, 16'ya bölünebilir olmalı) |
| `height` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, 16'ya bölünebilir olmalı) |
| `length` | INT | Hayır | 1'den MAX_RESOLUTION'a | Video dizisindeki kare sayısı (varsayılan: 93, adım: 4) |
| `batch_size` | INT | Hayır | 1'den 4096'ya | Oluşturulacak video dizisi sayısı (varsayılan: 1) |
| `start_image` | IMAGE | Hayır | - | Video dizisi için isteğe bağlı başlangıç görüntüsü |
| `end_image` | IMAGE | Hayır | - | Video dizisi için isteğe bağlı bitiş görüntüsü |

**Not:** Ne `start_image` ne de `end_image` sağlandığında, düğüm boş bir video latent oluşturur. Görüntüler sağlandığında, bunlar kodlanır ve uygun maskeleme ile video dizisinin başına ve/veya sonuna yerleştirilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Kodlanmış video dizisini içeren oluşturulmuş video latent temsili |
| `noise_mask` | LATENT | Oluşturma sırasında latentin hangi bölümlerinin korunması gerektiğini belirten maske |