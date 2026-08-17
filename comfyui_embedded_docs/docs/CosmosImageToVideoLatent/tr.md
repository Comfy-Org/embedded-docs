# CosmosGörüntüdenVideoyaGizli

CosmosImageToVideoLatent düğümü, görüntüden videoya üretim için bir video latent'i oluşturur. Boş bir latent ile başlar ve isteğe bağlı olarak bir başlangıç görüntüsünü ve/veya bir bitiş görüntüsünü video dizisinin ilk veya son karelerine kodlayabilir. Görüntü sağlandığında, kodlanan kareleri üretim sırasında sabit olarak işaretleyen bir gürültü maskesi de üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Giriş görüntülerini latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280) | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `height` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704) | INT | Evet | 16 to MAX_RESOLUTION (step 16) |
| `length` | Video dizisindeki kare sayısı (varsayılan: 121) | INT | Evet | 1 to MAX_RESOLUTION (step 8) |
| `batch_size` | Çıktı batch'inde oluşturulacak video latentlerinin sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `start_image` | Video dizisinin başlangıcına kodlanacak isteğe bağlı görüntü veya görüntü dizisi | IMAGE | Hayır | - |
| `end_image` | Video dizisinin sonuna kodlanacak isteğe bağlı görüntü veya görüntü dizisi | IMAGE | Hayır | - |

**Not:** `start_image` ve `end_image` parametrelerinden hiçbiri sağlanmadığında, düğüm gürültü maskesi olmadan boş bir latent döndürür. En az bir görüntü sağlandığında bir `noise_mask` dahil edilir: sağlanan görüntülerden kodlanan latent kareler 0 maske değerine (sabit tutulur) sahipken, kalan kareler 1 maske değerine (üretilecek) sahiptir. Görüntüler kodlamadan önce hedef `width` ve `height` değerlerine yeniden boyutlandırılır ve bir giriş görüntüsünden alınan kare sayısı, en fazla `length` olmak üzere batch boyutuna eşittir. Latent, 16 kanala, `width / 8` ve `height / 8` uzamsal boyutlarına ve `((length - 1) // 8) + 1` kareye sahiptir. Görüntüler sağlandığında, latent ve gürültü maskesi, çıktı batch'ini oluşturmak için `batch_size` kez tekrarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Video latent `samples` içeren bir LATENT ve `start_image` veya `end_image` sağlandığında, kodlanan kareleri sabit olarak işaretleyen bir `noise_mask` | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
