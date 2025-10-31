> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/tr.md)

Bu düğüm, belirli bir toplu işlemden, belirtilen toplu işlem indeksi ve uzunluğuna dayanarak belirli bir gizli örnek alt kümesini çıkarmak için tasarlanmıştır. Gizli örnekler üzerinde seçici işleme imkanı tanıyarak, verimlilik veya hedeflenen manipülasyon için toplu işlemin daha küçük bölümleri üzerinde işlem yapılmasını kolaylaştırır.

## Girdiler

| Parametre     | Veri Tipi | Açıklama |
|---------------|-------------|-------------|
| `samples`     | `LATENT`    | İçinden bir alt kümenin çıkarılacağı gizli örnekler koleksiyonu. Bu parametre, işlenecek kaynak örnek toplu işlemini belirlemek için çok önemlidir. |
| `batch_index` | `INT`       | Örnek alt kümesinin başlayacağı, toplu işlem içindeki başlangıç indeksini belirtir. Bu parametre, toplu işlemdeki belirli konumlardan örneklerin hedeflenmiş şekilde çıkarılmasını sağlar. |
| `length`      | `INT`       | Belirtilen başlangıç indeksinden itibaren çıkarılacak örnek sayısını tanımlar. Bu parametre, işlenecek alt kümenin boyutunu kontrol ederek, toplu işlem bölümlerinin esnek bir şekilde manipüle edilmesine olanak tanır. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Daha fazla işleme veya analiz için artık hazır olan, çıkarılan gizli örnek alt kümesi. |