# Ideogram 4 Zamanlayıcı

Ideogram 4 Scheduler düğümü, Ideogram 4 referans zamanlamasına dayalı olarak difüzyon örnekleme süreci için bir dizi sigma değeri (gürültü seviyesi) üretir. Görüntü boyutlarına uyum sağlayan ve istatistiksel parametreler aracılığıyla ince ayar yapılmasına olanak tanıyan özel bir gürültü zamanlaması oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `adımlar` | Zamanlamanın oluşturulacağı örnekleme adımı sayısı (varsayılan: 20). Çıktı, `steps + 1` adet sigma değeri içerir. | INT | Evet | 1 ila 200 |
| `genişlik` | Görüntünün piksel cinsinden genişliği (varsayılan: 1024). 512×512 referansa göre çözünürlük, gürültü zamanlamasını kaydırır. | INT | Evet | 256 ila 8192 (adım: 16) |
| `yükseklik` | Görüntünün piksel cinsinden yüksekliği (varsayılan: 1024). 512×512 referansa göre çözünürlük, gürültü zamanlamasını kaydırır. | INT | Evet | 256 ila 8192 (adım: 16) |
| `mu` | Logit-normal dağılımı için ortalama parametresi; merkezi gürültü seviyesini kontrol eder. logSNR kaymasını oluşturmak için çözünürlük terimiyle birleştirilir (varsayılan: 0.0). | FLOAT | Evet | -10.0 ila 10.0 (adım: 0.05) |
| `std` | Logit-normal dağılımı için standart sapma parametresi; gürültü seviyelerinin dağılımını kontrol eder (varsayılan: 1.75). | FLOAT | Evet | 0.1 ila 5.0 (adım: 0.05) |

Not: Zamanlama, referans zamanı üzerinden logit-normal bir dağılımdan türetilir. `0.5 * log((width × height) / (512 × 512))` değerine eşit bir çözünürlük terimi `mu` değerine eklenir; böylece aynı `mu` değerinde daha büyük veya daha küçük görüntüler, 512×512 referansa göre zamanlamayı kaydırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SIGMAS` | Gürültü zamanlamasını temsil eden sigma değerlerinden oluşan bir tensör; uzunluğu `steps + 1` değerine eşittir. Değerler yüksek gürültüden düşük gürültüye doğru azalır; tam gürültü giderme için son değer 0.0 olarak ayarlanır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/tr.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
