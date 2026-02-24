> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/tr.md)

**Merge Image Lists** düğümü, birden fazla ayrı görüntü listesini tek ve sürekli bir listede birleştirir. Bağlı her girdiden tüm görüntüleri alarak ve bunları alındıkları sırayla birbirine ekleyerek çalışır. Bu, farklı kaynaklardan gelen görüntüleri daha fazla işlem için düzenlemek veya gruplamak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Birleştirilecek bir görüntü listesi. Bu girdi birden fazla bağlantı kabul edebilir ve bağlanan her liste nihai çıktıya eklenecektir. |

**Not:** Bu düğüm birden fazla girdi alacak şekilde tasarlanmıştır. Tek `images` giriş soketine birden fazla görüntü listesi bağlayabilirsiniz. Düğüm, bağlı tüm listelerdeki tüm görüntüleri otomatik olarak tek bir çıktı listesinde birleştirecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Bağlı her girdi listesindeki tüm görüntüleri içeren, birleştirilmiş tek liste. |
