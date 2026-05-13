> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/tr.md)

CosmosImageToVideoLatent düğümü, giriş görüntülerinden video gizil temsilleri oluşturur. Boş bir video gizil temsili üretir ve isteğe bağlı olarak başlangıç ve/veya bitiş görüntülerini video dizisinin ilk ve/veya son karelerine kodlar. Görüntüler sağlandığında, üretim sırasında gizil temsilin hangi bölümlerinin korunması gerektiğini belirtmek için karşılık gelen gürültü maskeleri de oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Evet | - | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli |
| `width` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280) |
| `height` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704) |
| `length` | INT | Evet | 1 ile MAX_RESOLUTION | Video dizisindeki kare sayısı (varsayılan: 121) |
| `batch_size` | INT | Evet | 1 ile 4096 | Oluşturulacak gizil temsil gruplarının sayısı (varsayılan: 1) |
| `start_image` | IMAGE | Hayır | - | Video dizisinin başlangıcına kodlanacak isteğe bağlı görüntü |
| `end_image` | IMAGE | Hayır | - | Video dizisinin sonuna kodlanacak isteğe bağlı görüntü |

**Not:** Ne `start_image` ne de `end_image` sağlanmadığında, düğüm herhangi bir gürültü maskesi olmadan boş bir gizil temsil döndürür. Görüntülerden herhangi biri sağlandığında, gizil temsilin ilgili bölümleri kodlanır ve buna göre maskelenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latent` | LATENT | İsteğe bağlı olarak kodlanmış görüntüler ve karşılık gelen gürültü maskeleriyle birlikte oluşturulan video gizil temsili |

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
