Soft Switch düğümü, boolean bir koşula bağlı olarak iki olası giriş değeri arasında seçim yapar. `switch` değeri true olduğunda `on_true` girişinden, false olduğunda ise `on_false` girişinden gelen değeri çıktı olarak verir. Bu düğüm tembel (lazy) çalışacak şekilde tasarlanmıştır; yani anahtar durumuna bağlı olarak yalnızca ihtiyaç duyulan girişi değerlendirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `switch` | Hangi girişin iletileceğini belirleyen boolean koşulu. True olduğunda `on_true` girişi seçilir. False olduğunda `on_false` girişi seçilir. | BOOLEAN | Evet |  |
| `on_false` | `switch` koşulu false olduğunda çıktı olarak verilecek değer. Bu giriş isteğe bağlıdır, ancak `on_false` veya `on_true` girişlerinden en az biri bağlanmalıdır. | MATCH_TYPE | Hayır |  |
| `on_true` | `switch` koşulu true olduğunda çıktı olarak verilecek değer. Bu giriş isteğe bağlıdır, ancak `on_false` veya `on_true` girişlerinden en az biri bağlanmalıdır. | MATCH_TYPE | Hayır |  |

**Not:** `on_false` ve `on_true` girişleri, düğümün dahili şablonu tarafından tanımlandığı şekilde aynı veri türünde olmalıdır. Düğümün çalışması için bu iki girişten en az birinin bağlı olması gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçilen değer. Bağlı olan `on_false` veya `on_true` girişinin veri türüyle eşleşir. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `f5e40e7f43948b81b5442c885c3e1ff15e38f8f7ddda00ef3be42225765bfd1c`
