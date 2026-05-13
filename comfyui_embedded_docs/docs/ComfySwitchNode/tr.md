> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

Switch düğümü, bir boolean koşuluna bağlı olarak iki olası girdi arasında seçim yapar. `switch` etkinleştirildiğinde `on_true` girdisini, devre dışı bırakıldığında ise `on_false` girdisini çıktı olarak verir. Bu sayede iş akışınızda koşullu mantık oluşturabilir ve farklı veri yollarını seçebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `anahtar` | BOOLEAN | Evet | | Hangi girdinin iletileceğini belirleyen boolean koşul. Etkinleştirildiğinde (true), `doğruda` girdisi seçilir. Devre dışı bırakıldığında (false), `yanlışta` girdisi seçilir. |
| `yanlışta` | MATCH_TYPE | Hayır | | `anahtar` devre dışıyken (false) çıktıya iletilecek veri. Bu girdi yalnızca `anahtar` false olduğunda gereklidir. |
| `doğruda` | MATCH_TYPE | Hayır | | `anahtar` etkinken (true) çıktıya iletilecek veri. Bu girdi yalnızca `anahtar` true olduğunda gereklidir. |

**Girdi Gereksinimleri Notu:** `on_false` ve `on_true` girdileri koşullu olarak zorunludur. Düğüm, `switch` yalnızca true olduğunda `on_true` girdisini, false olduğunda ise yalnızca `on_false` girdisini talep eder. Her iki girdi de aynı veri türünde olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | Seçilen veri. `anahtar` true ise `doğruda` girdisinden, false ise `yanlışta` girdisinden gelen değer olacaktır. |

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
