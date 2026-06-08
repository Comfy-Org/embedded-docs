Bu düğüm, belirtilen batch indeksi ve uzunluğa göre belirli bir latent örnek alt kümesini verilen bir gruptan çıkarmak için tasarlanmıştır. Latent örneklerin seçici olarak işlenmesine olanak tanır; verimlilik veya hedefli müdahale amacıyla grubun daha küçük bölümleri üzerinde işlem yapılmasını kolaylaştırır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `örnekler` | İçinden bir alt kümenin çıkarılacağı latent örneklerin koleksiyonu. Bu parametre, işlenecek kaynak örnek grubunun belirlenmesi için kritiktir. | `LATENT` |
| `toplu_indeks` | Alt kümenin başlayacağı grup içindeki başlangıç indeksini belirtir. Bu parametre, gruptaki belirli konumlardan hedefli örnek çıkarımına olanak tanır. | `INT` |
| `uzunluk` | Belirtilen başlangıç indeksinden itibaren çıkarılacak örnek sayısını tanımlar. Bu parametre, işlenecek alt kümenin boyutunu kontrol ederek grup bölümlerinin esnek bir şekilde yönetilmesini sağlar. | `INT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `latent` | Çıkarılan latent örnek alt kümesi; artık daha ileri işleme veya analiz için kullanıma hazırdır. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/tr.md)
