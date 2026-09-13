# Gizli Kesme

LatentCut düğümü, seçilen bir boyut boyunca latent örneklerinden belirli bir bölümü çıkarır. Boyutu (x, y veya t), başlangıç konumunu ve ne kadar çıkarılacağını belirterek latent temsilinin bir kısmını keser. Düğüm hem pozitif hem de negatif indekslemeyi destekler ve çıkarma miktarını kullanılabilir sınırlar içinde kalacak şekilde otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | Çıkarılacak giriş latent örnekleri | LATENT | Evet | - |
| `dim` | Latent örneklerinin kesileceği boyut. "x" son eksen boyunca (tipik olarak genişlik), "y" sondan ikinci eksen boyunca (tipik olarak yükseklik) ve "t" sondan üçüncü eksen boyunca (video latentlerinde tipik olarak kareler) keser | COMBO | Evet | "x"<br>"y"<br>"t" |
| `index` | Kesme için başlangıç konumu (varsayılan: 0). Pozitif değerler başlangıçtan, negatif değerler sondan sayılır. Düğüm, indeksi latent örneklerinin geçerli aralığı içinde kalacak şekilde sınırlar | INT | Evet | -16384 ile 16384 |
| `amount` | Belirtilen boyut boyunca çıkarılacak öğe sayısı (varsayılan: 1). En az 1 olmalıdır. Başlangıç indeksinin ötesinde mevcut veriyi aşacaksa düğüm bu değeri otomatik olarak azaltır | INT | Evet | 1 ile 16384 |

Not: `index` ve `amount` değerleri, seçilen boyut boyunca latentin gerçek boyutuna uyacak şekilde ayarlanır. `index`, boyut büyüklüğünden büyükse son geçerli konuma sabitlenir. `index` negatifse, mutlak değer açısından boyut büyüklüğüne sabitlenir ve `amount`, verinin sonunu geçmeyecek şekilde sınırlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Latent örneklerinin çıkarılan kısmı | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/tr.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
