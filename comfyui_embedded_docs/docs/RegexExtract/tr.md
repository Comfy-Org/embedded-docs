> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/tr.md)

RegexExtract düğümü, metin içinde düzenli ifadeler kullanarak desenleri arar. İlk eşleşmeyi, tüm eşleşmeleri, eşleşmelerden belirli grupları veya birden fazla eşleşmedeki tüm grupları bulabilir. Düğüm, büyük/küçük harf duyarlılığı, çok satırlı eşleştirme ve dotall davranışı için çeşitli regex bayraklarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | Desenleri aranacak giriş metni |
| `regex_pattern` | STRING | Evet | - | Aranacak düzenli ifade deseni |
| `mode` | COMBO | Evet | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" | Çıkarım modu, eşleşmelerin hangi bölümlerinin döndürüleceğini belirler |
| `case_insensitive` | BOOLEAN | Hayır | - | Eşleştirme yaparken büyük/küçük harf duyarlılığını yoksayıp yoksamayacağı (varsayılan: True) |
| `multiline` | BOOLEAN | Hayır | - | Dizeyi çoklu satırlar olarak işleyip işlemeyeceği (varsayılan: False) |
| `dotall` | BOOLEAN | Hayır | - | Noktanın (.) yeni satırları eşleştirip eşleştirmeyeceği (varsayılan: False) |
| `group_index` | INT | Hayır | 0-100 | Grup modları kullanılırken çıkarılacak yakalama grubu dizini (varsayılan: 1) |

**Not:** "First Group" veya "All Groups" modları kullanılırken, `group_index` parametresi hangi yakalama grubunun çıkarılacağını belirtir. Grup 0, tüm eşleşmeyi temsil ederken, 1+ grupları regex deseninizdeki numaralandırılmış yakalama gruplarını temsil eder.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Seçilen mod ve parametrelere dayalı olarak çıkarılan metin |