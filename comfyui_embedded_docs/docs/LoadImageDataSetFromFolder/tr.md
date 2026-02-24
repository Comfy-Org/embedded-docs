> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/tr.md)

Bu düğüm, ComfyUI'nin giriş dizini içinde belirtilen bir alt klasörden birden fazla görüntü yükler. Seçilen klasördeki yaygın görüntü dosya türlerini tarar ve bunları bir liste olarak döndürür; bu, toplu işleme veya veri kümesi hazırlama için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Evet | *Birden fazla seçenek mevcut* | Görüntülerin yükleneceği klasör. Seçenekler, ComfyUI'nin ana giriş dizininde bulunan alt klasörlerdir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Yüklenen görüntülerin listesi. Düğüm, seçilen klasörde bulunan tüm geçerli görüntü dosyalarını (PNG, JPG, JPEG, WEBP) yükler. |
