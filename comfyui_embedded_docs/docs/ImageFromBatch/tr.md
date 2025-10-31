> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/tr.md)

`ImageFromBatch` düğümü, bir grup resimden belirli bir bölümü sağlanan indeks ve uzunluk değerlerine göre çıkarmak için tasarlanmıştır. Toplu haldeki resimler üzerinde daha ayrıntılı kontrol sağlayarak, daha büyük bir grup içindeki tek tek resimler veya resim alt kümeleri üzerinde işlemler yapılmasına olanak tanır.

## Girdiler

| Alan          | Veri Türü | Açıklama                                                                           |
|----------------|-------------|---------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | İçinden bir bölümün çıkarılacağı resim grubu. Bu parametre, kaynak grubu belirtmek için çok önemlidir. |
| `batch_index`  | `INT`       | Çıkarma işleminin başlayacağı, grup içindeki başlangıç indeksi. Çıkarılacak bölümün gruptaki başlangıç konumunu belirler. |
| `length`       | `INT`       | `batch_index`'ten başlayarak gruptan çıkarılacak resim sayısı. Bu parametre, çıkarılacak bölümün boyutunu tanımlar. |

## Çıktılar

| Alan | Veri Türü | Açıklama                                                                                   |
|-------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE`    | Belirtilen gruptan çıkarılan resim bölümü. Bu çıktı, orijinal grubun `batch_index` ve `length` parametreleri tarafından belirlenen bir alt kümesini temsil eder. |