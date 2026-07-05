# StabilSıfır123_Koşullandırma_Toplu

StableZero123_Conditioning_Batched düğümü, bir giriş görüntüsünü işler ve 3B model oluşturma için koşullandırma verileri üretir. CLIP vision ve VAE modellerini kullanarak görüntüyü kodlar, ardından yükseklik ve azimut açılarına dayalı kamera yerleştirmeleri oluşturarak toplu işleme için pozitif ve negatif koşullandırma ile birlikte gizli temsiller üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü` | Giriş görüntüsünü kodlamak için kullanılan CLIP vision modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | İşlenecek ve kodlanacak ilk giriş görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntü piksellerini gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | İşlenmiş görüntü için çıktı genişliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Hayır | 16 - MAX_RESOLUTION |
| `yükseklik` | İşlenmiş görüntü için çıktı yüksekliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Hayır | 16 - MAX_RESOLUTION |
| `toplu_boyut` | Toplu işlemde oluşturulacak koşullandırma örneklerinin sayısı (varsayılan: 1) | INT | Hayır | 1 - 4096 |
| `yükseklik` | Derece cinsinden ilk kamera yükseklik açısı (varsayılan: 0,0) | FLOAT | Hayır | -180,0 - 180,0 |
| `azimut` | Derece cinsinden ilk kamera azimut açısı (varsayılan: 0,0) | FLOAT | Hayır | -180,0 - 180,0 |
| `yükseklik_toplu_artışı` | Her toplu işlem öğesi için yüksekliğin artırılacağı miktar (varsayılan: 0,0) | FLOAT | Hayır | -180,0 - 180,0 |
| `azimut_toplu_artışı` | Her toplu işlem öğesi için azimutun artırılacağı miktar (varsayılan: 0,0) | FLOAT | Hayır | -180,0 - 180,0 |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır çünkü düğüm, gizli uzay oluşturma için bu boyutları dahili olarak 8'e böler.


| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntü yerleştirmeleri ve kamera parametrelerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Sıfır başlangıçlı yerleştirmelere sahip negatif koşullandırma verileri | CONDITIONING |
| `latent` | Toplu işlem indeksleme bilgisi ile işlenmiş görüntünün gizli temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/tr.md)

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`
