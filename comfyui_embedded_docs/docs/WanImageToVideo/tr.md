# WanGörüntüdenVideoya

WanImageToVideo düğümü, video oluşturma görevleri için conditioning ve latent temsillerini hazırlar. Video oluşturma için boş bir latent alanı oluşturur ve isteğe bağlı olarak video oluşturma sürecini yönlendirmek için başlangıç görüntülerini ve CLIP görsel çıktılarını dahil edebilir. Düğüm, sağlanan görüntü ve görsel verilere dayanarak hem pozitif hem de negatif conditioning girdilerini değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Oluşturmayı yönlendirmek için pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negative` | Oluşturmayı yönlendirmek için negatif conditioning girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent alana kodlamak için VAE modeli | VAE | Evet | - |
| `width` | Çıktı videosunun genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `height` | Çıktı videosunun yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ila MAX_RESOLUTION |
| `length` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ila MAX_RESOLUTION |
| `batch_size` | Bir batch içinde oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `clip_vision_output` | Ek conditioning için isteğe bağlı CLIP görsel çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `start_image` | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü. Sağlandığında, görüntü belirtilen genişlik ve yüksekliğe uyacak şekilde yeniden boyutlandırılır ve videonun ilk kareleri bu görüntüden başlatılır. Geri kalan kareler nötr gri (0.5) değerleriyle doldurulur. Görüntünün yalnızca ilk `length` karesi kullanılır. | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini VAE kullanarak kodlar ve conditioning girdilerine bir maske uygular. Maske, başlangıç görüntüsüyle başlatılanlar dışındaki tüm kareleri kapsar ve oluşturmanın sağlanan görüntünün üzerine inşa edilmesine olanak tanır. `clip_vision_output` parametresi, sağlandığında hem pozitif hem de negatif girdilere görsel tabanlı conditioning ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntü ve görsel veriler dahil edilmiş, değiştirilmiş pozitif conditioning | CONDITIONING |
| `negative` | Görüntü ve görsel veriler dahil edilmiş, değiştirilmiş negatif conditioning | CONDITIONING |
| `latent` | Video oluşturma için hazır, [batch_size, 16, ((length-1)//4)+1, height//8, width//8] şeklinde boş latent alan tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
