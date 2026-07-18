Switch düğümü, bir boolean koşuluna bağlı olarak iki olası girdi arasında seçim yapar. `switch` etkinleştirildiğinde `on_true` girdisini, devre dışı bırakıldığında ise `on_false` girdisini çıktı olarak verir. Bu sayede iş akışınızda koşullu mantık oluşturabilir ve farklı veri yollarını seçebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `anahtar` | Hangi girdinin iletileceğini belirleyen boolean koşul. Etkinleştirildiğinde (true), `doğruda` girdisi seçilir. Devre dışı bırakıldığında (false), `yanlışta` girdisi seçilir. | BOOLEAN | Evet |  |
| `yanlışta` | `anahtar` devre dışıyken (false) çıktıya iletilecek veri. Bu girdi yalnızca `anahtar` false olduğunda gereklidir. | MATCH_TYPE | Hayır |  |
| `doğruda` | `anahtar` etkinken (true) çıktıya iletilecek veri. Bu girdi yalnızca `anahtar` true olduğunda gereklidir. | MATCH_TYPE | Hayır |  |

**Girdi Gereksinimleri Notu:** `on_false` ve `on_true` girdileri koşullu olarak zorunludur. Düğüm, `switch` yalnızca true olduğunda `on_true` girdisini, false olduğunda ise yalnızca `on_false` girdisini talep eder. Her iki girdi de aynı veri türünde olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `çıktı` | Seçilen veri. `anahtar` true ise `doğruda` girdisinden, false ise `yanlışta` girdisinden gelen değer olacaktır. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
