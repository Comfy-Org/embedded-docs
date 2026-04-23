> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/tr.md)

WanSCAILToVideo düğümü, video oluşturma için conditioning ve boş bir latent alanı hazırlar. Referans görüntüler, poz videoları ve CLIP görüş çıktıları gibi isteğe bağlı girdileri işleyerek bunları bir video modeli için pozitif ve negatif conditioning'e gömer. Düğüm, değiştirilmiş conditioning'i ve belirtilen video boyutlarında boş bir latent tensörü çıktı olarak verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Pozitif conditioning girdisi. |
| `negative` | CONDITIONING | Evet | - | Negatif conditioning girdisi. |
| `vae` | VAE | Evet | - | Görüntüleri ve video karelerini kodlamak için kullanılan VAE modeli. |
| `width` | INT | Evet | 32 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 512). 8'e bölünebilir olmalıdır. |
| `height` | INT | Evet | 32 ile MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 896). 8'e bölünebilir olmalıdır. |
| `length` | INT | Evet | 1 ile MAX_RESOLUTION | Videodaki kare sayısı (varsayılan: 81). |
| `batch_size` | INT | Evet | 1 ile 4096 | Bir grupta oluşturulacak video sayısı (varsayılan: 1). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Conditioning için isteğe bağlı CLIP görüş çıktısı. |
| `reference_image` | IMAGE | Hayır | - | Conditioning için isteğe bağlı bir referans görüntüsü. |
| `pose_video` | IMAGE | Hayır | - | Poz conditioning için kullanılan video. Ana videonun çözünürlüğünün yarısına ölçeklenecektir. |
| `pose_strength` | FLOAT | Evet | 0,0 ile 10,0 | Poz latentinin gücü (varsayılan: 1,0). |
| `pose_start` | FLOAT | Evet | 0,0 ile 1,0 | Poz conditioning kullanmaya başlama adımı (varsayılan: 0,0). |
| `pose_end` | FLOAT | Evet | 0,0 ile 1,0 | Poz conditioning kullanmayı bitirme adımı (varsayılan: 1,0). |

**Not:** `pose_video` girdisi yalnızca ilk `length` kare için işlenir. `reference_image` girdisi ise yalnızca gruptaki ilk görüntü için işlenir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Potansiyel olarak gömülü referans görüntü latentleri, CLIP görüş çıktısı veya poz video latentleri içeren değiştirilmiş pozitif conditioning. |
| `negative` | CONDITIONING | Potansiyel olarak gömülü referans görüntü latentleri, CLIP görüş çıktısı veya poz video latentleri içeren değiştirilmiş negatif conditioning. |
| `latent` | LATENT | `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` şeklinde boş bir latent tensörü. |