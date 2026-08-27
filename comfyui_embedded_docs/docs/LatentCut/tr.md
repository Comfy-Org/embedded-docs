# Gizli Kesme

LatentCut düğümü, seçilen bir boyut boyunca latent örneklerden belirli bir bölümü çıkarır. Boyutu (x, y veya t), başlangıç konumunu ve çıkarılacak miktarı belirterek latent temsilin bir kısmını kesmenize olanak tanır. Düğüm, hem pozitif hem de negatif indekslemeyi destekler ve çıkarma miktarını mevcut sınırlar içinde kalacak şekilde otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Çıkarma yapılacak girdi latent örnekleri | LATENT | Evet | - |
| `boyut` | Latent örneklerin kesileceği boyut. "x" son eksen boyunca (genellikle genişlik), "y" sondan ikinci eksen boyunca (genellikle yükseklik) ve "t" sondan üçüncü eksen boyunca (genellikle video latentlerinde kareler) keser | COMBO | Evet | "x"<br>"y"<br>"t" |
| `dizin` | Kesme için başlangıç konumu (varsayılan: 0). Pozitif değerler baştan, negatif değerler sondan sayılır. Düğüm, dizini latent örneklerin geçerli aralığında kalacak şekilde otomatik olarak sınırlar | INT | Evet | -16384 ile 16384 |
| `miktar` | Belirtilen boyut boyunca çıkarılacak öğe sayısı (varsayılan: 1). Düğüm, bu değer başlangıç dizininden sonraki mevcut veriyi aşarsa otomatik olarak azaltır | INT | Evet | 1 ile 16384 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Latent örneklerin çıkarılan bölümü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/tr.md)

---
**Source fingerprint (SHA-256):** `7682de2644a4b85dba0571406f9f9802eca7caab09dc2ccf1ac91dc13b41bcdf`
