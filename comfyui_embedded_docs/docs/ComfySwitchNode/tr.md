# Anahtar

Switch düğümü, bir boolean koşula dayalı olarak iki olası girdi arasında seçim yapar. `switch` etkinleştirildiğinde `on_true` girdisini, devre dışı bırakıldığında ise `on_false` girdisini çıktı olarak verir; böylece iş akışınızda koşullu mantık oluşturmanıza ve farklı veri yollarını seçmenize olanak tanır. Bu düğüm şu anda deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `switch` | Hangi girdinin iletileceğini belirleyen bir boolean koşuldur. Etkinleştirildiğinde (true), `on_true` girdisi seçilir. Devre dışı bırakıldığında (false), `on_false` girdisi seçilir. | BOOLEAN | Evet |  |
| `on_false` | `switch` devre dışı bırakıldığında (false) çıktıya iletilecek veridir. Bu girdi yalnızca `switch` false olduğunda gereklidir. | MATCH_TYPE | Hayır |  |
| `on_true` | `switch` etkinleştirildiğinde (true) çıktıya iletilecek veridir. Bu girdi yalnızca `switch` true olduğunda gereklidir. | MATCH_TYPE | Hayır |  |

**Girdi Gereksinimleri Notu:** `on_false` ve `on_true` girdileri koşullu olarak gereklidir. Düğüm, `on_true` girdisini yalnızca `switch` true olduğunda, `on_false` girdisini ise yalnızca `switch` false olduğunda ister. Her iki girdi de aynı veri türünde olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçilen veridir. `switch` true ise `on_true` girdisindeki değer, `switch` false ise `on_false` girdisindeki değer olacaktır. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
