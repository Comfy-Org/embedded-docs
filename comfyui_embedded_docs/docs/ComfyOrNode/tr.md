# Veya

ComfyOrNode, bir dizi girdi değeri üzerinde mantıksal VEYA (OR) işlemi gerçekleştirir. Sağlanan değerlerden herhangi biri, Python'un standart doğruluk (truthiness) kurallarına göre doğru (truthy) kabul ediliyorsa `true` değerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `value` | Doğruluk değeri değerlendirilecek bir değer. Daha fazla girdi ekleyerek birden çok değer sağlayabilirsiniz. Düğüm, bu değerlerden herhangi biri doğru (truthy) ise `true` değerini döndürür. | ANY | Evet | Minimum 1 değer; birden çok değer kabul edilir |

**Not:** Düğüm minimum 1 girdi değeri kabul eder. Otomatik genişletme (autogrow) özelliğini kullanarak gerektiğinde daha fazla girdi ekleyebilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `BOOLEAN` | Girdi değerlerinden herhangi biri doğru (truthy) ise `true`; tüm girdi değerleri yanlış (falsy) ise `false` döndürür. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/tr.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
