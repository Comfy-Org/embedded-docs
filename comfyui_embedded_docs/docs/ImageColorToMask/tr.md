> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/tr.md)

`ImageColorToMask` düğümü, bir görüntüde belirli bir rengi maske'ye dönüştürmek için tasarlanmıştır. Bir görüntüyü ve bir hedef rengi işler, belirtilen rengin vurgulandığı bir maske oluşturur ve renk tabanlı segmentasyon veya nesne izolasyonu gibi işlemleri kolaylaştırır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | 'image' parametresi, işlenecek giriş görüntüsünü temsil eder. Görüntünün, belirtilen renkle eşleşen ve maske'ye dönüştürülecek alanlarını belirlemede çok önemlidir. |
| `renk`   | `INT`       | 'color' parametresi, görüntüde maske'ye dönüştürülecek hedef rengi belirtir. Ortaya çıkan maskede vurgulanacak belirli renk alanlarını tanımlamada kilit rol oynar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Çıktı, giriş görüntüsünün belirtilen renkle eşleşen alanlarını vurgulayan bir maskedir. Bu maske, segmentasyon veya nesne izolasyonu gibi daha ileri görüntü işleme görevleri için kullanılabilir. |