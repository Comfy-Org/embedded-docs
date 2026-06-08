GITSScheduler düğümü, GITS (Generative Iterative Time Steps - Üretken Yinelemeli Zaman Adımları) örnekleme yöntemi için gürültü planı sigma değerleri üretir. Bir katsayı parametresi ve adım sayısına bağlı olarak sigma değerlerini hesaplar; ayrıca toplam kullanılan adım sayısını azaltabilen isteğe bağlı bir gürültü giderme faktörü içerir. Düğüm, nihai sigma planını oluşturmak için önceden tanımlanmış gürültü seviyeleri ve enterpolasyon kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `katsayı` | Gürültü planı eğrisini kontrol eden katsayı değeri (varsayılan: 1.20) | FLOAT | Evet | 0.80 - 1.50 |
| `adımlar` | Sigma değerlerinin üretileceği toplam örnekleme adım sayısı (varsayılan: 10) | INT | Evet | 2 - 1000 |
| `gürültü_azaltma` | Kullanılan adım sayısını azaltan gürültü giderme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** `denoise` değeri 0.0 olarak ayarlandığında, düğüm boş bir tensör döndürür. `denoise` değeri 1.0'dan küçük olduğunda, kullanılan gerçek adım sayısı `round(steps * denoise)` olarak hesaplanır. Adım sayısı 20'den büyük olduğunda, düğüm, önceden tanımlanmış gürültü seviyelerini istenen adım sayısına genişletmek için log-doğrusal enterpolasyon kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Gürültü planı için oluşturulan sigma değerleri | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `b81b85f95236276822429ec7cbc90204c6f4f86ea3e89ed8b7c2aea40597fea9`
