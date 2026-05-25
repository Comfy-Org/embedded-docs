> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/tr.md)

# ComfyOrNode

ComfyOrNode düğümü, bir dizi girdi değeri üzerinde mantıksal VEYA işlemi gerçekleştirir. Python'un standart doğruluk kurallarına göre sağlanan değerlerden herhangi biri doğru (truthy) olarak kabul edilirse `true` döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `value` | ANY | Evet | Birden çok değer kabul edilir | Doğruluk değerlendirmesi için bir değer. Daha fazla girdi ekleyerek birden çok değer sağlayabilirsiniz. Bu değerlerden herhangi biri doğru (truthy) ise düğüm `true` döndürür. |

**Not:** Düğüm en az 1 girdi değeri kabul eder. Otomatik büyütme özelliğini kullanarak gerektiği kadar girdi ekleyebilirsiniz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `BOOLEAN` | BOOLEAN | Girdi değerlerinden herhangi biri doğru (truthy) ise `true` döndürür; tüm girdi değerleri yanlış (falsy) ise `false` döndürür. |

---
**Source fingerprint (SHA-256):** `00c60d5c80bbddc993af0bcd92e35dc77f153731329c23a6e4e9a980709111b1`
