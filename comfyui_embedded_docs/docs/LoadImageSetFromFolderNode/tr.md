> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/tr.md)

LoadImageSetFromFolderNode, eğitim amaçları için belirtilen bir klasör dizininden birden fazla görüntü yükler. Yaygın görüntü formatlarını otomatik olarak algılar ve isteğe bağlı olarak görüntüleri farklı yöntemler kullanarak yeniden boyutlandırabilir ve bunları bir toplu iş olarak döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Evet | Birden fazla seçenek mevcut | Görüntülerin yükleneceği klasör. |
| `resize_method` | STRING | Hayır | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Görüntüleri yeniden boyutlandırmak için kullanılacak yöntem (varsayılan: "None"). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Tek bir tensör olarak yüklenen görüntülerin toplu işi. |