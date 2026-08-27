# Liste Oluştur

Create List düğümü, birden fazla girdiyi tek bir sıralı listede birleştirir. Aynı veri türünde herhangi bir sayıda girdi alır ve bunları bağlandıkları sırayla birleştirir. Bu düğüm, bir iş akışındaki diğer düğümler tarafından işlenmek üzere görüntü veya metin gibi veri grupları hazırlamak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `girdiler` | `input`, `input_2`, `input_3` vb. olarak adlandırılan değişken sayıda girdi yuvası. Her yuva, aynı veri türünde öğelerden oluşan bir liste kabul eder. Artı (+) simgesine tıklayarak daha fazla yuva ekleyebilirsiniz. Tüm yuvalar aynı veri türünü kullanmalıdır (örn. tümü IMAGE veya tümü STRING). | Değişken | Evet | Herhangi bir sayıda yuva; her yuva herhangi bir sayıda öğe kabul eder |

**Not:** Düğüm, öğeleri bağladıkça otomatik olarak yeni girdi yuvaları oluşturur. Düğümün doğru çalışması için bağlı tüm girdilerin aynı veri türünü paylaşması gerekir. Bağlı her yuva bir öğe listesi sağlar ve düğüm listeleri yuva sırasına göre birleştirir (`input`, ardından `input_2`, ardından `input_3`, ...). Düğüm ayrıca "Image Iterator", "Text Iterator" ve "Iterator" takma adları altında aranabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `liste` | Bağlı girdilerdeki tüm öğeleri, sağlandıkları sırayla birleştirilmiş olarak içeren tek bir liste. Çıktı veri türü, girdi veri türüyle eşleşir. | Değişken |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/tr.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
