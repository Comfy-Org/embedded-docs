# Ideogram 4 Zamanlayıcı

Ideogram 4 Zamanlayıcı düğümü, Ideogram 4 referans programına dayalı olarak difüzyon örnekleme süreci için bir sigma değerleri dizisi (gürültü seviyeleri) üretir. Görüntü boyutlarına uyum sağlayan ve istatistiksel parametreler aracılığıyla ince ayar yapılmasına olanak tanıyan özel bir gürültü programı oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `steps` | Programın oluşturulacağı örnekleme adım sayısı (varsayılan: 20) | INT | Evet | 1 to 200 |
| `width` | Görüntünün piksel cinsinden genişliği (varsayılan: 1024) | INT | Evet | 256 to 8192 (step: 16) |
| `height` | Görüntünün piksel cinsinden yüksekliği (varsayılan: 1024) | INT | Evet | 256 to 8192 (step: 16) |
| `mu` | Logit-normal dağılım için ortalama parametresi; merkezi gürültü seviyesini kontrol eder (varsayılan: 0.0) | FLOAT | Evet | -10.0 to 10.0 (step: 0.05) |
| `std` | Logit-normal dağılım için standart sapma parametresi; gürültü seviyelerinin yayılımını kontrol eder (varsayılan: 1.75) | FLOAT | Evet | 0.1 to 5.0 (step: 0.05) |

Not: Programın etkin merkezi kayması, `mu` ile 512×512 referansına göre görüntü alanına dayalı bir çözünürlük teriminin birleşimiyle belirlenir. Bu nedenle daha büyük görüntü alanları, gürültü programını daha küçük alanlara kıyasla kaydırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SIGMAS` | Gürültü programını temsil eden, uzunluğu `steps + 1` değerine eşit bir sigma değerleri tensörü. Değerler yüksek gürültüden düşük gürültüye doğru azalır ve tam gürültü giderme işlemi için son değer 0.0 olarak ayarlanır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/tr.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
