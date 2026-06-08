Bu düğüm, belirtilen bir gürültü üreteci ve sigma değerlerini kullanarak gizli bir görüntüye kontrollü gürültü ekler. Girişi, modelin örnekleme sistemi aracılığıyla işleyerek verilen sigma aralığına uygun gürültü ölçeklendirmesi uygular ve gürültünün eklendiği yeni bir gizli temsil döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerini ve işleme fonksiyonlarını içeren model | MODEL | Evet | - |
| `gürültü` | Temel gürültü desenini üreten gürültü üreteci | NOISE | Evet | - |
| `sigmalar` | Gürültü ölçeklendirme yoğunluğunu kontrol eden sigma değerleri. Boşsa, düğüm orijinal gizli görüntüyü değiştirmeden döndürür. Birden fazla sigma sağlandığında, gürültü ölçeği ilk ve son sigma değerleri arasındaki mutlak fark olarak hesaplanır. Yalnızca bir sigma sağlandığında, bu değer doğrudan ölçek olarak kullanılır. | SIGMAS | Evet | - |
| `gizli_görüntü` | Gürültü eklenecek giriş gizli temsili. Yalnızca sıfırlardan oluşan boş gizli görüntüler işleme sırasında kaydırılmaz. | LATENT | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Gürültü eklenmiş, değiştirilmiş gizli temsil. Çıkıştaki NaN veya sonsuz değerler, kararlılık için sıfıra dönüştürülür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/tr.md)

---
**Source fingerprint (SHA-256):** `8f387f95aeec2780d27bee5b954ad2c6cd6daa9242a1ea15697455b157bc80d5`
