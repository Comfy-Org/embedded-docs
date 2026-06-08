ImageRGBToYUV düğümü, RGB renkli görüntüleri YUV renk uzayına dönüştürür. Giriş olarak bir RGB görüntüsü alır ve bunu üç ayrı kanala ayırır: Y (parlaklık), U (mavi izdüşümü) ve V (kırmızı izdüşümü). Her çıkış kanalı, ilgili YUV bileşenini temsil eden ayrı bir gri tonlamalı görüntü olarak döndürülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | YUV renk uzayına dönüştürülecek giriş RGB görüntüsü | IMAGE | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `Y` | YUV renk uzayının parlaklık (aydınlık) bileşeni | IMAGE |
| `U` | YUV renk uzayının mavi izdüşüm bileşeni | IMAGE |
| `V` | YUV renk uzayının kırmızı izdüşüm bileşeni | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/tr.md)

---
**Source fingerprint (SHA-256):** `119cba119b62c7b46ffdd2c0feca932a9af1ec41c338fead23c21fdf76a6abb2`
