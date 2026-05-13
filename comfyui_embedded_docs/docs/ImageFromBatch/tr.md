> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/tr.md)

`ImageFromBatch` düğümü, bir görüntü grubundan (batch) belirtilen indeks ve uzunluğa göre belirli bir bölümü çıkarmak için tasarlanmıştır. Gruplanmış görüntüler üzerinde daha ayrıntılı kontrol sağlayarak, daha büyük bir grup içindeki tek tek veya alt küme görüntüler üzerinde işlem yapılmasına olanak tanır.

## Girişler

| Alan           | Veri Türü | Açıklama                                                                                   |
|----------------|-------------|-----------------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | Bir bölümün çıkarılacağı görüntü grubu. Bu parametre, kaynak grubun belirtilmesi için kritiktir. |
| `batch_index`  | `INT`       | Çıkarma işleminin başlayacağı grup içindeki başlangıç indeksi. Gruptan çıkarılacak bölümün başlangıç konumunu belirler. |
| `length`       | `INT`       | `batch_index`'ten başlayarak gruptan çıkarılacak görüntü sayısı. Bu parametre, çıkarılacak bölümün boyutunu tanımlar. |

## Çıktılar

| Alan   | Veri Türü | Açıklama                                                                                   |
|--------|-------------|-----------------------------------------------------------------------------------------------|
| `image` | `IMAGE`    | Belirtilen gruptan çıkarılan görüntü bölümü. Bu çıktı, `batch_index` ve `length` parametreleri tarafından belirlenen, orijinal grubun bir alt kümesini temsil eder. |