# Ve

And düğümü, bir dizi girdi değeri üzerinde mantıksal AND işlemi gerçekleştirir. Yalnızca sağlanan tüm değerler Python'un doğruluk (truthiness) kurallarına göre truthy kabul edilirse `true` döndürür. Bu düğüm, devam etmeden önce birden fazla koşulun karşılandığını kontrol etmek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `values` | Değerlendirilecek genişletilebilir değer listesi. Düğüm en az bir değer gerektirir ve düğümdeki "+" düğmesine tıklayarak daha fazla yuva ekleyebilirsiniz. Her yuva herhangi bir veri türünü kabul eder. | ANY | Evet | 1 veya daha fazla değer |

**Not:** Düğüm, bir değerin `true` veya `false` olup olmadığını belirlemek için Python'un doğruluk (truthiness) kurallarını kullanır. Örneğin, boş bir dize, 0 sayısı, boş bir liste ve `None` değerinin tümü `false` olarak kabul edilir. Diğer tüm değerler `true` olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `BOOLEAN` | Tüm girdi değerleri truthy ise `true`, aksi takdirde `false` döndürür. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/tr.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
