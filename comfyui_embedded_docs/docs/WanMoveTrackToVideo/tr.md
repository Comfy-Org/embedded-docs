# WanMoveTrackToVideo

WanMoveTrackToVideo düğümü, video üretimi için conditioning ve latent verilerini hazırlar. Başlangıç görüntü dizisini bir VAE kullanarak latent uzaya kodlar ve isteğe bağlı olarak üretilen videodaki nesne hareketlerini yönlendirmek için hareket takip bilgilerini dahil edebilir. Düğüm, değiştirilmiş pozitif ve negatif conditioning ile birlikte bir video üretim modeli için hazır boş bir latent tensörü çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Değiştirilecek pozitif conditioning girdisi. | CONDITIONING | Evet | - |
| `negative` | Değiştirilecek negatif conditioning girdisi. | CONDITIONING | Evet | - |
| `vae` | Başlangıç görüntüsünü latent uzaya kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `tracks` | Nesne yollarını içeren isteğe bağlı hareket takip verileri. | TRACKS | Hayır | - |
| `strength` | Track conditioning'in gücü. Yalnızca `tracks` sağlandığında ve değer 0.0'dan büyük olduğunda etkilidir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `width` | Çıktı videosunun genişliği. 16'nın katları olarak ayarlayın. (varsayılan: 832) | INT | Evet | 16 - MAX_RESOLUTION |
| `height` | Çıktı videosunun yüksekliği. 16'nın katları olarak ayarlayın. (varsayılan: 480) | INT | Evet | 16 - MAX_RESOLUTION |
| `length` | Video dizisindeki kare sayısı. 4'ün katları olarak ayarlayın. (varsayılan: 81) | INT | Evet | 1 - MAX_RESOLUTION |
| `batch_size` | Latent çıktısı için grup boyutu. (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `start_image` | VAE ile kodlanacak başlangıç görüntüsü veya görüntü dizisi. | IMAGE | Evet | - |
| `clip_vision_output` | Conditioning'e eklenecek isteğe bağlı CLIP vision modeli çıktısı. | CLIP_VISION_OUTPUT | Hayır | - |

Not: Track tabanlı hareket yalnızca `tracks` sağlandığında ve `strength` 0.0'dan büyük olduğunda uygulanır. Aksi takdirde, conditioning değiştirilmemiş kodlanmış başlangıç görüntüsünü alır. `start_image`, conditioning için bir latent görüntü ve maske oluşturmak amacıyla kullanılır; mevcut değilse, düğüm yalnızca conditioning'i geçirir ve boş bir latent çıktısı verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Değiştirilmiş pozitif conditioning; potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içerir. | CONDITIONING |
| `negative` | Değiştirilmiş negatif conditioning; potansiyel olarak `concat_latent_image`, `concat_mask` ve `clip_vision_output` içerir. | CONDITIONING |
| `latent` | Boyutları `batch_size`, `length`, `height` ve `width` girdileriyle şekillendirilmiş boş bir latent tensörü. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
