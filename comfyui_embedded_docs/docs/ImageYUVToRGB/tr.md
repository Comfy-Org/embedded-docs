> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/tr.md)

ImageYUVToRGB düğümü, YUV renk uzayındaki görüntüleri RGB renk uzayına dönüştürür. Y (parlaklık), U (mavi izdüşüm) ve V (kırmızı izdüşüm) kanallarını temsil eden üç ayrı giriş görüntüsünü alır ve renk uzayı dönüşümü kullanarak bunları tek bir RGB görüntüsünde birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Y` | IMAGE | Evet | - | Y (parlaklık) kanalı giriş görüntüsü |
| `U` | IMAGE | Evet | - | U (mavi izdüşüm) kanalı giriş görüntüsü |
| `V` | IMAGE | Evet | - | V (kırmızı izdüşüm) kanalı giriş görüntüsü |

**Not:** Üç giriş görüntüsünün (Y, U ve V) tümü birlikte sağlanmalı ve doğru dönüşüm için uyumlu boyutlara sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output` | IMAGE | Dönüştürülmüş RGB görüntüsü |

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
