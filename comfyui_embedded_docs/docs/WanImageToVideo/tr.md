# WanGörüntüdenVideoya

WanImageToVideo düğümü, video oluşturma görevleri için conditioning ve latent temsillerini hazırlar. Video oluşturma için boş bir latent alan oluşturur ve isteğe bağlı olarak video oluşturma sürecini yönlendirmek için başlangıç görüntülerini ve CLIP vision çıktılarını dahil edebilir. Düğüm, sağlanan görüntü ve vision verilerine dayalı olarak hem pozitif hem de negatif conditioning girdilerini değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Oluşturmayı yönlendiren pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negatif` | Oluşturmayı yönlendiren negatif conditioning girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent alana kodlamak için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 to MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 to MAX_RESOLUTION |
| `toplu_boyut` | Bir toplu işlemde oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `clip_görü_çıktısı` | Ek conditioning için isteğe bağlı CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü. Sağlandığında, görüntü belirtilen genişlik ve yüksekliğe uyacak şekilde yeniden boyutlandırılır ve videonun ilk kareleri bu görüntüden başlatılır. Kalan kareler nötr gri (0.5) değerleriyle doldurulur. `length` değerini aşan kareler yok sayılır. | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini VAE kullanarak kodlar ve conditioning girdilerine bir maske uygular. Maske, başlangıç görüntüsüyle başlatılanlar dışındaki tüm kareleri kapsar ve oluşturmanın sağlanan görüntü üzerine inşa edilmesine olanak tanır. Kodlama sırasında görüntünün yalnızca ilk üç renk kanalı (RGB) kullanılır. `clip_vision_output` parametresi sağlandığında, hem pozitif hem de negatif girdilere vision tabanlı conditioning ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Görüntü ve vision verileri dahil edilmiş, değiştirilmiş pozitif conditioning | CONDITIONING |
| `negatif` | Görüntü ve vision verileri dahil edilmiş, değiştirilmiş negatif conditioning | CONDITIONING |
| `gizli` | Video oluşturma için hazır boş latent alan tensörü, şekli [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
