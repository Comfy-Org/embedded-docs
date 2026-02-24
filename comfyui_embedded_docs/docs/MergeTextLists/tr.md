> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/tr.md)

Bu düğüm, birden fazla metin listesini tek bir birleşik listede birleştirir. Metin girişlerini liste olarak alacak şekilde tasarlanmıştır ve bunları birbirine ekler. Düğüm, birleştirilmiş listedeki toplam metin sayısını kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `texts` | STRING | Evet | Yok | Birleştirilecek metin listeleri. Girişe birden fazla liste bağlanabilir ve bunlar tek bir listede birleştirilir. |

**Not:** Bu düğüm bir grup işlemi olarak yapılandırılmıştır (`is_group_process = True`), yani ana işleme fonksiyonu çalışmadan önce birden fazla liste girişini otomatik olarak birleştirerek işler.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `texts` | STRING | Tüm giriş metinlerini içeren tek, birleştirilmiş liste. |
