# CosmosGörüntüdenVideoyaGizli

CosmosImageToVideoLatent düğümü, giriş görüntülerinden bir video latent gösterimi oluşturur. İstenen genişlik, yükseklik ve kare sayısıyla boş bir video latent oluşturur; ardından isteğe bağlı olarak başlangıç görüntüsünü başlangıç karelerine ve/veya bitiş görüntüsünü bitiş karelerine kodlar. Görüntü sağlandığında, kodlanan karelerin üretim sırasında sabit kalması için bir gürültü maskesi de üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `vae` | Görüntüleri video latent uzayına kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280). | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704). | INT | Evet | 16 to MAX_RESOLUTION (step: 16) |
| `uzunluk` | Videodaki toplam kare sayısı (varsayılan: 121). | INT | Evet | 1 to MAX_RESOLUTION (step: 8) |
| `toplu_boyut` | Oluşturulacak video latentlerinin sayısı (varsayılan: 1). | INT | Evet | 1 ile 4096 |
| `başlangıç_görüntüsü` | Videonun başlangıcına kodlanacak isteğe bağlı görüntü veya görüntü dizisi. | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Videonun sonuna kodlanacak isteğe bağlı görüntü veya görüntü dizisi. | IMAGE | Hayır | - |

**Not:**
- Hem `start_image` hem de `end_image` sağlanmadığında düğüm, gürültü maskesi olmadan boş bir latent döndürür.
- `start_image` sağlandığında, latentin ilk karelerine kodlanır ve bu kareler gürültü maskesi değeri 0 (korunan) olarak işaretlenir. `end_image` sağlandığında, son karelere kodlanır ve bu kareler gürültü maskesi değeri 0 olarak işaretlenir. Geri kalan kareler 1 maske değerini korur.
- Latent 16 kanala sahiptir ve uzamsal boyutları `height / 8` x `width / 8` şeklindedir. Latent kare sayısı `((length - 1) // 8) + 1` formülüyle hesaplanır.
- `batch_size`, latenti ve varsa gürültü maskesini çoğaltır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | İsteğe bağlı olarak kodlanmış başlangıç ve/veya bitiş görüntülerini içeren oluşturulmuş video latentidir; görüntü sağlandığında, korunan karelerde değeri 0 olan eşleşen bir gürültü maskesi de içerir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
