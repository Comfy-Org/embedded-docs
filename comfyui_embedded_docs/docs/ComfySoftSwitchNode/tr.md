# ComfySoftSwitchNode

Soft Switch düğümü, boole koşuluna dayalı olarak iki olası girdi değeri arasında seçim yapar. `switch` true olduğunda `on_true` girdisindeki değeri, `switch` false olduğunda ise `on_false` girdisindeki değeri çıktı olarak verir. Bu düğüm tembel (lazy) olacak şekilde tasarlanmıştır; yani anahtar durumuna bağlı olarak yalnızca ihtiyaç duyulan girdiyi değerlendirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `switch` | Hangi girdinin geçirileceğini belirleyen boole koşulu. true olduğunda `on_true` girdisi seçilir. false olduğunda `on_false` girdisi seçilir. | BOOLEAN | Evet | true<br>false |
| `on_false` | `switch` koşulu false olduğunda çıktı olarak verilecek değer. Bu girdi isteğe bağlıdır; ancak `on_false` veya `on_true` girdilerinden en az biri bağlanmış olmalıdır. | MATCH_TYPE | Hayır |  |
| `on_true` | `switch` koşulu true olduğunda çıktı olarak verilecek değer. Bu girdi isteğe bağlıdır; ancak `on_false` veya `on_true` girdilerinden en az biri bağlanmış olmalıdır. | MATCH_TYPE | Hayır |  |

**Not:** `on_false` ve `on_true` girdileri, düğümün dahili şablonunda tanımlandığı gibi aynı veri türünde olmalıdır. Düğümün çalışması için bu iki girdiden en az birinin bağlanmış olması gerekir. Yalnızca bir girdi bağlanırsa, `switch` durumu ne olursa olsun bu değer çıktıya iletilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçilen değer. Bağlı olan `on_false` veya `on_true` girdisinin veri türüyle eşleşir. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
