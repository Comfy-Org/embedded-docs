# WanEğlenceİçBoyamadanVideoya

WanFunInpaintToVideo düğümü, başlangıç ve bitiş görüntüleri arasında inpainting yaparak video dizileri oluşturur. Video latentleri üretmek için pozitif ve negatif conditioning ile birlikte isteğe bağlı kare görüntülerini alır. Düğüm, yapılandırılabilir boyut ve uzunluk parametreleriyle video üretimini yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video üretimi için pozitif conditioning istemleri | CONDITIONING | Evet | - |
| `negatif` | Video üretiminde kaçınılması gereken negatif conditioning istemleri | CONDITIONING | Evet | - |
| `vae` | Kodlama/kod çözme işlemleri için VAE modeli | VAE | Evet | - |
| `genişlik` | Piksel cinsinden çıktı video genişliği (varsayılan: 832, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `yükseklik` | Piksel cinsinden çıktı video yüksekliği (varsayılan: 480, adım: 16) | INT | Evet | 16 ile MAX_RESOLUTION arası |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ile MAX_RESOLUTION arası |
| `toplu_boyut` | Bir partide oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 arası |
| `clip_görü_çıktısı` | Başlangıç görüntüsü için conditioning olarak kullanılan isteğe bağlı CLIP vision çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video üretimi için isteğe bağlı başlangıç kare görüntüsü | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Video üretimi için isteğe bağlı bitiş kare görüntüsü | IMAGE | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | İşlenmiş pozitif conditioning çıktısı | CONDITIONING |
| `negatif` | İşlenmiş negatif conditioning çıktısı | CONDITIONING |
| `gizli` | Oluşturulan video latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
