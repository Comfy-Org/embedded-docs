> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/tr.md)

Bu düğüm, belirtilen bir gürültü üreteci ve sigma değerlerini kullanarak gizli bir görüntüye kontrollü gürültü ekler. Girişi, modelin örnekleme sistemi aracılığıyla işleyerek verilen sigma aralığına uygun gürültü ölçeklendirmesi uygular ve gürültünün eklendiği yeni bir gizli temsil döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Örnekleme parametrelerini ve işleme fonksiyonlarını içeren model |
| `gürültü` | NOISE | Evet | - | Temel gürültü desenini üreten gürültü üreteci |
| `sigmalar` | SIGMAS | Evet | - | Gürültü ölçeklendirme yoğunluğunu kontrol eden sigma değerleri. Boşsa, düğüm orijinal gizli görüntüyü değiştirmeden döndürür. Birden fazla sigma sağlandığında, gürültü ölçeği ilk ve son sigma değerleri arasındaki mutlak fark olarak hesaplanır. Yalnızca bir sigma sağlandığında, bu değer doğrudan ölçek olarak kullanılır. |
| `gizli_görüntü` | LATENT | Evet | - | Gürültü eklenecek giriş gizli temsili. Yalnızca sıfırlardan oluşan boş gizli görüntüler işleme sırasında kaydırılmaz. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `LATENT` | LATENT | Gürültü eklenmiş, değiştirilmiş gizli temsil. Çıkıştaki NaN veya sonsuz değerler, kararlılık için sıfıra dönüştürülür. |

---
**Source fingerprint (SHA-256):** `8f387f95aeec2780d27bee5b954ad2c6cd6daa9242a1ea15697455b157bc80d5`
