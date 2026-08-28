# StabilSıfır123_Koşullandırma

StableZero123_Conditioning düğümü, 3D model oluşturma için koşullandırma verileri ve latent temsiller üretmek amacıyla bir girdi görüntüsünü ve kamera açılarını işler. Görüntü özelliklerini kodlamak için bir CLIP vision modeli kullanır, bunları elevation ve azimut açılarına dayalı kamera embedding bilgisiyle birleştirir ve sonraki 3D oluşturma görevleri için pozitif ve negatif koşullandırma ile birlikte bir latent temsil üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip_görü` | Görüntü özelliklerini kodlamak için kullanılan CLIP vision modeli | CLIP_VISION | Evet | - |
| `başlangıç_görüntüsü` | İşlenecek ve kodlanacak girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Pikselleri latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `genişlik` | Latent temsil için çıktı genişliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `yükseklik` | Latent temsil için çıktı yüksekliği (varsayılan: 256, 8'e bölünebilir olmalıdır) | INT | Evet | 16 to MAX_RESOLUTION |
| `toplu_boyut` | Batch içinde oluşturulacak örnek sayısı (varsayılan: 1) | INT | Evet | 1 ile 4096 |
| `yükseklik` | Kamera yükseklik açısı (derece cinsinden) (varsayılan: 0.0) | FLOAT | Evet | -180.0 ile 180.0 |
| `azimut` | Kamera azimut açısı (derece cinsinden) (varsayılan: 0.0) | FLOAT | Evet | -180.0 ile 180.0 |

**Not:** `width` ve `height` parametreleri 8'e bölünebilir olmalıdır; düğüm, latent temsil boyutlarını oluşturmak için bunları otomatik olarak 8'e böler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Görüntü özelliklerini ve kamera embedding'lerini birleştiren pozitif koşullandırma verisi; birleştirilecek bir latent olarak VAE ile kodlanmış girdi görüntüsünü içerir | CONDITIONING |
| `negatif` | Sıfırla başlatılmış özelliklere ve sıfırla başlatılmış bir latent'e sahip negatif koşullandırma verisi | CONDITIONING |
| `gizli` | Boyutları [batch_size, 4, height//8, width//8] olan sıfırla başlatılmış latent temsil | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
