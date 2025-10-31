> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/tr.md)

`ImageCrop` düğümü, belirli bir x ve y koordinatından başlayarak görüntüleri belirtilen genişlik ve yüksekliğe göre kırpmak için tasarlanmıştır. Bu işlevsellik, bir görüntünün belirli bölgelerine odaklanmak veya görüntü boyutunu belirli gereksinimleri karşılayacak şekilde ayarlamak için gereklidir.

## Girişler

| Alan | Veri Türü | Açıklama |
|-------|-------------|---------------|
| `image` | `IMAGE` | Kırpılacak giriş görüntüsü. Bu parametre, belirtilen boyutlar ve koordinatlar temel alınarak bir bölgenin çıkarılacağı kaynak görüntüyü tanımladığı için çok önemlidir. |
| `width` | `INT` | Kırpılan görüntünün genişliğini belirtir. Bu parametre, ortaya çıkacak kırpılmış görüntünün ne kadar geniş olacağını belirler. |
| `height` | `INT` | Kırpılan görüntünün yüksekliğini belirtir. Bu parametre, ortaya çıkacak kırpılmış görüntünün yüksekliğini belirler. |
| `x` | `INT` | Kırpma alanının sol üst köşesinin x koordinatı. Bu parametre, kırpma işleminin genişlik boyutu için başlangıç noktasını ayarlar. |
| `y` | `INT` | Kırpma alanının sol üst köşesinin y koordinatı. Bu parametre, kırpma işleminin yükseklik boyutu için başlangıç noktasını ayarlar. |

## Çıkışlar

| Alan | Veri Türü | Açıklama |
|-------|-------------|---------------|
| `image` | `IMAGE` | Kırpma işleminin bir sonucu olarak elde edilen kırpılmış görüntü. Bu çıktı, belirtilen görüntü bölgesinin daha fazla işlenmesi veya analizi için önemlidir. |