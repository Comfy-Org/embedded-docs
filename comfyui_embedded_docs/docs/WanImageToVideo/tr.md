> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/tr.md)

WanImageToVideo düğümü, video oluşturma görevleri için conditioning ve latent temsillerini hazırlar. Video oluşturma için boş bir latent alanı oluşturur ve isteğe bağlı olarak video oluşturma sürecini yönlendirmek için başlangıç görüntüleri ve CLIP görüş çıktılarını dahil edebilir. Düğüm, sağlanan görüntü ve görüş verilerine dayanarak hem pozitif hem de negatif conditioning girdilerini değiştirir.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Oluşturmayı yönlendirmek için pozitif conditioning girdisi |
| `negative` | CONDITIONING | Evet | - | Oluşturmayı yönlendirmek için negatif conditioning girdisi |
| `vae` | VAE | Evet | - | Görüntüleri latent alana kodlamak için VAE modeli |
| `width` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun genişliği (varsayılan: 832, adım: 16) |
| `height` | INT | Evet | 16 ile MAX_RESOLUTION | Çıktı videosunun yüksekliği (varsayılan: 480, adım: 16) |
| `length` | INT | Evet | 1 ile MAX_RESOLUTION | Videodaki kare sayısı (varsayılan: 81, adım: 4) |
| `batch_size` | INT | Evet | 1 ile 4096 | Bir grupta oluşturulacak video sayısı (varsayılan: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | - | Ek conditioning için isteğe bağlı CLIP görüş çıktısı |
| `start_image` | IMAGE | Hayır | - | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini kodlar ve conditioning girdilerine maskeleme uygular. `clip_vision_output` parametresi sağlandığında, hem pozitif hem de negatif girdilere görüş tabanlı conditioning ekler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Görüntü ve görüş verileri dahil edilmiş, değiştirilmiş pozitif conditioning |
| `negative` | CONDITIONING | Görüntü ve görüş verileri dahil edilmiş, değiştirilmiş negatif conditioning |
| `latent` | LATENT | Video oluşturma için hazır, boş latent alan tensörü |

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
