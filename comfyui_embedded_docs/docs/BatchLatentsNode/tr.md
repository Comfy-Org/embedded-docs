# Toplu Latentler

Batch Latents düğümü, birden fazla latent girdiyi tek bir batch halinde birleştirir. Değişken sayıda latent örnek alır ve bunları batch boyutu boyunca birleştirerek sonraki düğümlerde birlikte işlenmelerini sağlar. Bu, tek bir işlemde birden fazla görüntü üretmek veya işlemek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latents` | Tek bir batch halinde birleştirilecek latent örnekler kümesi. En az bir latent sağlamanız gerekir ve en fazla 50 ekleyebilirsiniz. Daha fazla latent bağladıkça düğüm otomatik olarak girdi yuvaları oluşturur. | LATENT | Evet | 1 ila 50 girdi |

**Not:** Düğümün çalışması için en az bir latent girdi sağlamanız gerekir. Düğüm, daha fazla latent bağladıkça en fazla 50 olacak şekilde otomatik olarak girdi yuvaları oluşturur.

Tüm girdi latentleri, birleştirilmeden önce ilk latentin uzamsal boyutlarına uyacak şekilde yeniden şekillendirilir. Her latentin `batch_index` meta verisi çıktıya aktarılır; `batch_index` değeri olmayan bir girdi, 0'dan başlayan varsayılan bir sıra alır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm girdi latentlerinin tek bir batch halinde birleştirilmiş halini içeren tek bir latent çıktısı. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/tr.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
