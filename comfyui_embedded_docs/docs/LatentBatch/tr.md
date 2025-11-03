> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/tr.md)

LatentBatch düğümü, iki farklı gizli örnek setini tek bir toplu işlemde birleştirmek üzere tasarlanmıştır ve birleştirme işleminden önce setlerden birinin boyutlarını diğerine uyacak şekilde yeniden boyutlandırabilir. Bu işlem, daha fazla işleme veya üretim görevleri için farklı gizli temsillerin birleştirilmesini kolaylaştırır.

## Girdiler

| Parametre   | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `örnekler1`  | `LATENT`  | Birleştirilecek ilk gizli örnek seti. Birleştirilmiş toplu işlemin nihai şeklinin belirlenmesinde kritik bir rol oynar. |
| `örnekler2`  | `LATENT`  | Birleştirilecek ikinci gizli örnek seti. Boyutları ilk setten farklıysa, birleştirme işleminden önce uyumluluğu sağlamak için yeniden boyutlandırılır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `latent`  | `LATENT`  | Gizli örneklerin birleştirilmiş seti; artık daha fazla işleme için tek bir toplu işlem halinde bir araya getirilmiştir. |