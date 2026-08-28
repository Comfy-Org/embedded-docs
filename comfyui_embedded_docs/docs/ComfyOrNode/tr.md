# Veya

Or düğümü, bir dizi girdi değeri üzerinde mantıksal VEYA (OR) işlemi gerçekleştirir. Python'un standart doğruluk (truthiness) kurallarına göre, sağlanan değerlerden herhangi biri doğru (truthy) kabul edilirse `true` değerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `değerler` | Doğruluk değerlerini değerlendirmek için büyütülebilir bir değer koleksiyonu. Eklenen her girdi yuvası `value_1`, `value_2` vb. şeklinde adlandırılır. Bu değerlerden herhangi biri doğru (truthy) ise düğüm `true` değerini döndürür. | ANY | Evet | 1 veya daha fazla değer |

**Not:** Düğüm en az 1 girdi değeri kabul eder. Otomatik büyüme özelliğini kullanarak gerektiği kadar girdi ekleyebilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `BOOLEAN` | Girdi değerlerinden herhangi biri doğru (truthy) ise `true`; tüm girdi değerleri yanlış (falsy) ise `false` döndürür. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/tr.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
