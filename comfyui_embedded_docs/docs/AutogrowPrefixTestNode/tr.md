# AutogrowPrefixTestNode

AutogrowPrefixTestNode, autogrow girdi özelliğini test eden bir mantık düğümüdür. Dinamik sayıda float girdisi kabul eder, her değeri metne dönüştürür, bunları virgülle ayrılmış bir dizede birleştirir ve bu dizeyi çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | 1 ile 10 arasında float değeri kabul eden dinamik bir girdi grubudur. Her değer bir ondalıklı sayıdır ve oluşturulan girdiler `float` önekiyle adlandırılır. | AUTOGROW | Evet | 1 ila 10 girdi |

**Not:** `autogrow` girdisi özel bir dinamik girdidir. Bu gruba en az 1, en fazla 10 olacak şekilde birden fazla float girdisi ekleyebilirsiniz. Düğüm, sağlanan tüm değerleri işler ve bağlı her girdiyi çıktı dizesine dahil eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm girdi float değerlerini virgülle ayrılmış olarak içeren tek bir dizedir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/tr.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
