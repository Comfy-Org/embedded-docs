# GITSZamanlayıcı

GITSScheduler düğümü, GITS (Generative Iterative Time Steps) örnekleme yöntemi için gürültü planı sigma değerlerini üretir. Sigma değerlerini bir katsayı parametresi ve adım sayısına göre hesaplar; toplam kullanılan adımları azaltabilen isteğe bağlı bir arındırma (denoise) faktörü içerir. Düğüm, son sigma planını oluşturmak için önceden tanımlanmış gürültü seviyelerini ve enterpolasyonu kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `katsayı` | Gürültü planı eğrisini kontrol eden katsayı değeri (varsayılan: 1.20). Değer iki ondalık basamağa yuvarlanır ve hangi önceden tanımlanmış gürültü seviyesi tablosunun kullanılacağını seçer. | FLOAT | Evet | 0.80 - 1.50 (adım 0.05) |
| `adımlar` | Sigma değerlerinin üretileceği toplam örnekleme adımı sayısı (varsayılan: 10) | INT | Evet | 2 - 1000 |
| `gürültü_azaltma` | Kullanılan adım sayısını azaltan arındırma faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** `denoise` değeri 0.0 veya daha küçük olduğunda, düğüm boş bir tensör döndürür. `denoise` değeri 1.0'dan küçük olduğunda, gerçek kullanılan adım sayısı `round(steps * denoise)` olarak hesaplanır ve planın yalnızca son kısmı korunur. Adım sayısı 2 ile 20 arasında olduğunda, düğüm eşleşen önceden tanımlanmış bir gürültü planı seçer. Adım sayısı 20'den büyük olduğunda, düğüm önceden tanımlanmış gürültü seviyelerini istenen adım sayısına genişletmek için log-doğrusal enterpolasyon kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `sigmas` | Gürültü planı için üretilen sigma değerleri. N adım için N+1 sigma değeri döndürülür ve son sigma 0 olarak ayarlanır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
