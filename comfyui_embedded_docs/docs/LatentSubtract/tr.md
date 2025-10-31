> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/tr.md)

LatentSubtract düğümü, bir gizli temsili diğerinden çıkarmak için tasarlanmıştır. Bu işlem, bir gizli uzayda temsil edilen özellikleri veya nitelikleri diğerinden etkili bir şekilde kaldırarak, üretken modellerin çıktılarının karakteristiklerini manipüle etmek veya değiştirmek için kullanılabilir.

## Girdiler

| Parametre   | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | Üzerinden çıkarma işlemi yapılacak birinci gizli örnekler kümesi. Çıkarma işlemi için temel oluşturur. |
| `samples2`   | `LATENT`    | Birinci kümeden çıkarılacak ikinci gizli örnekler kümesi. Bu işlem, nitelikleri veya özellikleri kaldırarak, ortaya çıkan üretken modelin çıktısını değiştirebilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | İkinci gizli örnekler kümesinin birinciden çıkarılması sonucu. Bu değiştirilmiş gizli temsil, ileri üretken görevler için kullanılabilir. |