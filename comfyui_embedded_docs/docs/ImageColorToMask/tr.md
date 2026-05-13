> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/tr.md)

`ImageColorToMask` düğümü, bir görüntüdeki belirli bir rengi maskeye dönüştürmek için tasarlanmıştır. Bir görüntü ve hedef rengi işleyerek, belirtilen rengin vurgulandığı bir maske oluşturur; bu sayede renk tabanlı bölütleme veya nesne ayırma gibi işlemleri kolaylaştırır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | 'image' parametresi, işlenecek giriş görüntüsünü temsil eder. Maskeye dönüştürülecek belirtilen renkle eşleşen görüntü alanlarının belirlenmesi açısından kritik öneme sahiptir. |
| `renk`   | `INT`       | 'color' parametresi, görüntüde maskeye dönüştürülecek hedef rengi belirtir. Ortaya çıkan maskede vurgulanacak belirli renk alanlarının tanımlanmasında anahtar rol oynar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Çıktı, giriş görüntüsünde belirtilen renkle eşleşen alanları vurgulayan bir maskedir. Bu maske, bölütleme veya nesne ayırma gibi ileri düzey görüntü işleme görevlerinde kullanılabilir. |