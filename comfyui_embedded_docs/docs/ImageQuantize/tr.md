> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/tr.md)

ImageQuantize düğümü, bir görüntüdeki renk sayısını belirtilen sayıya indirmek ve isteğe bağlı olarak görsel kaliteyi korumak için renk taklidi (dithering) teknikleri uygulamak üzere tasarlanmıştır. Bu işlem, palet tabanlı görüntüler oluşturmak veya belirli uygulamalar için renk karmaşıklığını azaltmak için kullanışlıdır.

## Girdiler

| Alan    | Veri Türü   | Açıklama                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------|
| `görüntü` | `IMAGE`     | Nicemlenecek girdi görüntü tensörü. Düğümün yürütülmesini, renk indirgeme işleminin gerçekleştirildiği birincil veri olarak etkiler. |
| `renkler`| `INT`       | Görüntünün indirgeneceği renk sayısını belirtir. Renk paleti boyutunu belirleyerek nicemleme işlemini doğrudan etkiler. |
| `titreşim`| COMBO[STRING] | Nicemleme sırasında uygulanacak renk taklidi tekniğini belirler; çıktı görüntüsünün görsel kalitesini ve görünümünü etkiler. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                                   |
|--------|-------------|-------------------------------------------------------------------------------|
| `görüntü`| `IMAGE`     | Girdi görüntüsünün nicemlenmiş versiyonu; azaltılmış renk karmaşıklığına sahiptir ve isteğe bağlı olarak görsel kaliteyi korumak için renk taklidi uygulanmıştır. |