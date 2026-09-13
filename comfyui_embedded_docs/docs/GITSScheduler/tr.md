# GITSZamanlayıcı

GITSScheduler düğümü, GITS (Generative Iterative Time Steps) örnekleme yöntemi için gürültü çizelgesi sigma değerlerini üretir. Bir katsayı parametresine ve adım sayısına göre sigma değerlerini hesaplar; kullanılan toplam adım sayısını azaltabilen bir gürültü giderme faktörü içerir. Düğüm, son sigma çizelgesini oluşturmak için önceden tanımlanmış gürültü seviyelerini ve interpolasyonu kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `katsayı` | Gelişmiş parametre. Gürültü çizelgesi eğrisini kontrol eden katsayı değeri (varsayılan: 1.20). Değer iki ondalık basamağa yuvarlanır ve hangi önceden tanımlanmış gürültü seviyesi tablosunun kullanılacağını seçer. | FLOAT | Evet | 0.80 - 1.50 (adım 0.05) |
| `adımlar` | Sigma değerlerinin üretileceği toplam örnekleme adımı sayısı (varsayılan: 10). | INT | Evet | 2 - 1000 |
| `gürültü_azaltma` | Kullanılan adım sayısını azaltan gürültü giderme faktörü (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |

**Not:** `denoise` 0.0 veya daha az olduğunda, düğüm boş bir tensör döndürür. `denoise` 1.0'den küçük olduğunda, kullanılan gerçek adım sayısı `round(steps * denoise)` olarak hesaplanır ve çizelgenin yalnızca buna karşılık gelen son kısmı korunur. 2 ile 20 arasındaki adımlar için düğüm, eşleşen önceden tanımlanmış bir gürültü çizelgesi seçer. 20'den büyük adımlar için düğüm, önceden tanımlanmış gürültü seviyelerini istenen adım sayısına genişletmek üzere log-doğrusal interpolasyon kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `sigmas` | Gürültü çizelgesi için üretilen sigma değerleri. N örnekleme adımı için N+1 sigma değeri döndürülür ve son sigma 0 olarak ayarlanır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
