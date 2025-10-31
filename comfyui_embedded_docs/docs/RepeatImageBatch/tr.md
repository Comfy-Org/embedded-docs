> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/tr.md)

RepeatImageBatch düğümü, belirli bir görüntüyü belirtilen sayıda kopyalayarak aynı görüntülerden oluşan bir toplu işlem oluşturmak için tasarlanmıştır. Bu işlevsellik, toplu işleme veya veri artırma gibi aynı görüntünün birden fazla kopyasını gerektiren işlemler için kullanışlıdır.

## Girdiler

| Alan     | Veri Türü | Açıklama                                                                 |
|----------|-----------|--------------------------------------------------------------------------|
| `image`  | `IMAGE`   | 'image' parametresi, çoğaltılacak görüntüyü temsil eder. Toplu işlem boyunca kopyalanacak içeriği tanımlamak için kritik öneme sahiptir. |
| `amount` | `INT`     | 'amount' parametresi, girdi görüntüsünün kaç kez çoğaltılacağını belirtir. Çıktı toplu işleminin boyutunu doğrudan etkileyerek esnek toplu işlem oluşturma imkanı sağlar. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                              |
|--------|-----------|-----------------------------------------------------------------------|
| `image`| `IMAGE`   | Çıktı, her biri girdi görüntüsünün aynısı olan ve belirtilen 'amount' değerine göre çoğaltılmış görüntülerden oluşan bir toplu işlemdir. |