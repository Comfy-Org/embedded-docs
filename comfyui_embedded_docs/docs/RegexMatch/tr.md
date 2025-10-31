> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/tr.md)

RegexMatch düğümü, bir metin dizesinin belirtilen normal ifade deseniyle eşleşip eşleşmediğini kontrol eder. Girdi dizesinde regex deseninin herhangi bir oluşumunu arar ve bir eşleşme bulunup bulunmadığını döndürür. Desen eşleştirmenin nasıl davranacağını kontrol etmek için büyük/küçük harf duyarlılığı, çok satırlı mod ve dotall modu gibi çeşitli regex bayraklarını yapılandırabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | Eşleşmelerin aranacağı metin dizesi |
| `regex_pattern` | STRING | Evet | - | Dizeye karşı eşleştirilecek normal ifade deseni |
| `case_insensitive` | BOOLEAN | Hayır | - | Eşleştirme yaparken büyük/küçük harf duyarlılığını yoksayıp yoksamayacağı (varsayılan: True) |
| `multiline` | BOOLEAN | Hayır | - | Regex eşleştirmesi için çok satırlı modun etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) |
| `dotall` | BOOLEAN | Hayır | - | Regex eşleştirmesi için dotall modunun etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `matches` | BOOLEAN | Regex deseni girdi dizesinin herhangi bir bölümüyle eşleşirse True, aksi takdirde False döndürür |