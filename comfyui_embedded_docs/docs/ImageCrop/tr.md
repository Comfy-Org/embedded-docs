> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/tr.md)

`ImageCrop` düğümü, belirtilen bir x ve y koordinatından başlayarak, görüntüleri belirli bir genişlik ve yüksekliğe kırpmak için tasarlanmıştır. Bu işlevsellik, bir görüntünün belirli bölgelerine odaklanmak veya görüntü boyutunu belirli gereksinimleri karşılayacak şekilde ayarlamak için gereklidir.

## Girişler

| Alan | Veri Türü | Açıklama                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `görüntü` | `IMAGE` | Kırpılacak giriş görüntüsü. Bu parametre, belirtilen boyutlara ve koordinatlara göre bir bölgenin çıkarılacağı kaynak görüntüyü tanımladığı için çok önemlidir. |
| `genişlik` | `INT` | Kırpılan görüntünün genişliğini belirtir. Bu parametre, elde edilen kırpılmış görüntünün ne kadar geniş olacağını belirler. |
| `yükseklik` | `INT` | Kırpılan görüntünün yüksekliğini belirtir. Bu parametre, elde edilen kırpılmış görüntünün yüksekliğini belirler. |
| `x` | `INT` | Kırpma alanının sol üst köşesinin x koordinatı. Bu parametre, kırpma işleminin genişlik boyutu için başlangıç noktasını ayarlar. |
| `y` | `INT` | Kırpma alanının sol üst köşesinin y koordinatı. Bu parametre, kırpma işleminin yükseklik boyutu için başlangıç noktasını ayarlar. |

## Çıktılar

| Alan | Veri Türü | Açıklama                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `görüntü` | `IMAGE` | Kırpma işleminin sonucu olarak elde edilen kırpılmış görüntü. Bu çıktı, belirtilen görüntü bölgesinin daha fazla işlenmesi veya analizi için önemlidir. |