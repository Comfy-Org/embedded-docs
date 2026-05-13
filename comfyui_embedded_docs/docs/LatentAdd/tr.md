> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/tr.md)

LatentAdd düğümü, iki gizli temsilin (latent representation) toplanması için tasarlanmıştır. Bu temsillerde kodlanmış özelliklerin veya niteliklerin, öğe bazında toplama işlemi yapılarak birleştirilmesini sağlar.

## Girişler

| Parametre    | Veri Türü    | Açıklama |
|--------------|--------------|-------------|
| `örnekler1`   | `LATENT`     | Toplanacak ilk gizli örnek kümesi. Özellikleri başka bir gizli örnek kümesiyle birleştirilecek olan girdilerden birini temsil eder. |
| `örnekler2`   | `LATENT`     | Toplanacak ikinci gizli örnek kümesi. Özellikleri, öğe bazında toplama yoluyla ilk gizli örnek kümesiyle birleştirilen diğer girdi olarak işlev görür. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-----------|
| `latent`  | `LATENT`    | İki gizli örneğin öğe bazında toplanmasının sonucu. Her iki girdinin özelliklerini birleştiren yeni bir gizli örnek kümesini temsil eder. |