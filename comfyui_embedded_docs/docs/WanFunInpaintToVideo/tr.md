# WanEğlenceİçBoyamadanVideoya

WanFunInpaintToVideo düğümü, başlangıç ve bitiş görüntüleri arasında iç boyama (inpainting) yaparak video dizileri oluşturur. İsteğe bağlı kare görüntüleriyle birlikte pozitif ve negatif koşullandırma alarak video gizil (latent) değişkenleri üretir. Düğüm, yapılandırılabilir boyut ve uzunluk parametreleriyle video oluşturmayı yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Video oluşturma için pozitif koşullandırma yönlendirmeleri | CONDITIONING | Evet | - |
| `negatif` | Video oluşturmada kaçınılması gereken negatif koşullandırma yönlendirmeleri | CONDITIONING | Evet | - |
| `vae` | Kodlama/kod çözme işlemleri için VAE modeli | VAE | Evet | - |
| `genişlik` | Çıktı videosu genişliği piksel cinsinden (varsayılan: 832, adım: 16) | INT | Evet | 16 ila MAKSİMUM_ÇÖZÜNÜRLÜK |
| `yükseklik` | Çıktı videosu yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) | INT | Evet | 16 ila MAKSİMUM_ÇÖZÜNÜRLÜK |
| `uzunluk` | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) | INT | Evet | 1 ila MAKSİMUM_ÇÖZÜNÜRLÜK |
| `toplu_boyut` | Bir grupta oluşturulacak video sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `clip_görü_çıktısı` | Ek koşullandırma için isteğe bağlı CLIP görüş çıktısı | CLIP_VISION_OUTPUT | Hayır | - |
| `başlangıç_görüntüsü` | Video oluşturma için isteğe bağlı başlangıç karesi görüntüsü | IMAGE | Hayır | - |
| `bitiş_görüntüsü` | Video oluşturma için isteğe bağlı bitiş karesi görüntüsü | IMAGE | Hayır | - |


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | İşlenmiş pozitif koşullandırma çıktısı | CONDITIONING |
| `negative` | İşlenmiş negatif koşullandırma çıktısı | CONDITIONING |
| `latent` | Oluşturulan video gizil (latent) temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
