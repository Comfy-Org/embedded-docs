> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/tr.md)

Wan22ImageToVideoLatent düğümü, görüntülerden video latent temsilleri oluşturur. Belirtilen boyutlarda boş bir video latent alanı oluşturur ve isteğe bağlı olarak bir başlangıç görüntü dizisini başlangıç karelerine kodlayabilir. Bir başlangıç görüntüsü sağlandığında, görüntüyü latent alana kodlar ve boyanan bölgeler için karşılık gelen bir gürültü maskesi oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Evet | - | Görüntüleri latent alana kodlamak için kullanılan VAE modeli |
| `width` | INT | Hayır | 32 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280, adım: 32) |
| `height` | INT | Hayır | 32 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704, adım: 32) |
| `length` | INT | Hayır | 1 - MAX_RESOLUTION | Video dizisindeki kare sayısı (varsayılan: 49, adım: 4) |
| `batch_size` | INT | Hayır | 1 - 4096 | Oluşturulacak parti sayısı (varsayılan: 1) |
| `start_image` | IMAGE | Hayır | - | Video latent içine kodlanacak isteğe bağlı başlangıç görüntü dizisi |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini latent alanın başlangıç karelerine kodlar ve karşılık gelen bir gürültü maskesi oluşturur. Genişlik ve yükseklik parametreleri, uygun latent alan boyutları için 16'ya bölünebilir olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Oluşturulan video latent temsili |
| `noise_mask` | LATENT | Üretim sırasında hangi bölgelerin gürültüden arındırılması gerektiğini belirten gürültü maskesi |