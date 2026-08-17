# LatentCutToBatch

The LatentCutToBatch düğümü, bir latent gösterimi seçilen bir boyut boyunca birden çok dilime ayırır ve bunları yeni bir batch (yığın) halinde istifler. Bu sayede bir latent örneğin farklı kısımlarını bağımsız olarak işleyebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Bölünecek ve batch haline getirilecek latent gösterim. | LATENT | Evet | - |
| `dim` | Latent örneklerin kesileceği boyut. `"t"` zamansal boyutu, `"x"` genişliği, `"y"` ise yüksekliği ifade eder. | COMBO | Evet | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | Belirtilen boyuttan kesilecek her dilimin boyutu. Boyutun boyutu bu değere tam bölünemiyorsa, kalan kısım atılır. (varsayılan: 1) | INT | Evet | 1 ila 16384 (maksimum çözünürlük) |

Not: Seçilen boyut batch veya kanal ekseni ise, girdi değiştirilmeden döndürülür. `slice_size` boyutun boyutundan büyükse, boyutun tamamı tek bir dilim olarak kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `samples` | Dilimlenmiş ve istiflenmiş örnekleri içeren sonuç latent batch'i. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/tr.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
