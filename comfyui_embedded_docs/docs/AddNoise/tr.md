# Gürültü Ekle

Bu düğüm, belirtilen bir gürültü üreteci ve sigma değerlerini kullanarak latent bir görüntüye kontrollü gürültü ekler. Girişi modelin örnekleme sistemi aracılığıyla işleyerek verilen sigma aralığına uygun gürültü ölçeklemesi uygular ve gürültü eklenmiş yeni bir latent temsil döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerini ve işleme işlevlerini içeren model | MODEL | Evet | - |
| `noise` | Temel gürültü desenini üreten gürültü üreteci | NOISE | Evet | - |
| `sigmas` | Gürültü ölçekleme yoğunluğunu kontrol eden sigma değerleri. Boşsa, düğüm orijinal latent görüntüyü değiştirmeden döndürür. Birden fazla sigma sağlandığında, gürültü ölçeği ilk ve son sigma değerleri arasındaki mutlak fark olarak hesaplanır. Yalnızca bir sigma sağlandığında, bu değer doğrudan ölçek olarak kullanılır. | SIGMAS | Evet | - |
| `latent_image` | Gürültü eklenecek girdi latent temsili. Boş latent görüntüler (yalnızca sıfırlardan oluşan) işleme sırasında kaydırılmaz. | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Gürültü eklenmiş değiştirilmiş latent temsil. Çıktıdaki NaN veya sonsuz değerler kararlılık için sıfıra dönüştürülür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/tr.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
