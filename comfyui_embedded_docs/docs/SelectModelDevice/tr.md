# Model Cihazı Seç

SelectModelDevice düğümü, bir difüzyon modelinin hangi cihazda (CPU veya belirli bir GPU) çalışacağını seçmenizi sağlar. Seçilen seçeneğe bağlı olarak, yükleyicinin orijinal cihazını geri yükler, modeli CPU'ya sabitler veya belirli bir GPU'ya taşır ve diğer çoklu GPU düğümleriyle çakışmaları otomatik olarak yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Belirli bir cihaza yerleştirilecek difüzyon modeli. | MODEL | Evet |  |
| `device` | Modelin hedef cihazı. Seçenekler, kullanılabilir GPU'lara göre dinamik olarak oluşturulur. (varsayılan: "default") | COMBO | Evet | `"default"`<br>`"cpu"`<br>`"gpu:N"` (her kullanılabilir GPU için; örn. `"gpu:0"`, `"gpu:1"`, ...) |

**Parametre Ayrıntıları:**
- `"default"`: Model yükleyicinin atadığı cihazı, önceki bir SelectModelDevice düğümü değiştirmiş olsa bile geri yükler.
- `"cpu"`: Hem yükleme hem de boşaltma (offload) cihazını CPU'ya sabitler.
- `"gpu:N"`: Yükleme cihazını N. kullanılabilir GPU'ya sabitler (örn. ilk GPU için `"gpu:0"`). Boşaltma (offload) cihazı, yükleyicinin orijinal tercihine geri yüklenir.

**Önemli Notlar:**
- Bilinmeyen `"gpu:N"` değerleri doğrulama sırasında kabul edilir; böylece taşınabilir iş akışları daha az GPU'ya sahip makinelerde başarısız olmaz. Çalışma zamanında, kullanılamayan bir cihaz modelin değiştirilmeden geçirilmesine ve bir günlük mesajı kaydedilmesine neden olur.
- İstenen cihaz mevcut makinede yoksa (ör. 2 GPU'lu bir makinede oluşturulan bir iş akışı 1 GPU'lu bir makinede açılırsa), düğüm başarısız olmak yerine modeli değiştirmeden geçirir ve bir mesajı günlüğe kaydeder.
- Model zaten istenen cihazdaysa, düğüm hızlı yolu kullanır ve modeli yeniden yüklemez.
- İstenen cihaz mevcut cihazdan farklıysa, yükleyicinin yeniden yükleme fabrikası kullanılarak yeni bir model oluşturulur; böylece döndürülen model yeni cihazda bağımsız ağırlıklara sahip olur. Bunu desteklemeyen yükleyiciler, düğümün modeli bir uyarıyla değiştirmeden geçirmesine neden olur.
- İş akışında zaten MultiGPU CFG Split uygulanmışsa ve seçilen GPU mevcut çoklu GPU klonlarından biriyle eşleşiyorsa, bu klon kaldırılır; böylece iki yama uygulayıcı (patcher) aynı cihaza bağlanmış olmaz.
- Bu düğümün, modeli zaten tüketmiş bir düğümden (örn. bir KSampler) *sonra* yerleştirilmesi önerilmez; çünkü cihaz orijinal cihazla eşleşirse, önceki düğümün değiştirdiği herhangi bir durum gözlemlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Difüzyon modeli, artık seçilen cihaza yerleştirilmiştir. Cihaz geçersiz veya kullanılamıyorsa, model değiştirilmeden geçirilir. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/tr.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
