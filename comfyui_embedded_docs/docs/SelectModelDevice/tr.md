# SelectModelDevice Düğümü

## Genel Bakış

SelectModelDevice düğümü, bir difüzyon modelinin hangi cihazda (CPU veya belirli bir GPU) çalışacağını manuel olarak seçmenizi sağlar. Bir modeli farklı bir cihaza taşıyabilir ve diğer çoklu GPU düğümleriyle oluşan çakışmaları otomatik olarak yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Belirli bir cihaza yerleştirilecek difüzyon modeli. | MODEL | Evet |  |
| `device` | Model için hedef cihaz. Seçenekler, mevcut GPU'lara göre dinamik olarak oluşturulur. (varsayılan: "default") | COMBO | Evet | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

**Parametre Detayları:**
- `"default"`: Daha önceki bir SelectModelDevice düğümü değiştirmiş olsa bile, model yükleyici tarafından atanan cihazı geri yükler.
- `"cpu"`: Hem yükleme hem de boşaltma cihazını CPU'ya sabitler.
- `"gpu:N"`: Yükleme cihazını N. mevcut GPU'ya sabitler (örneğin, ilk GPU için `"gpu:0"`). Boşaltma cihazı, yükleyicinin orijinal seçimine geri döndürülür.

**Önemli Notlar:**
- İstenen cihaz mevcut makinede yoksa (örneğin, 2 GPU'lu bir makinede oluşturulan iş akışı 1 GPU'lu bir makinede açılırsa), düğüm modeli değiştirmeden geçirir ve hata vermek yerine bir mesaj günlüğe kaydeder.
- Model zaten istenen cihazdaysa, düğüm hızlı bir yol izler ve modeli yeniden yüklemez.
- Bu düğümü, modeli zaten tüketmiş bir düğümden (örneğin, bir KSampler) *sonra* yerleştirmek önerilmez, çünkü önceki düğüm tarafından değiştirilen herhangi bir durum, cihaz orijinaliyle eşleşiyorsa gözlemlenecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Seçilen cihaza yerleştirilmiş difüzyon modeli. Cihaz geçersiz veya kullanılamıyorsa, model değiştirilmeden geçirilir. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/tr.md)

---
**Source fingerprint (SHA-256):** `02841975f123cc8ae8152ea86f1798e0e7e68255ecd11e04271da886b75eb0fd`
