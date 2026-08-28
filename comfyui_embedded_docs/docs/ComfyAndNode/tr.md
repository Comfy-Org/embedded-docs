# Ve

And düğümü, bir dizi girdi değeri üzerinde mantıksal VE işlemi gerçekleştirir. Yalnızca sağlanan tüm değerler Python'un doğruluk değerlendirme kurallarına göre doğru kabul ediliyorsa `true` döndürür. Bu düğüm, devam etmeden önce birden fazla koşulun tamamının karşılandığını kontrol etmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `değerler` | Değerlendirilecek bir değer. Düğüm en az bir değer kabul eder; düğüm üzerindeki "+" düğmesine tıklayarak daha fazla değer ekleyebilirsiniz. Her tür veriyi kabul eder. | ANY | Evet | 1 veya daha fazla (üst sınır yok) |

**Not:** Düğüm, bir değerin `true` mu yoksa `false` mı olduğunu belirlemek için Python'un doğruluk değerlendirme kurallarını kullanır. Örneğin, boş bir dize, 0 sayısı, boş bir liste ve `None` değerleri `false` olarak kabul edilir. Diğer tüm değerler `true` olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `BOOLEAN` | Tüm girdi değerleri doğru kabul ediliyorsa `true`, aksi takdirde `false` döndürür. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/tr.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
