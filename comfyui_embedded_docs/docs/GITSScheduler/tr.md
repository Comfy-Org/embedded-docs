# GITSZamanlayıcı

GITSScheduler düğümü, GITS örnekleme yöntemi tarafından kullanılan sigma (gürültü seviyesi) planını üretir. `coeff` parametresine ve `steps` sayısına göre önceden tanımlanmış bir gürültü seviyesi tablosu seçer; `denoise` değeri 1.0'ın altında kullanıldığında planı isteğe bağlı olarak kısaltır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `coeff` | Planı oluşturmak için hangi önceden tanımlanmış gürültü seviyesi tablosunun seçileceğini belirleyen katsayı. Değer 2 ondalık basamağa yuvarlanır (varsayılan: 1.20) | FLOAT | Evet | 0.80 - 1.50 |
| `steps` | Sigma değerlerinin üretileceği toplam örnekleme adımı sayısı (varsayılan: 10) | INT | Evet | 2 - 1000 |
| `denoise` | Kullanılan adım sayısını azaltan gürültü giderme faktörü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** `denoise` 0.0 olarak ayarlandığında düğüm boş bir tensör döndürür. `denoise` 1.0'dan küçük olduğunda, kullanılan gerçek adım sayısı `round(steps * denoise)` olarak hesaplanır. 20 adıma kadar düğüm önceden tanımlanmış gürültü seviyelerini doğrudan kullanır; 20 adımdan fazla olduğunda, önceden tanımlanmış gürültü seviyelerini istenen adım sayısına genişletmek için log-doğrusal enterpolasyon kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `sigmas` | Gürültü planı için üretilen sigma değerleri | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/tr.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
