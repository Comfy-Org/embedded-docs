> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/tr.md)

Giriş dizininden birden çok görseli toplu işleme ve eğitim amaçları için yükler. Çeşitli görsel formatlarını destekler ve isteğe bağlı olarak farklı yöntemler kullanarak görselleri yeniden boyutlandırabilir. Bu düğüm, seçilen tüm görselleri bir toplu iş olarak işler ve bunları tek bir tensör olarak döndürür.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Birden çok görsel dosyası | Giriş dizininden birden çok görsel seçin. PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF ve TIFF formatlarını destekler. Görsellerin toplu seçimine izin verir. |
| `resize_method` | STRING | Hayır | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Yüklenen görselleri yeniden boyutlandırmak için isteğe bağlı yöntem (varsayılan: "None"). Orijinal boyutları korumak için "None", zorla yeniden boyutlandırmak için "Stretch", kırparak en-boy oranını korumak için "Crop" veya dolgu ekleyerek en-boy oranını korumak için "Pad" seçeneğini belirleyin. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Daha ileri işlemler için yüklenen tüm görselleri bir toplu iş olarak içeren bir tensör. |

---
**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`
