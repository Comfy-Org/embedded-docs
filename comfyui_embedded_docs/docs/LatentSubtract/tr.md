> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/tr.md)

LatentSubtract düğümü, bir gizli temsilin diğerinden çıkarılması için tasarlanmıştır. Bu işlem, bir gizli uzayda temsil edilen özellikleri veya nitelikleri etkili bir şekilde kaldırarak üretken modellerin çıktılarının özelliklerini değiştirmek veya düzenlemek için kullanılabilir.

## Girişler

| Parametre    | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `örnekler1`   | `LATENT`    | Çıkarma işleminin yapılacağı ilk gizli örnek kümesi. Çıkarma işlemi için temel görevi görür. |
| `örnekler2`   | `LATENT`    | İlk kümeden çıkarılacak ikinci gizli örnek kümesi. Bu işlem, nitelikleri veya özellikleri kaldırarak ortaya çıkan üretken modelin çıktısını değiştirebilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | İkinci gizli örnek kümesinin birinciden çıkarılmasıyla elde edilen sonuç. Bu değiştirilmiş gizli temsil, daha sonraki üretken görevler için kullanılabilir. |