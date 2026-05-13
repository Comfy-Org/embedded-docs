> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/tr.md)

LatentConcat düğümü, iki gizli (latent) örneği seçilen bir boyut boyunca birleştirerek bir araya getirir. İki gizli girdi alır ve bunları x, y veya t ekseni boyunca birleştirir; hangi örneğin önce geleceğini kontrol etme seçeneği sunar. Düğüm, birleştirme işlemini gerçekleştirmeden önce ikinci girdinin grup boyutunu (batch size) birinciyle eşleşecek şekilde otomatik olarak ayarlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler1` | LATENT | Evet | - | Birleştirilecek ilk gizli örnek |
| `örnekler2` | LATENT | Evet | - | Birleştirilecek ikinci gizli örnek |
| `boyut` | COMBO | Evet | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | Gizli örneklerin birleştirileceği boyut. Pozitif değerler (x, y, t) sonuçta samples1'i samples2'den önce yerleştirir. Negatif değerler (-x, -y, -t) samples2'yi samples1'den önce yerleştirir. Boyut eşlemesi şu şekildedir: x = genişlik, y = yükseklik, t = zaman/karesayısı |

**Not:** İkinci gizli örnek (`samples2`), birleştirme işleminden önce birinci gizli örneğin (`samples1`) grup boyutuyla eşleşecek şekilde otomatik olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | İki girdi örneğinin belirtilen boyut boyunca birleştirilmesiyle elde edilen birleştirilmiş gizli örnekler |

---
**Source fingerprint (SHA-256):** `46514ef85887279ec577ad88ac46f1c20f428903ee63b076888d7d5df09fde77`
