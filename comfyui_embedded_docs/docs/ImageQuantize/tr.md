> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/tr.md)

ImageQuantize düğümü, bir görüntüdeki renk sayısını belirtilen sayıya düşürmek ve isteğe bağlı olarak görsel kaliteyi korumak için renk taklidi (dithering) teknikleri uygulamak üzere tasarlanmıştır. Bu işlem, palet tabanlı görüntüler oluşturmak veya belirli uygulamalar için renk karmaşıklığını azaltmak amacıyla kullanışlıdır.

## Girişler

| Alan    | Veri Türü | Açıklama                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------|
| `image` | `IMAGE`     | Nicemlenecek giriş görüntü tensörü. Renk azaltma işleminin gerçekleştirildiği birincil veri olduğu için düğümün yürütülmesini etkiler. |
| `colors`| `INT`       | Görüntünün indirgeneceği renk sayısını belirtir. Renk paleti boyutunu belirleyerek nicemleme sürecini doğrudan etkiler. |
| `dither`| COMBO[STRING] | Nicemleme sırasında uygulanacak renk taklidi tekniğini belirler; çıktı görüntüsünün görsel kalitesini ve görünümünü etkiler. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                                   |
|---------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | Giriş görüntüsünün nicemlenmiş sürümü; azaltılmış renk karmaşıklığına sahiptir ve görsel kaliteyi korumak için isteğe bağlı olarak renk taklidi uygulanmıştır. |