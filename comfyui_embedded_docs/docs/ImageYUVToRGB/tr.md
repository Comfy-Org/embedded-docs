> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/tr.md)

ImageYUVToRGB düğümü, YUV renk uzayındaki görüntüleri RGB renk uzayına dönüştürür. Y (parlaklık), U (mavi çıkıntı) ve V (kırmızı çıkıntı) kanallarını temsil eden üç ayrı girdi görüntüsünü alır ve bunları renk uzayı dönüşümü kullanarak tek bir RGB görüntüsünde birleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Y` | IMAGE | Evet | - | Y (parlaklık) kanalı girdi görüntüsü |
| `U` | IMAGE | Evet | - | U (mavi çıkıntı) kanalı girdi görüntüsü |
| `V` | IMAGE | Evet | - | V (kırmızı çıkıntı) kanalı girdi görüntüsü |

**Not:** Üç girdi görüntüsünün (Y, U ve V) tamamı birlikte sağlanmalı ve uygun dönüşüm için uyumlu boyutlara sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Dönüştürülmüş RGB görüntü |