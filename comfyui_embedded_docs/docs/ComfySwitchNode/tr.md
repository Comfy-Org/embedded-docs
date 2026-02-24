> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

Switch düğümü, bir boolean koşula dayanarak iki olası girdi arasında seçim yapar. `switch` etkinleştirildiğinde `on_true` girdisini, devre dışı bırakıldığında ise `on_false` girdisini çıktı olarak verir. Bu, iş akışınızda koşullu mantık oluşturmanıza ve farklı veri yolları seçmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Evet | | Hangi girdinin geçirileceğini belirleyen bir boolean koşulu. Etkinleştirildiğinde (true), `on_true` girdisi seçilir. Devre dışı bırakıldığında (false), `on_false` girdisi seçilir. |
| `on_false` | MATCH_TYPE | Hayır | | `switch` devre dışı bırakıldığında (false) çıktıya geçirilecek veri. Bu girdi yalnızca `switch` false olduğunda gereklidir. |
| `on_true` | MATCH_TYPE | Hayır | | `switch` etkinleştirildiğinde (true) çıktıya geçirilecek veri. Bu girdi yalnızca `switch` true olduğunda gereklidir. |

**Girdi Gereksinimleri Hakkında Not:** `on_false` ve `on_true` girdileri koşullu olarak gereklidir. Düğüm, yalnızca `switch` true olduğunda `on_true` girdisini, yalnızca `switch` false olduğunda ise `on_false` girdisini talep edecektir. Her iki girdi de aynı veri türünde olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | Seçilen veri. `switch` true ise `on_true` girdisinden, false ise `on_false` girdisinden gelen değer olacaktır. |
