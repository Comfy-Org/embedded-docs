# Toplu Latentler

The Batch Latents düğümü, birden fazla latent girdiyi tek bir batch halinde birleştirir. Değişken sayıda latent örnek alır ve bunları batch boyutu boyunca birleştirir; böylece sonraki düğümler tarafından birlikte işlenebilirler. Düğüm ayrıca tüm girdilerin batch indeks meta verilerini birleştirilmiş çıktıda birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latentler` | Tek bir batch halinde birleştirilecek latent örnekler kümesi. En az bir latent sağlamanız gerekir ve en fazla 50 ekleyebilirsiniz. Daha fazla latent bağladıkça düğüm otomatik olarak girdi yuvaları oluşturur. | LATENT | Evet | 1 ile 50 inputs |

**Not:** Düğümün çalışması için en az bir latent girdi sağlamanız gerekir. Düğüm, daha fazla latent bağladıkça en fazla 50 olacak şekilde otomatik olarak girdi yuvaları oluşturur. Her girdi latentı, birleştirilmeden önce ilk latentın örnek şekline uyacak şekilde yeniden şekillendirilir ve batch indeks meta verisi olmayan her latentaya sıralı bir batch indeksi atanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm girdi latentlarını tek bir batch halinde ve birleştirilmiş batch indeks meta verileriyle birlikte içeren tek bir latent çıktısı. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/tr.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
