> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/tr.md)

GITSScheduler düğümü, GITS (Generative Iterative Time Steps - Üretken Yinelemeli Zaman Adımları) örnekleme yöntemi için gürültü planı sigma değerlerini oluşturur. Bir katsayı parametresi ve adım sayısına dayalı olarak sigma değerlerini hesaplar ve kullanılan toplam adım sayısını azaltabilen isteğe bağlı bir gürültü giderme faktörü içerir. Düğüm, önceden tanımlanmış gürültü seviyelerini ve enterpolasyonu kullanarak nihai sigma planını oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `coeff` | FLOAT | Evet | 0.80 - 1.50 | Gürültü planı eğrisini kontrol eden katsayı değeri (varsayılan: 1.20) |
| `steps` | INT | Evet | 2 - 1000 | Sigma değerlerinin oluşturulacağı toplam örnekleme adım sayısı (varsayılan: 10) |
| `denoise` | FLOAT | Evet | 0.0 - 1.0 | Kullanılan adım sayısını azaltan gürültü giderme faktörü (varsayılan: 1.0) |

**Not:** `denoise` 0.0 olarak ayarlandığında, düğüm boş bir tensör döndürür. `denoise` 1.0'dan küçük olduğunda, kullanılan gerçek adım sayısı `round(steps * denoise)` olarak hesaplanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Gürültü planı için oluşturulan sigma değerleri |