# GizliÇıkarma

LatentSubtract düğümü, bir gizli temsilin diğerinden çıkarılması için tasarlanmıştır. Bu işlem, bir gizli uzayda temsil edilen özellikleri veya nitelikleri etkili bir şekilde kaldırarak üretken modellerin çıktılarının özelliklerini değiştirmek veya düzenlemek için kullanılabilir.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler1` | Çıkarma işleminin yapılacağı ilk gizli örnek kümesi. Çıkarma işlemi için temel görevi görür. | `LATENT` |
| `örnekler2` | İlk kümeden çıkarılacak ikinci gizli örnek kümesi. Bu işlem, nitelikleri veya özellikleri kaldırarak ortaya çıkan üretken modelin çıktısını değiştirebilir. | `LATENT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | İkinci gizli örnek kümesinin birinciden çıkarılmasıyla elde edilen sonuç. Bu değiştirilmiş gizli temsil, daha sonraki üretken görevler için kullanılabilir. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/tr.md)
