# LatentCutToBatch

LatentCutToBatch düğümü, bir latent gösterimi seçilen bir boyut boyunca (zaman, genişlik veya yükseklik) belirli boyuttaki dilimlere böler ve bunları yeni bir parti halinde istifler. Her dilim, parti içinde ayrı bir öğe haline gelir; böylece bir latent örneğinin farklı bölümleri bağımsız olarak işlenebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Bölünecek ve parti haline getirilecek latent gösterim. | LATENT | Evet | - |
| `dim` | Latent örneklerin kesileceği boyut. `"t"` zamansal (kare) boyutunu, `"x"` genişliği ve `"y"` yüksekliği ifade eder. | COMBO | Evet | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | Belirtilen boyuttan kesilecek her dilimin boyutu. Boyutun uzunluğu bu değere tam bölünemiyorsa, kalan kısım atılır. (varsayılan: 1) | INT | Evet | 1 ila 16384 (maksimum çözünürlük) |

Not: `"t"` seçeneği yalnızca latent bir zamansal boyut içerdiğinde etkili olur. Seçilen boyut, parti veya kanal konumuna karşılık geliyorsa ya da mevcut değilse (örneğin, kareleri olmayan bir latentte `"t"` seçilmesi), düğüm girdiyi değiştirmeden döndürür. `slice_size`, seçilen boyutun boyutundan büyükse, tüm boyut tek bir dilim olarak kullanılır. Boyutun uzunluğu `slice_size` değerine tam bölünemediğinde, sonda kalan kısım atılır. Çıktı parti boyutu, girdi parti boyutunun dilim sayısıyla çarpılmasıyla elde edilir ve dilimlenen boyutun kendisi `slice_size` değerine indirgenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Dilimlenmiş ve istiflenmiş örnekleri içeren sonuç latent partisi. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/tr.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
