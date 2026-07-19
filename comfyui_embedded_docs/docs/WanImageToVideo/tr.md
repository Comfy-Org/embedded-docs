# WanGörüntüdenVideoya

WanImageToVideo düğümü, video oluşturma görevleri için conditioning ve latent temsillerini hazırlar. Video oluşturma için boş bir latent alanı oluşturur ve isteğe bağlı olarak video oluşturma sürecini yönlendirmek için başlangıç görüntüleri ve CLIP görüş çıktılarını dahil edebilir. Düğüm, sağlanan görüntü ve görüş verilerine dayanarak hem pozitif hem de negatif conditioning girdilerini değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Oluşturmayı yönlendirmek için pozitif conditioning girdisi | CONDITIONING | Evet | - |
| `negatif` | Oluşturmayı yönlendirmek için negatif conditioning girdisi | CONDITIONING | Evet | - |
| `vae` | Görüntüleri latent alana kodlamak için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosunun genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION |
| `yükseklik` | Çıktı videosunun yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION |
| `uzunluk` | Videodaki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ile MAX_RESOLUTION |
| `toplu_boyut` | Bir grupta oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `clip_görü_çıktısı` | Ek conditioning için isteğe bağlı CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video oluşturmayı başlatmak için isteğe bağlı başlangıç görüntüsü | IMAGE | Hayır | - |

**Not:** `start_image` sağlandığında, düğüm görüntü dizisini kodlar ve conditioning girdilerine maskeleme uygular. `clip_vision_output` parametresi sağlandığında, hem pozitif hem de negatif girdilere görüş tabanlı conditioning ekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Görüntü ve görüş verileri dahil edilmiş, değiştirilmiş pozitif conditioning | CONDITIONING |
| `negatif` | Görüntü ve görüş verileri dahil edilmiş, değiştirilmiş negatif conditioning | CONDITIONING |
| `gizli` | Video oluşturma için hazır, boş latent alan tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
