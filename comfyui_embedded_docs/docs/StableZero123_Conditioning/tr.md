# StabilSıfır123_Koşullandırma

StableZero123_Conditioning düğümü, 3D model üretimi için koşullandırma verileri ve latent temsiller üretmek üzere bir giriş görüntüsünü ve kamera açılarını işler. Görüntü özelliklerini kodlamak için bir CLIP vision modeli kullanır, bunları elevasyon ve azimut açılarına dayalı kamera gömme bilgileriyle birleştirir ve alt akış 3D üretim görevleri için pozitif ve negatif koşullandırma ile bir latent temsil üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_vision` | Görüntü özelliklerini kodlamak için kullanılan CLIP vision modeli | CLIP_VISION | Evet | - |
| `init_image` | İşlenecek ve kodlanacak giriş görüntüsü | IMAGE | Evet | - |
| `vae` | Pikselleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Latent temsil için çıktı genişliği (varsayılan: 256, adım: 8) | INT | Evet | 16 - MAX_RESOLUTION |
| `height` | Latent temsil için çıktı yüksekliği (varsayılan: 256, adım: 8) | INT | Evet | 16 - MAX_RESOLUTION |
| `batch_size` | Partide üretilecek örnek sayısı (varsayılan: 1) | INT | Evet | 1 - 4096 |
| `elevation` | Derece cinsinden kamera elevasyon açısı (varsayılan: 0.0, adım: 0.1) | FLOAT | Evet | -180.0 - 180.0 |
| `azimuth` | Derece cinsinden kamera azimut açısı (varsayılan: 0.0, adım: 0.1) | FLOAT | Evet | -180.0 - 180.0 |

**Not:** `width` ve `height` parametreleri 8'lik adım kullanır, bu nedenle değerler 8'in katları olarak ayarlanır. Düğüm, latent temsil boyutlarını belirlemek için bunları 8'e böler. Görüntü, VAE kodlamasından önce merkez kırpma ile bilineer üst ölçekleme kullanılarak verilen `width` ve `height` değerlerine yeniden ölçeklendirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntü özellikleri ile kamera gömmelerini birleştiren, birleştirilecek latent olarak VAE ile kodlanmış giriş görüntüsünü içeren pozitif koşullandırma verisi | CONDITIONING |
| `negative` | Sıfırla başlatılmış özellikler ve sıfırla başlatılmış latent içeren negatif koşullandırma verisi | CONDITIONING |
| `latent` | [batch_size, 4, height//8, width//8] boyutlarında sıfırla başlatılmış latent temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
