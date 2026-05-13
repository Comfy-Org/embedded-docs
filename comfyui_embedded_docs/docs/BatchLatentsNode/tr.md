> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/tr.md)

**Batch Latents (Toplu Gizli Değişkenler) düğümü**, birden fazla gizli değişken girdisini tek bir toplu işlemde birleştirir. Değişken sayıda gizli değişken örneği alır ve bunları toplu işlem boyutu boyunca birleştirerek sonraki düğümlerde birlikte işlenmelerini sağlar. Bu, tek bir işlemde birden fazla görüntü oluşturmak veya işlemek için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Evet | 2 ila 50 girdi | Tek bir toplu işlemde birleştirilecek bir dizi gizli değişken örneği. En az iki gizli değişken sağlamalısınız ve en fazla 50 tane ekleyebilirsiniz. Düğüm, daha fazla gizli değişken bağladıkça otomatik olarak girdi yuvaları oluşturur. |

**Not:** Düğümün çalışması için en az iki gizli değişken girdisi sağlamalısınız. Düğüm, daha fazla gizli değişken bağladıkça, maksimum 50'ye kadar otomatik olarak girdi yuvaları oluşturacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Tüm girdi gizli değişkenlerini tek bir toplu işlemde birleştiren tek bir gizli değişken çıktısı. |

---
**Source fingerprint (SHA-256):** `215e7e2df43e902815dd87d228e8d5e09f18f6f52002cc3e861551fc207a9896`
