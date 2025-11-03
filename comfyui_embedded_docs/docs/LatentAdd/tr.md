> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/tr.md)

LatentAdd düğümü, iki gizli temsilin toplanması için tasarlanmıştır. Bu temsillerde kodlanmış özellik veya karakteristiklerin birleştirilmesini, eleman bazlı toplama işlemi gerçekleştirerek kolaylaştırır.

## Girdiler

| Parametre   | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `örnekler1`   | `LATENT`    | Eklenecek ilk gizli örnekler kümesi. Özelliklerinin başka bir gizli örnekler kümesiyle birleştirileceği girdilerden birini temsil eder. |
| `örnekler2`   | `LATENT`    | Eklenecek ikinci gizli örnekler kümesi. Özelliklerinin ilk gizli örnekler kümesiyle eleman bazlı toplama yoluyla birleştirileceği diğer girdiyi sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | İki gizli örneğin eleman bazlı toplamının sonucu olan ve her iki girdinin özelliklerini birleştiren yeni bir gizli örnekler kümesini temsil eder. |