# Görüntü Kırp

`ImageCrop` düğümü, belirtilen bir x ve y koordinatından başlayarak, görüntüleri belirli bir genişlik ve yüksekliğe kırpmak için tasarlanmıştır. Bu işlevsellik, bir görüntünün belirli bölgelerine odaklanmak veya görüntü boyutunu belirli gereksinimleri karşılayacak şekilde ayarlamak için gereklidir.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Kırpılacak giriş görüntüsü. Bu parametre, belirtilen boyutlara ve koordinatlara göre bir bölgenin çıkarılacağı kaynak görüntüyü tanımladığı için çok önemlidir. | `IMAGE` |
| `genişlik` | Kırpılan görüntünün genişliğini belirtir. Bu parametre, elde edilen kırpılmış görüntünün ne kadar geniş olacağını belirler. | `INT` |
| `yükseklik` | Kırpılan görüntünün yüksekliğini belirtir. Bu parametre, elde edilen kırpılmış görüntünün yüksekliğini belirler. | `INT` |
| `x` | Kırpma alanının sol üst köşesinin x koordinatı. Bu parametre, kırpma işleminin genişlik boyutu için başlangıç noktasını ayarlar. | `INT` |
| `y` | Kırpma alanının sol üst köşesinin y koordinatı. Bu parametre, kırpma işleminin yükseklik boyutu için başlangıç noktasını ayarlar. | `INT` |


| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Kırpma işleminin sonucu olarak elde edilen kırpılmış görüntü. Bu çıktı, belirtilen görüntü bölgesinin daha fazla işlenmesi veya analizi için önemlidir. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/tr.md)
