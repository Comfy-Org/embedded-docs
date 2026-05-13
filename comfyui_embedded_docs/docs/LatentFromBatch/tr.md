> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/tr.md)

Bu düğüm, belirtilen batch indeksi ve uzunluğa göre belirli bir latent örnek alt kümesini verilen bir gruptan çıkarmak için tasarlanmıştır. Latent örneklerin seçici olarak işlenmesine olanak tanır; verimlilik veya hedefli müdahale amacıyla grubun daha küçük bölümleri üzerinde işlem yapılmasını kolaylaştırır.

## Girişler

| Parametre      | Veri Türü  | Açıklama |
|----------------|------------|----------|
| `samples`      | `LATENT`   | İçinden bir alt kümenin çıkarılacağı latent örneklerin koleksiyonu. Bu parametre, işlenecek kaynak örnek grubunun belirlenmesi için kritiktir. |
| `batch_index`  | `INT`      | Alt kümenin başlayacağı grup içindeki başlangıç indeksini belirtir. Bu parametre, gruptaki belirli konumlardan hedefli örnek çıkarımına olanak tanır. |
| `length`       | `INT`      | Belirtilen başlangıç indeksinden itibaren çıkarılacak örnek sayısını tanımlar. Bu parametre, işlenecek alt kümenin boyutunu kontrol ederek grup bölümlerinin esnek bir şekilde yönetilmesini sağlar. |

## Çıktılar

| Parametre | Veri Türü  | Açıklama |
|-----------|------------|----------|
| `latent`  | `LATENT`   | Çıkarılan latent örnek alt kümesi; artık daha ileri işleme veya analiz için kullanıma hazırdır. |