> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/tr.md)

Soft Switch düğümü, bir boolean koşuluna dayanarak iki olası giriş değeri arasında seçim yapar. `switch` true olduğunda `on_true` girişindeki değeri, false olduğunda ise `on_false` girişindeki değeri çıktı olarak verir. Bu düğüm, yalnızca switch durumuna bağlı olarak ihtiyaç duyulan girişi değerlendiren "tembel" (lazy) bir tasarıma sahiptir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | Evet | | Hangi girişin geçirileceğini belirleyen boolean koşulu. True olduğunda `on_true` girişi seçilir. False olduğunda `on_false` girişi seçilir. |
| `on_false` | MATCH_TYPE | Hayır | | `switch` koşulu false olduğunda çıktılanacak değer. Bu giriş isteğe bağlıdır, ancak `on_false` veya `on_true` girişlerinden en az biri bağlanmış olmalıdır. |
| `on_true` | MATCH_TYPE | Hayır | | `switch` koşulu true olduğunda çıktılanacak değer. Bu giriş isteğe bağlıdır, ancak `on_false` veya `on_true` girişlerinden en az biri bağlanmış olmalıdır. |

**Not:** `on_false` ve `on_true` girişleri, düğümün dahili şablonu tarafından tanımlandığı gibi aynı veri türünde olmalıdır. Düğümün çalışması için bu iki girişten en az biri bağlanmış olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | Seçilen değer. Bağlanan `on_false` veya `on_true` girişinin veri türüyle eşleşecektir. |
