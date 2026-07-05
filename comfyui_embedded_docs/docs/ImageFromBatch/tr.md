# TopluİşlemdenGörüntü

`ImageFromBatch` düğümü, bir görüntü grubundan (batch) belirtilen indeks ve uzunluğa göre belirli bir bölümü çıkarmak için tasarlanmıştır. Gruplanmış görüntüler üzerinde daha ayrıntılı kontrol sağlayarak, daha büyük bir grup içindeki tek tek veya alt küme görüntüler üzerinde işlem yapılmasına olanak tanır.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Bir bölümün çıkarılacağı görüntü grubu. Bu parametre, kaynak grubun belirtilmesi için kritiktir. | `IMAGE` |
| `toplu_indeks` | Çıkarma işleminin başlayacağı grup içindeki başlangıç indeksi. Gruptan çıkarılacak bölümün başlangıç konumunu belirler. | `INT` |
| `uzunluk` | `toplu_indeks`'ten başlayarak gruptan çıkarılacak görüntü sayısı. Bu parametre, çıkarılacak bölümün boyutunu tanımlar. | `INT` |


| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Belirtilen gruptan çıkarılan görüntü bölümü. Bu çıktı, `toplu_indeks` ve `uzunluk` parametreleri tarafından belirlenen, orijinal grubun bir alt kümesini temsil eder. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/tr.md)
