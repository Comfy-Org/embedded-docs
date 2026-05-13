> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/tr.md)

StableZero123_Conditioning_Batched düğümü, bir giriş görüntüsünü işler ve 3B model oluşturma için koşullandırma verileri üretir. CLIP vision ve VAE modellerini kullanarak görüntüyü kodlar, ardından yükseklik ve azimut açılarına dayalı kamera yerleştirmeleri oluşturarak toplu işleme için pozitif ve negatif koşullandırma ile birlikte gizli temsiller üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_görü` | CLIP_VISION | Evet | - | Giriş görüntüsünü kodlamak için kullanılan CLIP vision modeli |
| `başlangıç_görüntüsü` | IMAGE | Evet | - | İşlenecek ve kodlanacak ilk giriş görüntüsü |
| `vae` | VAE | Evet | - | Görüntü piksellerini gizli uzaya kodlamak için kullanılan VAE modeli |
| `genişlik` | INT | Hayır | 16 - MAX_RESOLUTION | İşlenmiş görüntü için çıktı genişliği (varsayılan: 256, 8'e bölünebilir olmalıdır) |
| `yükseklik` | INT | Hayır | 16 - MAX_RESOLUTION | İşlenmiş görüntü için çıktı yüksekliği (varsayılan: 256, 8'e bölünebilir olmalıdır) |
| `toplu_boyut` | INT | Hayır | 1 - 4096 | Toplu işlemde oluşturulacak koşullandırma örneklerinin sayısı (varsayılan: 1) |
| `yükseklik` | FLOAT | Hayır | -180,0 - 180,0 | Derece cinsinden ilk kamera yükseklik açısı (varsayılan: 0,0) |
| `azimut` | FLOAT | Hayır | -180,0 - 180,0 | Derece cinsinden ilk kamera azimut açısı (varsayılan: 0,0) |
| `yükseklik_toplu_artışı` | FLOAT | Hayır | -180,0 - 180,0 | Her toplu işlem öğesi için yüksekliğin artırılacağı miktar (varsayılan: 0,0) |
| `azimut_toplu_artışı` | FLOAT | Hayır | -180,0 - 180,0 | Her toplu işlem öğesi için azimutun artırılacağı miktar (varsayılan: 0,0) |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır çünkü düğüm, gizli uzay oluşturma için bu boyutları dahili olarak 8'e böler.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Görüntü yerleştirmeleri ve kamera parametrelerini içeren pozitif koşullandırma verileri |
| `gizli` | CONDITIONING | Sıfır başlangıçlı yerleştirmelere sahip negatif koşullandırma verileri |
| `latent` | LATENT | Toplu işlem indeksleme bilgisi ile işlenmiş görüntünün gizli temsili |

---
**Source fingerprint (SHA-256):** `2b770f7a168a0d3e33da8bfa63383080709fa5d53846dbf6a4374bd1ef1746aa`
