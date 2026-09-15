# Liste Oluştur

Create List düğümü, birden çok girdiyi tek bir sıralı listede birleştirir. Aynı veri türünü paylaşan herhangi sayıda girdi yuvasını kabul eder ve öğelerini yuvaların bağlanma sırasına göre birleştirir. Sonuç, bağlı tüm öğeleri içeren tek bir listedir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `girdiler` | `input`, `input_2`, `input_3` vb. adlarla değişken sayıda girdi yuvası. Her yuva, aynı veri türünde öğelerden oluşan bir liste kabul eder (örneğin hepsi IMAGE veya hepsi STRING). Yeni yuvalar gerektiğinde otomatik olarak oluşturulur. Düğüm, listeleri yuva sırasına göre birleştirir. | Any | Evet | Herhangi sayıda yuva; her yuva herhangi sayıda öğe kabul eder |

**Not:** Bağlanan tüm girdiler aynı veri türünü paylaşmalıdır. Bağlanan her yuva bir öğe listesi sağlar ve düğüm listeleri yuva sırasına göre birleştirir (`input`, ardından `input_2`, ardından `input_3`, ...). Düğüm ayrıca "Image Iterator", "Text Iterator" ve "Iterator" takma adlarıyla aranabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `list` | Bağlanan girdilerdeki tüm öğeleri, yuvaların sağlanma sırasına göre birleştirilmiş halde içeren tek bir liste. Çıktı veri türü, girdi veri türüyle eşleşir. | Any |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/tr.md)

---
**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`
