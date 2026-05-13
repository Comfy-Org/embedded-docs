> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/tr.md)

Wan22ImageToVideoLatent düğümü, görüntülerden video gizil temsilleri oluşturur. Belirtilen boyutlarda boş bir video gizil alanı oluşturur ve isteğe bağlı olarak başlangıç görüntü dizisini ilk karelere kodlayabilir. Bir başlangıç görüntüsü sağlandığında, görüntüyü gizil alana kodlar ve boyanmış bölgeler için karşılık gelen bir gürültü maskesi oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Evet | - | Görüntüleri gizil alana kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 32 - MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280, adım: 32) |
| `height` | INT | Evet | 32 - MAKS_ÇÖZÜNÜRLÜK | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704, adım: 32) |
| `length` | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK | Video dizisindeki kare sayısı (varsayılan: 49, adım: 4) |
| `batch_size` | INT | Evet | 1 - 4096 | Oluşturulacak grup sayısı (varsayılan: 1) |
| `start_image` | IMAGE | Hayır | - | Video gizil alanına kodlanacak isteğe bağlı başlangıç görüntü dizisi |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini gizil alanın ilk karelerine kodlar ve karşılık gelen bir gürültü maskesi oluşturur. Genişlik ve yükseklik parametreleri, uygun gizil alan boyutları için 16'ya bölünebilir olmalıdır. `length` parametresi, video gizil alanındaki kare sayısını belirler; gizil alanın zamansal boyutu `((length - 1) // 4) + 1` olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Oluşturulan video gizil temsili |
| `noise_mask` | LATENT | Oluşturma sırasında hangi bölgelerin gürültüden arındırılması gerektiğini belirten gürültü maskesi |

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
