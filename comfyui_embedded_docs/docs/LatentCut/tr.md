# Gizli Kesme

LatentCut düğümü, seçilen bir boyut boyunca latent örneklerden belirli bir bölüm çıkarır. Boyutu (x, y veya t), başlangıç konumunu ve çıkarılacak miktarı belirterek latent gösterimin bir kısmını kesmenize olanak tanır. Düğüm hem pozitif hem negatif indekslemeyi işler ve çıkarma miktarını mevcut sınırlar içinde kalacak şekilde otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Çıkarım yapılacak giriş latent örnekleri | LATENT | Evet | - |
| `dim` | Latent örneklerin kesileceği boyut | COMBO | Evet | "x"<br>"y"<br>"t" |
| `index` | Kesme için başlangıç konumu (varsayılan: 0). Pozitif değerler baştan, negatif değerler sondan sayılır. Düğüm, indeksi latent örneklerin geçerli aralığında kalacak şekilde otomatik olarak sınırlar. | INT | Evet | -16384 - 16384 |
| `amount` | Belirtilen boyut boyunca çıkarılacak öğe sayısı (varsayılan: 1). Düğüm, bu değer başlangıç indeksinin ötesindeki mevcut veriyi aşarsa otomatik olarak azaltır. | INT | Evet | 1 - 16384 |

Not: `x`, latent tensörün son boyutu boyunca, `y` sondan ikinci boyut boyunca ve `t` sondan üçüncü boyut boyunca keser. `index` pozitif olduğunda seçilen boyutun son geçerli konumuna sınırlanır; negatif olduğunda verinin başlangıcından önceyi göstermeyecek şekilde sınırlanır. İstenen kesim mevcut verinin ötesine uzanacaksa `amount` azaltılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Latent örneklerin çıkarılan bölümü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/tr.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
