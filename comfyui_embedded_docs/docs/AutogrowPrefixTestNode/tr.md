# AutogrowPrefixTestNode

AutogrowPrefixTestNode, otomatik büyüyen girdi (autogrow) özelliğini test etmek için tasarlanmış bir mantık düğümüdür. Dinamik sayıda float girdisi kabul eder, bu değerleri virgülle ayrılmış bir dize hâlinde birleştirir ve bu dizeyi çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | Float değerleri kabul eden dinamik bir girdi grubudur. Grup, 1 ile 10 arasında float girdisi tutabilir ve düğüm, sağlanan tüm değerleri işler. | FLOAT | Evet | 1 ila 10 girdi |

**Not:** `autogrow` girdisi, en fazla 10 float girdisi eklemek için genişletilebilen özel bir dinamik girdidir. Minimum 1 girdidir. Bu düğümdeki `min` ve `max` değerleri, grupta izin verilen girdi sayısını tanımlar; her bir float değerinin değer aralığını değil.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm girdi float değerlerini virgülle ayrılmış olarak içeren tek bir dize. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
