# Model Cihazı Seç

Select Model Device düğümü, bir difüzyon modelinin hangi cihazda (CPU veya belirli bir GPU) çalışacağını manuel olarak seçmenizi sağlar. Bir modeli farklı bir cihaza taşıyabilir ve diğer çoklu GPU düğümleriyle olan çakışmaları otomatik olarak yönetir. `"default"` seçildiğinde, model yükleyici tarafından seçilen özgün cihaz geri yüklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Belirli bir cihaza yerleştirilecek difüzyon modeli. | MODEL | Evet |  |
| `device` | Model için hedef cihaz. Seçenekler, geçerli makinede kullanılabilir cihazlara göre dinamik olarak oluşturulur. (varsayılan: `"default"`) | COMBO | Evet | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (algılanan her GPU için bir `"gpu:N"` girdisi) |

**Parametre Ayrıntıları:**
- `"default"`: Daha önce bir Select Model Device çağrısı yapılmış olsa bile, model yükleyici tarafından atanan yükleme ve boşaltma cihazlarını geri yükler.
- `"cpu"`: Hem yükleme hem de boşaltma cihazını CPU'ya sabitler.
- `"gpu:N"`: Yükleme cihazını mevcut N. GPU'ya sabitler (örneğin, ilk GPU için `"gpu:0"`). Boşaltma cihazı, yükleyicinin özgün seçimine geri yüklenir.

**Önemli Notlar:**
- İstenen cihaz geçerli makinede yoksa (örneğin, 2 GPU'lu bir makinede oluşturulan bir iş akışı 1 GPU'lu bir makinede açılırsa), düğüm modeli değiştirmeden geçirir ve başarısız olmak yerine bir ileti günlüğe kaydeder. Taşınabilir iş akışlarının erkenden hata vermemesi için girdi doğrulaması sırasında bilinmeyen `gpu:N` değerlerine izin verilir.
- Model zaten istenen cihazdaysa, düğüm hızlı bir yol kullanır ve modeli yeniden yüklemez.
- İstenen cihaz, girdi modelinin zaten bulunduğu cihazdan farklı olduğunda, yeni patcher'ın yeni cihazda bağımsız ağırlıklara sahip olması için yükleyicinin yeniden yükleme fabrikası kullanılarak yeni bir model oluşturulur.
- Model yükleyici çoklu GPU'yu desteklemiyorsa (yeniden yükleme fabrikası yoksa), düğüm modeli değiştirmeden geçirir ve bir uyarı günlüğe kaydeder.
- Bir MultiGPU CFG Split klonu seçilen cihazı zaten kaplıyorsa, iki modelin aynı cihaza bağlanmaması için o klon budanır.
- Varsayılan olmayan bir cihaz (CPU veya GPU) seçildiğinde, düğüm ayrıca modelin hesaplama dtype'ını o cihaz tarafından desteklenen bir dtype'a ayarlar.
- Bu düğümün, modeli zaten tüketmiş bir düğümden (örneğin, bir KSampler) sonra yerleştirilmesi önerilmez, çünkü cihaz özgün cihazla eşleşirse önceki düğüm tarafından değiştirilen herhangi bir durum gözlemlenecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Seçilen cihaza yerleştirilmiş difüzyon modeli. Cihaz geçersiz veya kullanılamaz durumdaysa, model değiştirilmeden geçirilir. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/tr.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
