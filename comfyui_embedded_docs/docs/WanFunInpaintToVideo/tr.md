> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/tr.md)

WanFunInpaintToVideo düğümü, başlangıç ve bitiş görüntüleri arasında iç boyama (inpainting) yaparak video dizileri oluşturur. İsteğe bağlı kare görüntüleriyle birlikte pozitif ve negatif koşullandırma alarak video gizil (latent) değişkenleri üretir. Düğüm, yapılandırılabilir boyut ve uzunluk parametreleriyle video oluşturmayı yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Video oluşturma için pozitif koşullandırma yönlendirmeleri |
| `negatif` | CONDITIONING | Evet | - | Video oluşturmada kaçınılması gereken negatif koşullandırma yönlendirmeleri |
| `vae` | VAE | Evet | - | Kodlama/kod çözme işlemleri için VAE modeli |
| `genişlik` | INT | Evet | 16 ila MAKSİMUM_ÇÖZÜNÜRLÜK | Çıktı videosu genişliği piksel cinsinden (varsayılan: 832, adım: 16) |
| `yükseklik` | INT | Evet | 16 ila MAKSİMUM_ÇÖZÜNÜRLÜK | Çıktı videosu yüksekliği piksel cinsinden (varsayılan: 480, adım: 16) |
| `uzunluk` | INT | Evet | 1 ila MAKSİMUM_ÇÖZÜNÜRLÜK | Video dizisindeki kare sayısı (varsayılan: 81, adım: 4) |
| `toplu_boyut` | INT | Evet | 1 ila 4096 | Bir grupta oluşturulacak video sayısı (varsayılan: 1) |
| `clip_görü_çıktısı` | CLIP_VISION_OUTPUT | Hayır | - | Ek koşullandırma için isteğe bağlı CLIP görüş çıktısı |
| `başlangıç_görüntüsü` | IMAGE | Hayır | - | Video oluşturma için isteğe bağlı başlangıç karesi görüntüsü |
| `bitiş_görüntüsü` | IMAGE | Hayır | - | Video oluşturma için isteğe bağlı bitiş karesi görüntüsü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | İşlenmiş pozitif koşullandırma çıktısı |
| `gizli` | CONDITIONING | İşlenmiş negatif koşullandırma çıktısı |
| `latent` | LATENT | Oluşturulan video gizil (latent) temsili |

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
