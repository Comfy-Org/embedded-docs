> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/tr.md)

CosmosImageToVideoLatent düğümü, girdi görüntülerinden video latent temsilleri oluşturur. Boş bir video latent oluşturur ve isteğe bağlı olarak başlangıç ve/veya bitiş görüntülerini video dizisinin başlangıç ve/veya bitiş karelerine kodlar. Görüntüler sağlandığında, ayrıca oluşturma sırasında latentin hangi bölümlerinin korunması gerektiğini belirten ilgili gürültü maskeleri de oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Evet | - | Görüntüleri latent uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 1280) |
| `yükseklik` | INT | Hayır | 16'dan MAX_RESOLUTION'a | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 704) |
| `uzunluk` | INT | Hayır | 1'den MAX_RESOLUTION'a | Video dizisindeki kare sayısı (varsayılan: 121) |
| `toplu_boyut` | INT | Hayır | 1'den 4096'ya | Oluşturulacak latent batch sayısı (varsayılan: 1) |
| `başlangıç_görüntüsü` | IMAGE | Hayır | - | Video dizisinin başına kodlanacak isteğe bağlı görüntü |
| `bitiş_görüntüsü` | IMAGE | Hayır | - | Video dizisinin sonuna kodlanacak isteğe bağlı görüntü |

**Not:** Ne `start_image` ne de `end_image` sağlanmadığında, düğüm herhangi bir gürültü maskesi olmadan boş bir latent döndürür. Görüntülerden herhangi biri sağlandığında, latentin ilgili bölümleri kodlanır ve buna göre maskelenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latent` | LATENT | İsteğe bağlı kodlanmış görüntüler ve ilgili gürültü maskeleri ile oluşturulan video latent temsili |