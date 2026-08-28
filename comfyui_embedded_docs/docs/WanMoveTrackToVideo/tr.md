# WanMoveTrackToVideo

WanMoveTrackToVideo düğümü, isteğe bağlı hareket takibi bilgilerini dahil ederek video üretimi için conditioning ve latent uzay verilerini hazırlar. Bir başlangıç görüntü dizisini latent bir temsile kodlar ve üretilen videodaki hareketi yönlendirmek için nesne izlerinden gelen konumsal verileri harmanlayabilir. Düğüm, değiştirilmiş positive ve negative conditioning ile birlikte bir video modeli için hazır boş bir latent tensör çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Değiştirilecek positive conditioning girdisi. | CONDITIONING | Evet | - |
| `negatif` | Değiştirilecek negative conditioning girdisi. | CONDITIONING | Evet | - |
| `vae` | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `izler` | Nesne yollarını içeren isteğe bağlı hareket takibi verileri. | TRACKS | Hayır | - |
| `güç` | Track conditioning'in gücü. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `genişlik` | Çıktı videosunun genişliği. 16'ya bölünebilir olmalıdır. (varsayılan: 832) | INT | Evet | 16 - MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun yüksekliği. 16'ya bölünebilir olmalıdır. (varsayılan: 480) | INT | Evet | 16 - MAX_RESOLUTION |
| `uzunluk` | Video dizisindeki kare sayısı, 4'er artışlarla. (varsayılan: 81) | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_boyutu` | Latent çıktı için batch boyutu. (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `başlangıç_görseli` | Kodlanacak başlangıç görüntüsü veya görüntü dizisi. | IMAGE | Evet | - |
| `clip_vision_output` | Conditioning'e eklenecek isteğe bağlı CLIP vision modeli çıktısı. | CLIP_VISION_OUTPUT | Hayır | - |

**Not:** `strength` parametresi yalnızca `tracks` sağlandığında ve `strength` 0.0'dan büyük olduğunda etkilidir; track conditioning yalnızca `start_image` de sağlandığında uygulanır. `tracks` sağlanmazsa veya `strength` 0.0 ise, track harmanlama atlanır. Track harmanlama etkin olduğunda, positive conditioning track ile harmanlanmış latent görüntüyü alırken, negative conditioning değiştirilmemiş latent görüntüyü alır. `start_image` sağlanmazsa, latent görüntü ve maske conditioning'i oluşturulmaz; positive ve negative conditioning değiştirilmeden geçer (sağlanmışsa `clip_vision_output` yine de eklenir) ve düğüm boş bir latent çıkarır.

**Not:** `start_image` sağlandığında, görüntü dizisi hedef `width` ve `height` boyutlarına yeniden boyutlandırılır ve ilk `length` kareye kırpılır. Dizi `length` değerinden kısaysa, VAE kodlamasından önce kalan kareler nötr gri karelerle (değer 0.5) doldurulur. Ortaya çıkan conditioning, başlangıç görüntüsü karelerine karşılık gelen zamansal konumlarda değeri 0 ve diğer konumlarda 1 olan bir `concat_mask` içerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | `concat_latent_image`, `concat_mask` ve `clip_vision_output` içerebilen değiştirilmiş positive conditioning. | CONDITIONING |
| `negatif` | `concat_latent_image`, `concat_mask` ve `clip_vision_output` içerebilen değiştirilmiş negative conditioning. | CONDITIONING |
| `latent` | `batch_size`, `length`, `height` ve `width` girdilerine göre belirlenen, `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` şeklinde boş bir latent tensör. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
