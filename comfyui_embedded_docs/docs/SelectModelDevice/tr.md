# Model Cihazı Seç

## Genel Bakış

SelectModelDevice düğümü, bir difüzyon modelinin hangi aygıtta (CPU veya belirli bir GPU) çalışacağını elle seçmenizi sağlar. Modeli farklı bir aygıta taşıyabilir ve diğer çoklu GPU düğümleriyle çakışmaları otomatik olarak yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Belirli bir aygıta yerleştirilecek difüzyon modeli. | MODEL | Evet |  |
| `device` | Model için hedef aygıt. Seçenekler, kullanılabilir GPU'lara göre dinamik olarak oluşturulur. (varsayılan: "default") | COMBO | Evet | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (algılanan her GPU için bir `"gpu:N"` girişi) |

**Parametre Ayrıntıları:**
- `"default"`: Önceki bir SelectModelDevice düğümü değiştirmiş olsa bile, model yükleyicinin atadığı aygıtı geri yükler.
- `"cpu"`: Hem yükleme hem boşaltma aygıtını CPU'ya sabitler.
- `"gpu:N"`: Yükleme aygıtını N. kullanılabilir GPU'ya sabitler (ör. ilk GPU için `"gpu:0"`). Boşaltma aygıtı, yükleyicinin orijinal seçimine geri yüklenir.

**Önemli Notlar:**
- İstenen aygıt mevcut makinede yoksa (ör. 2 GPU'lu bir makinede oluşturulan bir iş akışı 1 GPU'lu bir makinede açılırsa), düğüm hataya düşmek yerine modeli değiştirmeden iletir ve bir mesaj günlüğe kaydeder.
- Model zaten istenen aygıttaysa, düğüm hızlı yolu kullanır ve modeli yeniden yüklemez.
- Model yükleyici çoklu GPU'yu desteklemiyorsa (yeniden yükleme fabrikası yoksa), düğüm modeli değiştirmeden iletir ve bir uyarı kaydeder.
- Bir MultiGPU CFG Split kopyası seçilen aygıtı zaten kaplıyorsa, iki model aynı aygıta bağlanmasın diye bu kopya budanır.
- Belirli bir aygıt seçildiğinde, düğüm ayrıca modelin hesaplama dtype'ını o aygıt tarafından desteklenen bir türe ayarlar.
- Bu düğümü, modeli zaten tüketen bir düğümden (ör. bir KSampler) *sonra* yerleştirmek önerilmez; aygıt orijinalle eşleşiyorsa, önceki düğümün değiştirdiği durum gözlemlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Seçilen aygıta yerleştirilmiş difüzyon modeli. Aygıt geçersiz veya kullanılamıyorsa, model değiştirilmeden iletilir. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/tr.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
