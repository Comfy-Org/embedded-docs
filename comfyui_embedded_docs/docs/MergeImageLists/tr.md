# Görüntü Listelerini Birleştir

Görüntü Listelerini Birleştir düğümü, birden fazla ayrı görüntü listesini tek ve sürekli bir listede birleştirir. Bağlı her girdiden tüm görüntüleri alarak ve bunları alındıkları sırayla birbirine ekleyerek çalışır. Bu, farklı kaynaklardan gelen görüntüleri daha sonraki işlemler için düzenlemek veya gruplamak amacıyla kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Birleştirilecek görüntü listesi. Bu girdi birden fazla bağlantı kabul edebilir ve bağlı her liste nihai çıktıda birleştirilecektir. | IMAGE | Evet | - |

**Not:** Bu düğüm birden fazla girdi alacak şekilde tasarlanmıştır. Tek `images` girdi soketine birden fazla görüntü listesi bağlayabilirsiniz. Düğüm, bağlı tüm listelerdeki tüm görüntüleri otomatik olarak tek bir çıktı listesinde birleştirecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | Bağlı her girdi listesindeki tüm görüntüleri içeren, birleştirilmiş tek liste. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/tr.md)

---
**Source fingerprint (SHA-256):** `8fc53091b817a5036aae022aa841ba11fae0ed3242a969f5ae9072f48e061366`
