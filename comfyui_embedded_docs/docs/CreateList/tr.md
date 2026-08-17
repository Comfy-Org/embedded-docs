# Liste Oluştur

Create List düğümü, birden çok girdiyi tek ve sıralı bir listede birleştirir. Aynı veri türünde herhangi bir sayıda girdi alır ve bunları bağlanma sırasına göre art arda ekler. Bu düğüm; görüntüler veya metinler gibi veri gruplarını, iş akışındaki diğer düğümler tarafından işlenmek üzere hazırlamak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `inputs` | Büyütülebilir bir girdi slotları kümesi. Artı (+) simgesine tıklayarak daha fazla slot ekleyin veya öğeleri bağlayın; yeni slotlar otomatik olarak oluşturulur. Her slot bir veya daha fazla öğe kabul eder ve tüm slotlar aynı veri türünü paylaşmalıdır (örneğin, tümü IMAGE veya tümü STRING). | Değişir (bağlanan veri türüyle eşleşir) | Evet | Herhangi bir sayıda slot; her slot bir veya daha fazla öğe kabul eder |

**Not:** Düğüm, öğeleri bağladıkça otomatik olarak yeni girdi slotları oluşturur. Düğümün doğru çalışması için bağlanan tüm girdiler aynı veri türünü paylaşmalıdır ve çıktı listesi de aynı türü alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `list` | Bağlı girdi slotlarındaki tüm öğeleri, slotların bağlanma sırasına göre art arda eklenmiş şekilde içeren tek bir listedir. Çıktı veri türü, girdi veri türüyle eşleşir. | Değişir (girdi veri türüyle eşleşir) |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/tr.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
