# GizliTopluİş

LatentBatch düğümü, iki latent örnek kümesini tek bir parti halinde birleştirmek ve birleştirme öncesinde gerekirse bir kümeyi diğerinin boyutlarına uyacak şekilde yeniden boyutlandırmak için tasarlanmıştır. Bu işlem, farklı latent temsillerin daha ileri işleme veya üretim görevleri için birleştirilmesini kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler1` | Birleştirilecek ilk latent örnek kümesi. Birleştirilmiş partinin nihai şeklinin belirlenmesinde önemli bir rol oynar. | `LATENT` |
| `örnekler2` | Birleştirilecek ikinci latent örnek kümesi. Boyutları ilk kümeden farklıysa, birleştirme öncesinde uyumluluğu sağlamak için yeniden boyutlandırılır. | `LATENT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Artık daha ileri işleme için tek bir partide birleştirilmiş olan latent örneklerin birleştirilmiş kümesi. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/tr.md)
