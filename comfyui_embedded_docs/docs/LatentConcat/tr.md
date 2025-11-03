> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/tr.md)

LatentConcat düğümü, iki gizli örneği belirtilen bir boyut boyunca birleştirir. İki gizli girdi alır ve bunları seçilen eksen (x, y veya t boyutu) boyunca birleştirir. Düğüm, birleştirme işlemini gerçekleştirmeden önce ikinci girdinin toplu işlem boyutunu otomatik olarak ilk girdiyle eşleşecek şekilde ayarlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Evet | - | Birleştirilecek ilk gizli örnek |
| `samples2` | LATENT | Evet | - | Birleştirilecek ikinci gizli örnek |
| `dim` | COMBO | Evet | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | Gizli örneklerin birleştirileceği boyut. Pozitif değerler samples1'i samples2'den önce birleştirir, negatif değerler samples2'yi samples1'den önce birleştirir |

**Not:** İkinci gizli örnek (`samples2`), birleştirme işleminden önce otomatik olarak ilk gizli örneğin (`samples1`) toplu işlem boyutuyla eşleşecek şekilde ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | İki girdi örneğinin belirtilen boyut boyunca birleştirilmesi sonucu oluşan birleştirilmiş gizli örnekler |