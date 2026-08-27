# StabilSıfır123_Koşullandırma_Toplu

StableZero123_Conditioning_Batched düğümü, tek bir giriş görüntüsünden 3B model oluşturmak için koşullandırma verilerini hazırlar. Görüntüyü bir CLIP görüş modeli ve bir VAE ile kodlar, görsel özellikleri yükseklik ve azimut açılarından oluşturulan kamera gömme vektörleriyle birleştirir ve bir örnek grubu için pozitif ve negatif koşullandırmanın yanı sıra bir latent tensör üretir. `batch_size` 1'den büyük olduğunda, gruptaki her öğe için yükseklik ve azimut açıları, grup artış değerleri kadar artırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_görü` | Giriş görüntüsünü kodlamak için kullanılan CLIP görüş modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | İşlenecek ve kodlanacak başlangıç giriş görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntü piksellerini latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | İşlenen görüntünün çıktı genişliği (varsayılan: 256) | INT | Evet | 16 to MAX_RESOLUTION (step of 8) |
| `yükseklik` | İşlenen görüntünün çıktı yüksekliği (varsayılan: 256) | INT | Evet | 16 to MAX_RESOLUTION (step of 8) |
| `toplu_boyut` | Grupta oluşturulacak koşullandırma örneği sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `yükseklik` | Kameranın başlangıç yükseklik açısı, derece cinsinden (varsayılan: 0.0) | FLOAT | Evet | -180.0 ile 180.0 |
| `azimut` | Kameranın başlangıç azimut açısı, derece cinsinden (varsayılan: 0.0) | FLOAT | Evet | -180.0 ile 180.0 |
| `yükseklik_toplu_artışı` | Gruptaki her öğe için yüksekliğin artırılma miktarı (varsayılan: 0.0) | FLOAT | Evet | -180.0 ile 180.0 |
| `azimut_toplu_artışı` | Gruptaki her öğe için azimutun artırılma miktarı (varsayılan: 0.0) | FLOAT | Evet | -180.0 ile 180.0 |

**Not:** `width` ve `height` değerleri 8'in katı olmalıdır; çünkü düğüm, latent tensörü oluştururken bu boyutları dahili olarak 8'e böler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Her grup öğesi için görüntü gömme vektörlerini ve kamera gömme vektörlerini içeren pozitif koşullandırma verileri | CONDITIONING |
| `negatif` | Sıfırla başlatılmış gömme vektörlerine sahip negatif koşullandırma verileri | CONDITIONING |
| `gizli` | batch_size x 4 x height/8 x width/8 boyutlarında, sıfırla başlatılmış latent tensör ve grup indeksleme bilgileri | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/tr.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
