# LatentCutToBatch

The LatentCutToBatch düğümü, bir gizli temsili (latent representation) seçilen bir boyut boyunca birden çok dilime ayırır ve bunları yeni bir toplu iş (batch) halinde istifler. Bu, gizli bir örneğin farklı bölümlerini bağımsız olarak işlemenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Bölünecek ve toplu iş haline getirilecek gizli temsil. | LATENT | Evet | - |
| `dim` | Gizli örneklerin kesileceği boyut. `"t"` zaman boyutunu, `"x"` genişliği ve `"y"` yüksekliği ifade eder. | COMBO | Evet | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | Belirtilen boyuttan kesilecek her bir dilimin boyutu. Boyutun boyutu bu değere tam olarak bölünemiyorsa, kalan kısım atılır. (varsayılan: 1) | INT | Evet | 1 ila 16384 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Dilimlenmiş ve istiflenmiş örnekleri içeren sonuçtaki gizli toplu iş. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/tr.md)

---
**Source fingerprint (SHA-256):** `38d0ace3ef91e47e3f047aa7057c61e09b6534702526b34691b4bc239c933cd3`
