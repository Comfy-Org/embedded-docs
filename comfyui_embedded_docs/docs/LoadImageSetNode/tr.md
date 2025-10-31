> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/tr.md)

LoadImageSetNode, toplu işleme ve eğitim amaçları için giriş dizininden birden fazla görüntü yükler. Çeşitli görüntü formatlarını destekler ve isteğe bağlı olarak görüntüleri farklı yöntemlerle yeniden boyutlandırabilir. Bu düğüm, seçilen tüm görüntüleri bir toplu iş olarak işler ve tek bir tensör olarak döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Birden fazla görüntü dosyası | Giriş dizininden birden fazla görüntü seçin. PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF ve TIFF formatlarını destekler. Görüntülerin toplu seçimine izin verir. |
| `resize_method` | STRING | Hayır | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Yüklenen görüntüleri yeniden boyutlandırmak için isteğe bağlı yöntem (varsayılan: "None"). Orijinal boyutları korumak için "None", zorla yeniden boyutlandırmak için "Stretch", en-boy oranını koruyarak kırpmak için "Crop" veya en-boy oranını koruyarak dolgu eklemek için "Pad" seçeneğini belirleyin. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Daha fazla işleme için yüklenen tüm görüntüleri bir toplu iş olarak içeren bir tensör. |