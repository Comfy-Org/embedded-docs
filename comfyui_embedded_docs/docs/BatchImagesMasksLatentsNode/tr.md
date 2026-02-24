> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/tr.md)

Batch Images/Masks/Latents düğümü, aynı türdeki birden fazla girdiyi tek bir toplu işte (batch) birleştirir. Girdilerin görüntü, maske veya gizli gösterim (latent) olup olmadığını otomatik olarak algılar ve uygun toplu işleme yöntemini kullanır. Bu, toplu girdi kabul eden düğümler tarafından işlenmek üzere birden fazla öğeyi hazırlamak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `inputs` | IMAGE, MASK veya LATENT | Evet | 1 ila 50 girdi | Toplu iş halinde birleştirilecek dinamik bir girdi listesi. 1 ila 50 arasında öğe ekleyebilirsiniz. Tüm öğeler aynı türde olmalıdır (hepsi görüntü, hepsi maske veya hepsi latent). |

**Not:** Düğüm, veri türünü (IMAGE, MASK veya LATENT) `inputs` listesindeki ilk öğeye göre otomatik olarak belirler. Sonraki tüm öğeler bu türle eşleşmelidir. Farklı veri türlerini karıştırmaya çalışırsanız düğüm hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE, MASK veya LATENT | Tek bir toplu çıktı. Veri türü, girdi türüyle eşleşir (toplu IMAGE, toplu MASK veya toplu LATENT). |
