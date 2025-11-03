> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/tr.md)

ImageRGBToYUV düğümü, RGB renkli görüntüleri YUV renk uzayına dönüştürür. Bir RGB görüntüsünü girdi olarak alır ve onu üç ayrı kanala ayırır: Y (parlaklık), U (mavi çıkıntı) ve V (kırmızı çıkıntı). Her çıktı kanalı, ilgili YUV bileşenini temsil eden ayrı bir gri tonlamalı görüntü olarak döndürülür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | YUV renk uzayına dönüştürülecek girdi RGB görüntüsü |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `U` | IMAGE | YUV renk uzayının parlaklık bileşeni |
| `V` | IMAGE | YUV renk uzayının mavi çıkıntı bileşeni |
| `V` | IMAGE | YUV renk uzayının kırmızı çıkıntı bileşeni |