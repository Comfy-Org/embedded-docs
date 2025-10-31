> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/tr.md)

WanImageToVideo düğümü, video üretimi görevleri için koşullandırma ve gizli temsilleri hazırlar. Video üretimi için boş bir gizli alan oluşturur ve isteğe bağlı olarak başlangıç görüntülerini ve CLIP görü çıktılarını video üretim sürecini yönlendirmek için dahil edebilir. Düğüm, sağlanan görüntü ve görü verilerine dayanarak hem pozitif hem de negatif koşullandırma girdilerini değiştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Üretimi yönlendirmek için pozitif koşullandırma girdisi |
| `negatif` | CONDITIONING | Evet | - | Üretimi yönlendirmek için negatif koşullandırma girdisi |
| `vae` | VAE | Evet | - | Görüntüleri gizli alana kodlamak için VAE modeli |
| `genişlik` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı videosunun genişliği (varsayılan: 832, adım: 16) |
| `yükseklik` | INT | Evet | 16 - MAX_RESOLUTION | Çıktı videosunun yüksekliği (varsayılan: 480, adım: 16) |
| `uzunluk` | INT | Evet | 1 - MAX_RESOLUTION | Videodaki kare sayısı (varsayılan: 81, adım: 4) |
| `toplu_boyut` | INT | Evet | 1 - 4096 | Toplu halde üretilecek video sayısı (varsayılan: 1) |
| `clip_görü_çıktısı` | CLIP_VISION_OUTPUT | Hayır | - | İsteğe bağlı ek koşullandırma için CLIP görü çıktısı |
| `başlangıç_görüntüsü` | IMAGE | Hayır | - | Video üretimini başlatmak için isteğe bağlı başlangıç görüntüsü |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini kodlar ve koşullandırma girdilerine maskeleme uygular. `clip_vision_output` parametresi sağlandığında, hem pozitif hem de negatif girdilere görü tabanlı koşullandırma ekler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Görüntü ve görü verileri dahil edilmiş değiştirilmiş pozitif koşullandırma |
| `gizli` | CONDITIONING | Görüntü ve görü verileri dahil edilmiş değiştirilmiş negatif koşullandırma |
| `latent` | LATENT | Video üretimi için hazır boş gizli alan tensörü |