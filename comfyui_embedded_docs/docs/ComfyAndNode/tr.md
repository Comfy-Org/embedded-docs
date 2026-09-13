# Ve

And düğümü, bir girdi değerleri grubu üzerinde mantıksal AND işlemi gerçekleştirir. Yalnızca bağlı her değer Python'un doğruluk (truthiness) kurallarına göre doğru kabul edildiğinde `true` döndürür; bu da birkaç koşulun aynı anda karşılandığını kontrol etmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `values` | Değerlendirilecek büyütülebilir bir değer grubu. Düğüm tek bir yuva ile başlar ve düğümdeki "+" düğmesine tıklayarak daha fazla ekleyebilirsiniz. Herhangi bir veri türünü kabul eder. | ANY | Evet | Minimum 1 (maksimum yok) |

**Not:** Bu girdi büyütülebilir bir yuva grubudur. Yuvalar tek tek eklenir (örneğin `value_1`, `value_2` ve benzeri) ve en az bir yuva bulunmalıdır.

**Not:** Düğüm, bir değerin `true` mu `false` mu olduğuna karar vermek için Python'un doğruluk kurallarını kullanır. Örneğin, boş bir dize, 0 sayısı, boş bir liste ve `None` değerlerinin tümü `false` olarak değerlendirilir. Diğer tüm değerler `true` olarak değerlendirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `BOOLEAN` | Tüm girdi değerleri doğru kabul edilirse `true`, aksi halde `false` döndürür. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/tr.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
