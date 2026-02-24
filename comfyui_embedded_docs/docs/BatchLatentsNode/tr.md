> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/tr.md)

Batch Latents düğümü, birden fazla gizli (latent) girdiyi tek bir toplu işlemde birleştirir. Değişken sayıda gizli örnek alır ve bunları toplu işlem (batch) boyutu boyunca birleştirerek, sonraki düğümlerde birlikte işlenmelerini sağlar. Bu, tek bir işlemde birden fazla görüntü oluşturmak veya işlemek için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Evet | Yok | Toplu işleme dahil edilecek ilk gizli örnek. |
| `latent_2` ila `latent_50` | LATENT | Hayır | Yok | Toplu işleme dahil edilecek ek gizli örnekler. Toplamda 2 ile 50 arasında gizli girdi ekleyebilirsiniz. |

**Not:** Düğümün çalışması için en az iki gizli girdi sağlamanız gerekir. Düğüm, daha fazla gizli örnek bağladıkça, maksimum 50'ye kadar otomatik olarak girdi yuvaları oluşturacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | LATENT | Tüm girdi gizli örneklerini tek bir toplu işlemde birleştiren tek bir gizli çıktı. |
