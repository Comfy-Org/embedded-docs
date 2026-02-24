> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/tr.md)

LatentCutToBatch düğümü, bir gizli temsili alır ve belirtilen bir boyut boyunca birden fazla dilime böler. Bu dilimler daha sonra yeni bir toplu iş boyutunda istiflenir, böylece tek bir gizli örnek, daha küçük gizli örneklerden oluşan bir toplu işe dönüştürülür. Bu, gizli uzayın farklı bölümlerini bağımsız olarak işlemek için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Evet | - | Bölünecek ve toplu işlenecek gizli temsil. |
| `dim` | COMBO | Evet | `"t"`<br>`"x"`<br>`"y"` | Gizli örneklerin kesileceği boyut. `"t"` zamansal boyutu, `"x"` genişliği, `"y"` ise yüksekliği ifade eder. |
| `slice_size` | INT | Evet | 1 - 16384 | Belirtilen boyuttan kesilecek her bir dilimin boyutu. Boyutun boyutu bu değere tam olarak bölünemezse, kalan kısım atılır. (varsayılan: 1) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `samples` | LATENT | Dilimlenmiş ve istiflenmiş örnekleri içeren, ortaya çıkan gizli toplu iş. |
