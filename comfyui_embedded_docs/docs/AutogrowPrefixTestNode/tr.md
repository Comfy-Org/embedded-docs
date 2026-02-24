> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/tr.md)

AutogrowPrefixTestNode, otomatik büyüyen giriş özelliğini test etmek için tasarlanmış bir mantık düğümüdür. Dinamik sayıda kayan nokta girişi kabul eder, değerlerini virgülle ayrılmış bir dize halinde birleştirir ve bu dizeyi çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | AUTOGROW | Evet | 1 ila 10 giriş | 1 ila 10 arasında kayan nokta değeri kabul edebilen dinamik bir giriş grubu. Gruptaki her giriş bir FLOAT türündedir. |

**Not:** `autogrow` girişi özel bir dinamik giriştir. Bu gruba en fazla 10 adet olmak üzere birden fazla kayan nokta girişi ekleyebilirsiniz. Düğüm, sağlanan tüm değerleri işleyecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Tüm giriş kayan nokta değerlerini virgüllerle ayrılmış halde içeren tek bir dize. |
