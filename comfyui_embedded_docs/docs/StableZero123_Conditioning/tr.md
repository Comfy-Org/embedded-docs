# StabilSıfır123_Koşullandırma

The StableZero123_Conditioning düğümü, 3B model üretimi için koşullandırma verileri ve latent temsiller oluşturmak amacıyla bir girdi görüntüsünü ve kamera açılarını işler. Görüntü özelliklerini kodlamak için bir CLIP görme modeli kullanır, bunları yükseklik ve azimut açılarına dayalı kamera embedding bilgisiyle birleştirir ve alt akış 3B üretim görevleri için pozitif ve negatif koşullandırma ile birlikte bir latent temsil üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_vision` | Görüntü özelliklerini kodlamak için kullanılan CLIP görme modeli | CLIP_VISION | Evet | - |
| `init_image` | İşlenecek ve kodlanacak girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Pikselleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `width` | Latent temsil için çıktı genişliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `height` | Latent temsil için çıktı yüksekliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Evet | 16 ila MAX_RESOLUTION |
| `batch_size` | Partide üretilecek örnek sayısı (varsayılan: 1) | INT | Evet | 1 ila 4096 |
| `elevation` | Kamera yükseklik açısı (derece cinsinden) (varsayılan: 0.0) | FLOAT | Evet | -180.0 ila 180.0 |
| `azimuth` | Kamera azimut açısı (derece cinsinden) (varsayılan: 0.0) | FLOAT | Evet | -180.0 ila 180.0 |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır; çünkü düğüm, latent temsil boyutlarını oluşturmak için bunları otomatik olarak 8'e böler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Görüntü özelliklerini ve kamera embedding bilgilerini birleştiren pozitif koşullandırma verileri | CONDITIONING |
| `negative` | Sıfırla başlatılmış özelliklere sahip negatif koşullandırma verileri | CONDITIONING |
| `latent` | [batch_size, 4, height//8, width//8] boyutlarına sahip latent temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
