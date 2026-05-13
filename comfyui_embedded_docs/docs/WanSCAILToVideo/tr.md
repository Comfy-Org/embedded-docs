> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/tr.md)

WanSCAILToVideo düğümü, video üretimi için koşullandırma (conditioning) ve boş bir latent alan hazırlar. Referans görüntüler, poz videoları ve CLIP görüş çıktıları gibi isteğe bağlı girdileri işleyerek bunları bir video modeli için pozitif ve negatif koşullandırmaya gömer. Düğüm, değiştirilmiş koşullandırmayı ve belirtilen video boyutlarında boş bir latent tensörü çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Pozitif koşullandırma girdisi. |
| `negatif` | CONDITIONING | Evet | - | Negatif koşullandırma girdisi. |
| `vae` | VAE | Evet | - | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli. |
| `genişlik` | INT | Evet | 32 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 512). 8'e bölünebilir olmalıdır. |
| `yükseklik` | INT | Evet | 32 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 896). 8'e bölünebilir olmalıdır. |
| `uzunluk` | INT | Evet | 1 - MAX_RESOLUTION | Videodaki kare sayısı (varsayılan: 81). 4'e bölünebilir olmalıdır. |
| `toplu_boyutu` | INT | Evet | 1 - 4096 | Bir grupta (batch) oluşturulacak video sayısı (varsayılan: 1). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Koşullandırma için isteğe bağlı CLIP görüş çıktısı. |
| `referans_görsel` | IMAGE | Hayır | - | Koşullandırma için isteğe bağlı bir referans görüntüsü. |
| `poz_videosu` | IMAGE | Hayır | - | Poz koşullandırması için kullanılan video. Ana videonun çözünürlüğünün yarısına ölçeklenecektir. |
| `poz_gücü` | FLOAT | Evet | 0.0 - 10.0 | Poz latentinin gücü (varsayılan: 1.0). |
| `poz_başlangıcı` | FLOAT | Evet | 0.0 - 1.0 | Poz koşullandırmasını kullanmaya başlama adımı (varsayılan: 0.0). |
| `poz_bitişi` | FLOAT | Evet | 0.0 - 1.0 | Poz koşullandırmasını kullanmayı bitirme adımı (varsayılan: 1.0). |

**Not:** `pose_video` girdisi yalnızca ilk `length` kare için işlenir. `reference_image` girdisi ise yalnızca gruptaki ilk görüntü için işlenir. `reference_image` sağlandığında, negatif koşullandırma için aynı boyutta sıfırlarla doldurulmuş bir latent kullanılır. `clip_vision_output` sağlandığında, hem pozitif hem de negatif koşullandırmaya uygulanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Potansiyel olarak gömülü referans görüntü latentleri, CLIP görüş çıktısı veya poz video latentleri içeren değiştirilmiş pozitif koşullandırma. |
| `latent` | CONDITIONING | Potansiyel olarak gömülü referans görüntü latentleri, CLIP görüş çıktısı veya poz video latentleri içeren değiştirilmiş negatif koşullandırma. |
| `latent` | LATENT | Şekli `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` olan boş bir latent tensörü. |

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
