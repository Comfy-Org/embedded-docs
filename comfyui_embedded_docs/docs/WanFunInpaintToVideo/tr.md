> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/tr.md)

WanFunInpaintToVideo düğümü, başlangıç ve bitiş görüntüleri arasında boyama yaparak video dizileri oluşturur. Video latents oluşturmak için pozitif ve negatif koşullandırmanın yanı sıra isteğe bağlı kare görüntülerini alır. Düğüm, yapılandırılabilir boyut ve uzunluk parametreleriyle video oluşturmayı işler.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Video oluşturma için pozitif koşullandırma promptları |
| `negative` | CONDITIONING | Evet | - | Video oluşturmada kaçınılacak negatif koşullandırma promptları |
| `vae` | VAE | Evet | - | Kodlama/kod çözme işlemleri için VAE modeli |
| `width` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı videosunun piksel cinsinden yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 - MAX_RESOLUTION | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 - 4096 | Toplu halde oluşturulacak video sayısı (varsayılan: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP vision çıktısı |
| `start_image` | IMAGE | Hayır | - | Video oluşturma için isteğe bağlı başlangıç kare görüntüsü |
| `end_image` | IMAGE | Hayır | - | Video oluşturma için isteğe bağlı bitiş kare görüntüsü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | İşlenmiş pozitif koşullandırma çıktısı |
| `negative` | CONDITIONING | İşlenmiş negatif koşullandırma çıktısı |
| `latent` | LATENT | Oluşturulan video latent temsili |