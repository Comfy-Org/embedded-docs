WanSCAILToVideo düğümü, video üretimi için koşullandırma (conditioning) ve boş bir latent alan hazırlar. Referans görüntüler, poz videoları ve CLIP görüş çıktıları gibi isteğe bağlı girdileri işleyerek bunları bir video modeli için pozitif ve negatif koşullandırmaya gömer. Düğüm, değiştirilmiş koşullandırmayı ve belirtilen video boyutlarında boş bir latent tensörü çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Pozitif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `negatif` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | - |
| `vae` | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli. | VAE | Evet | - |
| `genişlik` | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 512). 8'e bölünebilir olmalıdır. | INT | Evet | 32 - MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 896). 8'e bölünebilir olmalıdır. | INT | Evet | 32 - MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81). 4'e bölünebilir olmalıdır. | INT | Evet | 1 - MAX_RESOLUTION |
| `toplu_boyutu` | Bir grupta (batch) oluşturulacak video sayısı (varsayılan: 1). | INT | Evet | 1 - 4096 |
| `clip_vision_output` | Koşullandırma için isteğe bağlı CLIP görüş çıktısı. | CLIP_VISION_OUTPUT | Hayır | - |
| `referans_görsel` | Koşullandırma için isteğe bağlı bir referans görüntüsü. | IMAGE | Hayır | - |
| `poz_videosu` | Poz koşullandırması için kullanılan video. Ana videonun çözünürlüğünün yarısına ölçeklenecektir. | IMAGE | Hayır | - |
| `poz_gücü` | Poz latentinin gücü (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 10.0 |
| `poz_başlangıcı` | Poz koşullandırmasını kullanmaya başlama adımı (varsayılan: 0.0). | FLOAT | Evet | 0.0 - 1.0 |
| `poz_bitişi` | Poz koşullandırmasını kullanmayı bitirme adımı (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 1.0 |

**Not:** `pose_video` girdisi yalnızca ilk `length` kare için işlenir. `reference_image` girdisi ise yalnızca gruptaki ilk görüntü için işlenir. `reference_image` sağlandığında, negatif koşullandırma için aynı boyutta sıfırlarla doldurulmuş bir latent kullanılır. `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negatif` | Potansiyel olarak gömülü referans görüntü latentleri, CLIP görüş çıktısı veya poz video latentleri içeren değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `latent` | Potansiyel olarak gömülü referans görüntü latentleri, CLIP görüş çıktısı veya poz video latentleri içeren değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `video_frame_offset` | Şekli `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` olan boş bir latent tensörü. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
