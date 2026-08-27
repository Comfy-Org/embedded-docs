# Gizli Birleştirme

LatentConcat düğümü, iki latent örneği seçilen bir boyut boyunca birleştirir. İki latent girdi alır ve bunları x, y veya t ekseni boyunca birleştirir; hangi örneğin önce geleceğini kontrol etme seçeneği sunar. Düğüm, birleştirme işlemini gerçekleştirmeden önce ikinci girdinin batch boyutunu birinciyle eşleşecek şekilde otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler1` | Birleştirilecek ilk latent örnek | LATENT | Evet | - |
| `örnekler2` | Birleştirilecek ikinci latent örnek | LATENT | Evet | - |
| `boyut` | Latent örneklerin hangi boyut boyunca birleştirileceğini belirtir. Pozitif değerler (x, y, t) sonuçta samples1'i samples2'den önce yerleştirir. Negatif değerler (-x, -y, -t) samples2'yi samples1'den önce yerleştirir. Boyut eşlemesi şu şekildedir: x = genişlik, y = yükseklik, t = zaman/kare | COMBO | Evet | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**Not:** İkinci latent örnek (`samples2`), birleştirmeden önce birinci latent örneğin (`samples1`) batch boyutuyla eşleşmesi için gerektiğinde otomatik olarak tekrarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `output` | Belirtilen boyut boyunca iki girdi örneğinin birleştirilmesiyle elde edilen birleştirilmiş latent örnekler | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/tr.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
