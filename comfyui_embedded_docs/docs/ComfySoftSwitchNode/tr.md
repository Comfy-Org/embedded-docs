# ComfySoftSwitchNode

Soft Switch düğümü, boolean bir koşula bağlı olarak iki olası girdi değeri arasında seçim yapar. `switch` true olduğunda `on_true` girdisinden, `switch` false olduğunda `on_false` girdisinden değeri çıktı olarak verir. Bu düğüm tembel (lazy) olacak şekilde tasarlanmıştır; yani `switch` durumuna bağlı olarak yalnızca ihtiyaç duyulan girdiyi değerlendirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `switch` | Hangi girdinin iletileceğini belirleyen boolean koşul. True olduğunda `on_true` girdisi seçilir. False olduğunda `on_false` girdisi seçilir. | BOOLEAN | Evet | True or False |
| `on_false` | `switch` koşulu false olduğunda çıktı olarak verilecek değer. Bu girdi isteğe bağlıdır, ancak `on_false` veya `on_true` girdilerinden en az biri bağlanmalıdır. | MATCH_TYPE | Hayır | `on_true` ile aynı veri türü |
| `on_true` | `switch` koşulu true olduğunda çıktı olarak verilecek değer. Bu girdi isteğe bağlıdır, ancak `on_false` veya `on_true` girdilerinden en az biri bağlanmalıdır. | MATCH_TYPE | Hayır | `on_false` ile aynı veri türü |

**Not:** `on_false` ve `on_true` girdileri, düğümün dahili şablonunda tanımlandığı gibi aynı veri türünde olmalıdır. Düğümün çalışması için bu iki girdiden en az birinin bağlı olması gerekir. Düğüm tembel olduğundan, yalnızca bir girdi bağlandığında, `switch` durumu ne olursa olsun düğüm her zaman o girdinin değerini çıktı olarak verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçilen değer. Bağlı `on_false` veya `on_true` girdisinin veri türüyle eşleşir. Her iki girdi de bağlandığında, `switch` true ise `on_true` değerini, `switch` false ise `on_false` değerini çıktı olarak verir. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
