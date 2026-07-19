# BatchImagesMasksLatentsNode

Topluluk İmaj/Maske/Latent düğümü, aynı türdeki birden çok girdiyi tek bir toplu işlemde birleştirir. Girdilerin imaj, maske veya latent temsil olup olmadığını otomatik olarak algılar ve uygun toplu işleme yöntemini kullanır. Bu, toplu girdi kabul eden düğümler tarafından işlenmek üzere birden çok öğeyi hazırlamak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `inputs` | Bir toplu işlemde birleştirilecek dinamik girdi listesi. 1 ile 50 arasında öğe ekleyebilirsiniz. Tüm öğeler aynı türde olmalıdır (tümü imaj, tümü maske veya tümü latent). | IMAGE, MASK veya LATENT | Evet | 1 ila 50 girdi |

**Not:** Düğüm, veri türünü (IMAGE, MASK veya LATENT) `inputs` listesindeki ilk öğeye göre otomatik olarak belirler. Sonraki tüm öğeler bu türle eşleşmelidir. Farklı veri türlerini karıştırmaya çalışırsanız düğüm başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tek bir toplu çıktı. Veri türü, girdi türüyle eşleşir (toplu IMAGE, toplu MASK veya toplu LATENT). | IMAGE, MASK veya LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/tr.md)

---
**Source fingerprint (SHA-256):** `6f3037bc00fd8526f42ad2d79a0f27434f58bd6dd0338a585cc707a771ac0989`
