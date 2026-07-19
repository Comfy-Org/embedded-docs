# CosmosGörüntüdenVideoyaGizli

CosmosImageToVideoLatent düğümü, giriş görüntülerinden video gizil temsilleri oluşturur. Boş bir video gizil temsili üretir ve isteğe bağlı olarak başlangıç ve/veya bitiş görüntülerini video dizisinin ilk ve/veya son karelerine kodlar. Görüntüler sağlandığında, üretim sırasında gizil temsilin hangi bölümlerinin korunması gerektiğini belirtmek için karşılık gelen gürültü maskeleri de oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Görüntüleri gizil uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280) | INT | Evet | 16 ile MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704) | INT | Evet | 16 ile MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 121) | INT | Evet | 1 ile MAX_RESOLUTION |
| `toplu_boyut` | Oluşturulacak gizil temsil gruplarının sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `başlangıç_görüntüsü` | Video dizisinin başlangıcına kodlanacak isteğe bağlı görüntü | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Video dizisinin sonuna kodlanacak isteğe bağlı görüntü | IMAGE | Hayır | - |

**Not:** Ne `start_image` ne de `end_image` sağlanmadığında, düğüm herhangi bir gürültü maskesi olmadan boş bir gizil temsil döndürür. Görüntülerden herhangi biri sağlandığında, gizil temsilin ilgili bölümleri kodlanır ve buna göre maskelenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | İsteğe bağlı olarak kodlanmış görüntüler ve karşılık gelen gürültü maskeleriyle birlikte oluşturulan video gizil temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
