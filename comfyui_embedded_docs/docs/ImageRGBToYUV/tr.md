# GörüntüRGB'denYUV'ye

ImageRGBToYUV düğümü, RGB'den YCbCr'ye renk dönüşümü kullanarak bir RGB görüntüsünü YUV tarzı renk bileşenlerine dönüştürür. Sonucu üç ayrı görüntüye ayırır — Y (parlaklık veya aydınlık), U (mavi fark kroma) ve V (kırmızı fark kroma) — ve her bileşeni girdiyle aynı genişlik ve yükseklikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Y, U ve V bileşenlerine dönüştürülecek girdi RGB görüntüsü. Görüntü bir alfa kanalı içeriyorsa yalnızca ilk üç (RGB) kanal kullanılır. | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `Y` | YUV renk uzayının parlaklık (aydınlık) bileşeni, üç kanallı görüntü olarak döndürülür | IMAGE |
| `U` | YUV renk uzayının mavi fark kroma bileşeni, üç kanallı görüntü olarak döndürülür | IMAGE |
| `V` | YUV renk uzayının kırmızı fark kroma bileşeni, üç kanallı görüntü olarak döndürülür | IMAGE |

Her çıktı, girdi görüntüsüyle aynı genişlik ve yüksekliğe sahiptir. İlgili Y, U veya V bileşeni üç kanalın tamamında yinelenir; böylece her çıktı standart bir üç kanallı görüntü olarak döndürülür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/tr.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
