# Gürültü Ekle

Bu düğüm, belirtilen bir gürültü üreteci ve sigma değerlerini kullanarak latent bir görüntüye kontrollü gürültü ekler. Verilen sigma aralığına uygun gürültü ölçeklemesi uygulamak için girdiyi modelin örnekleme sistemi üzerinden işler ve gürültü eklenmiş yeni bir latent temsil döndürür. Bu düğüm şu anda deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerini ve işleme fonksiyonlarını içeren model | MODEL | Evet | - |
| `gürültü` | Temel gürültü desenini üreten gürültü üreteci | NOISE | Evet | - |
| `sigmalar` | Gürültü ölçekleme yoğunluğunu kontrol eden sigma değerleri. Boşsa, düğüm orijinal latent görüntüyü değiştirilmeden döndürür. Birden fazla sigma sağlandığında, gürültü ölçeği ilk ve son sigma değerleri arasındaki mutlak fark olarak hesaplanır. Yalnızca bir sigma sağlandığında, bu değer doğrudan ölçek olarak kullanılır. | SIGMAS | Evet | - |
| `gizli_görüntü` | Gürültü eklenecek girdi latent temsili. Yalnızca sıfırlardan oluşan boş latent görüntüler işleme sırasında kaydırılmaz. | LATENT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Gürültü eklenmiş değiştirilmiş latent temsil. Çıktıdaki NaN veya sonsuz değerler, kararlılık için sıfıra dönüştürülür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/tr.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
