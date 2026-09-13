# Toplu Latentler

Batch Latents düğümü, birden çok latent girdisini tek bir batch içinde birleştirir. Değişken sayıda latent örneği alır ve sonraki düğümler tarafından birlikte işlenebilmeleri için bunları batch boyutu boyunca birleştirir. Düğüm ayrıca tüm girdilerin batch dizini meta verilerini birleştirilmiş çıktıda birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latentler` | Tek bir batch içinde birleştirilecek bir dizi latent örneği. En az bir latent sağlamanız gerekir ve 50'ye kadar ekleyebilirsiniz. Daha fazla latent bağladıkça düğüm otomatik olarak girdi yuvaları (`latent_1`, `latent_2` vb.) oluşturur. | LATENT | Evet | 1 ila 50 girdi |

**Not:** Düğümün çalışması için en az bir latent girdisi sağlamalısınız. Daha fazla latent bağladıkça düğüm otomatik olarak girdi yuvaları oluşturur, en fazla 50'ye kadar. Birleştirilmeden önce her girdi latentı, ilk latentın örnek şekliyle eşleşecek şekilde yeniden şekillendirilir ve batch dizini meta verisi olmayan her latent için sıralı bir batch dizini atanır. Girdi latentları, birleştirilmiş sonucu üretmek için batch boyutu boyunca birleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tek bir batch içinde birleştirilmiş tüm girdi latentlarını ve bunların birleştirilmiş batch dizini meta verilerini içeren tek bir latent çıktısı. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/tr.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
