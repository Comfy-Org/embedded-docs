# LatentCutToBatch

LatentCutToBatch düğümü, bir latent temsilini seçilen bir boyut (zaman, genişlik veya yükseklik) boyunca belirtilen boyutta dilimlere böler ve bu dilimleri yeni bir batch içinde yığar. Her dilim batch içinde ayrı bir öğe haline gelir, böylece bir latent örneğinin farklı bölümleri bağımsız olarak işlenebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Bölünecek ve batch haline getirilecek latent temsili. | LATENT | Evet | - |
| `dim` | Latent örneklerinin hangi boyut boyunca kesileceği. `"t"` zamansal (kare) boyutu, `"x"` genişliği ve `"y"` yüksekliği belirtir. | COMBO | Evet | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | Belirtilen boyuttan kesilecek her bir dilimin boyutu. Boyutun büyüklüğü bu değere tam bölünemiyorsa kalan kısım atılır. (varsayılan: 1) | INT | Evet | 1 ila 16384 (maksimum çözünürlük) |

Not: `"t"` seçeneği yalnızca latent zamansal bir boyut içerdiğinde etkili olur. Seçilen boyut batch veya kanal konumuna karşılık geliyorsa ya da mevcut değilse (örneğin, kareleri olmayan bir latent üzerinde `"t"` seçildiğinde), düğüm girdiyi değiştirmeden döndürür. `slice_size` seçilen boyutun büyüklüğünden büyükse, tüm boyut tek bir dilim olarak kullanılır. Boyut büyüklüğü `slice_size` değerine tam bölünemediğinde, sondaki artık kısım atılır. Çıktı batch boyutu, girdi batch boyutunun dilim sayısıyla çarpımıdır ve dilimlenen boyutun kendisi `slice_size` değerine düşürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Dilimlenmiş ve yığılmış örnekleri içeren sonuç latent batch'i. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/tr.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
