# Toplu Maskeler

Batch Masks düğümü, birden çok bağımsız maske girdisini tek bir toplu maske (batch) halinde birleştirir. Değişken sayıda maske girdisi alır ve bunları sonraki düğümlerde maskelerin toplu işlenmesine olanak tanıyan tek bir toplu maske tensörü olarak verir. Girdi maskeleri farklı boyutlardaysa, ilk maskenin boyutlarıyla eşleşecek şekilde otomatik olarak yeniden boyutlandırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `mask` | Bir toplu maske halinde birleştirilecek maske girdileri. En az bir maske gereklidir. Düğümdeki "+" düğmesine tıklayarak toplamda 50 maskeye kadar ekleyebilirsiniz. Maskeler farklı boyutlardaysa, ilk maskenin boyutlarıyla eşleşecek şekilde otomatik olarak yeniden boyutlandırılır. | MASK | Evet | 1 - 50 maske |

**Not:** Bu düğüm bir otomatik büyüyen girdi şablonu kullanır. En az bir maske bağlamalısınız. Toplamda 50 maske olacak şekilde 49 maske girdisi daha ekleyebilirsiniz. Bağlanan tüm maskeler tek bir toplu maske halinde birleştirilir. Maskeler farklı yükseklik veya genişliklere sahipse, ilk maskenin boyutlarıyla eşleşecek şekilde bilinear enterpolasyon kullanılarak otomatik olarak yeniden boyutlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Girdi maskelerinin tümünü bir arada içeren tek bir toplu maske. Hiçbir maske sağlanmazsa None döndürür. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/tr.md)

---
**Source fingerprint (SHA-256):** `7e9bc4be72c7fa8fceab2cf167c72b7e1ff858c0281d977f2ad3ab433d9d58d6`
