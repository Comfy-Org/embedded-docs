> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/tr.md)

OptimalStepsScheduler düğümü, seçilen model türüne ve adım yapılandırmasına dayanarak yayılım modelleri için gürültü programı sigma değerlerini hesaplar. Toplam adım sayısını gürültü giderme parametresine göre ayarlar ve istenen adım sayısına uyacak şekilde gürültü seviyelerini enterpole eder. Düğüm, yayılım örnekleme sürecinde kullanılan gürültü seviyelerini belirleyen bir sigma değerleri dizisi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_türü` | COMBO | Evet | "FLUX"<br>"Wan"<br>"Chroma" | Gürültü seviyesi hesaplaması için kullanılacak yayılım modelinin türü |
| `adımlar` | INT | Evet | 3-1000 | Hesaplanacak toplam örnekleme adımı sayısı (varsayılan: 20) |
| `gürültü_azaltma` | FLOAT | Hayır | 0.0-1.0 | Etkili adım sayısını ayarlayan gürültü giderme gücünü kontrol eder (varsayılan: 1.0) |

**Not:** `denoise` değeri 1.0'dan küçük olarak ayarlandığında, düğüm etkili adımları `steps * denoise` olarak hesaplar. Eğer `denoise` 0.0 olarak ayarlanırsa, düğüm boş bir tensör döndürür.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Yayılım örneklemesi için gürültü programını temsil eden bir sigma değerleri dizisi |