> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/tr.md)

## Genel Bakış

Ve düğümü, bir dizi girdi değeri üzerinde mantıksal VE işlemi gerçekleştirir. Python'un doğruluk kurallarına göre, yalnızca sağlanan tüm değerler doğru (truthy) olarak kabul edilirse `true` döndürür. Bu düğüm, devam etmeden önce birden çok koşulun tamamının karşılandığını kontrol etmek için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `değerler` | ANY | Evet | 1 veya daha fazla değer | Değerlendirilecek değerlerin listesi. Düğüm en az bir değer kabul eder ve düğüm üzerindeki "+" düğmesine tıklayarak daha fazla değer ekleyebilirsiniz. |

**Not:** Düğüm, bir değerin `true` veya `false` olup olmadığını belirlemek için Python'un doğruluk kurallarını kullanır. Örneğin, boş bir dize, 0 sayısı, boş bir liste ve `None` değerinin tümü `false` olarak kabul edilir. Diğer tüm değerler `true` olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `BOOLEAN` | BOOLEAN | Tüm girdi değerleri doğru (truthy) ise `true`, aksi takdirde `false` döndürür. |

---
**Source fingerprint (SHA-256):** `fd9d18ce698472a7e35ad3082f2ccff8ae264b11bd887a498f929cd877ff38c4`
