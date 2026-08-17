# StabilSıfır123_Koşullandırma_Toplu

StableZero123_Conditioning_Batched düğümü, Stable Zero123 modeli ile bir nesnenin 3B görünümlerini oluşturmak için gereken koşullandırma verilerini hazırlar. Girdi görüntüsünü bir CLIP görüş modeli ve bir VAE ile kodlar, görüntü özelliklerini toplu işteki her öğe için kamera yükseklik ve azimut açılarıyla birleştirir ve boş bir latent ile birlikte pozitif ve negatif koşullandırma çıktıları üretir. Toplu iş artış girdileri, toplu işteki ardışık her öğe için kamera açısını yükseltir veya alçaltır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_vision` | Girdi görüntüsünü görüntü yerleştirmelerine kodlamak için kullanılan CLIP görüş modeli | CLIP_VISION | Evet | - |
| `init_image` | İşlenecek ve kodlanacak ilk girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntü piksellerini latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | İşlenen görüntünün hedef genişliği (varsayılan: 256) | INT | Evet | 16 to MAX_RESOLUTION (step 8) |
| `height` | İşlenen görüntünün hedef yüksekliği (varsayılan: 256) | INT | Evet | 16 to MAX_RESOLUTION (step 8) |
| `batch_size` | Toplu işte oluşturulacak koşullandırma örneklerinin sayısı (varsayılan: 1) | INT | Evet | 1 to 4096 |
| `elevation` | Başlangıç kamera yükseklik açısı, derece cinsinden (varsayılan: 0.0) | FLOAT | Evet | -180.0 to 180.0 (step 0.1) |
| `azimuth` | Başlangıç kamera azimut açısı, derece cinsinden (varsayılan: 0.0) | FLOAT | Evet | -180.0 to 180.0 (step 0.1) |
| `elevation_batch_increment` | Toplu işteki ardışık her öğe için yükseklik açısına eklenen miktar (varsayılan: 0.0, gelişmiş parametre) | FLOAT | Evet | -180.0 to 180.0 (step 0.1) |
| `azimuth_batch_increment` | Toplu işteki ardışık her öğe için azimut açısına eklenen miktar (varsayılan: 0.0, gelişmiş parametre) | FLOAT | Evet | -180.0 to 180.0 (step 0.1) |

**Not:** `width` ve `height` değerleri 8'in katları olmalıdır (8'lik seçim adımı bunu zorunlu kılar) çünkü düğüm, latent boyutlarını oluşturmak için bu değerleri 8'e böler. Toplu işteki her öğe için `elevation` ve `azimuth` değerleri `elevation_batch_increment` ve `azimuth_batch_increment` kadar artırılır; böylece ardışık toplu iş öğeleri adım adım kamera açıları alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Oluşturma sırasında birleştirme için kullanılan görüntü yerleştirmelerini, kamera yerleştirmelerini ve kodlanmış girdi görüntüsünü birleştiren pozitif koşullandırma | CONDITIONING |
| `negative` | Birleştirme için sıfır başlatılmış görüntü yerleştirmelerini ve sıfır latent kullanan negatif koşullandırma | CONDITIONING |
| `latent` | (batch_size, 4, height/8, width/8) boyutlarında ve toplu iş dizini bilgisi içeren boş latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/tr.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
