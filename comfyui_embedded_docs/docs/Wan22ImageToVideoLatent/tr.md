# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent düğümü, görüntülerden video gizil temsilleri oluşturur. Belirtilen boyutlarda boş bir video gizil alanı oluşturur ve isteğe bağlı olarak başlangıç görüntü dizisini ilk karelere kodlayabilir. Bir başlangıç görüntüsü sağlandığında, görüntüyü gizil alana kodlar ve boyanmış bölgeler için karşılık gelen bir gürültü maskesi oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Görüntüleri gizil alana kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280, adım: 32) | INT | Evet | 32 - MAKS_ÇÖZÜNÜRLÜK |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704, adım: 32) | INT | Evet | 32 - MAKS_ÇÖZÜNÜRLÜK |
| `length` | Video dizisindeki kare sayısı (varsayılan: 49, adım: 4) | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK |
| `batch_size` | Oluşturulacak grup sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `start_image` | Video gizil alanına kodlanacak isteğe bağlı başlangıç görüntü dizisi | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini gizil alanın ilk karelerine kodlar ve karşılık gelen bir gürültü maskesi oluşturur. Genişlik ve yükseklik parametreleri, uygun gizil alan boyutları için 16'ya bölünebilir olmalıdır. `length` parametresi, video gizil alanındaki kare sayısını belirler; gizil alanın zamansal boyutu `((length - 1) // 4) + 1` olarak hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Oluşturulan video gizil temsili | LATENT |
| `noise_mask` | Oluşturma sırasında hangi bölgelerin gürültüden arındırılması gerektiğini belirten gürültü maskesi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
