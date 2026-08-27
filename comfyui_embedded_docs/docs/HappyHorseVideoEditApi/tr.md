# HappyHorse Video Düzenleme

HappyHorse modeli ile metin talimatlarını veya referans görsellerini kullanarak bir videoyu düzenleyin. Çıktı süresi 3-15 saniyedir ve girdi videosuyla eşleşir; 15 saniyeden uzun girdiler kırpılır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak HappyHorse video düzenleme modeli. Bu seçim, hangi prompt, çözünürlük, oran ve referans görsel seçeneklerinin kullanılabilir olduğunu belirler. | DYNAMIC_COMBO | Evet | "happyhorse-1.0-video-edit" |
| `video` | Düzenlenecek video. | VIDEO | Evet | 3 ila 60 saniye |
| `tohum` | Üretim için kullanılacak seed (varsayılan: 0). | INT | Evet | 0 ila 2147483647 |
| `filigran` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). Gelişmiş parametre. | BOOLEAN | Evet | True<br>False |

### happyhorse-1.0-video-edit Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları veya stil aktarımı gereksinimleri. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `resolution` | Çıktı çözünürlüğü. | COMBO | Evet | "720P"<br>"1080P" |
| `ratio` | En-boy oranı. Değiştirilmezse, girdi video oranına yaklaşır. | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Genişletilebilir yuva: düzenlemeyi yönlendirmek için 0 ila 5 referans görseli (`image1`...`image5`) bağlayın. | IMAGE | Hayır | 0 ila 5 görsel |

**Not:** Girdi videosu 3 ila 60 saniye uzunluğunda olmalıdır. Çıktı süresi 3-15 saniyedir ve girdi videosuyla eşleşir; 15 saniyeden uzun girdi videoları kırpılır. `prompt` en az 1 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Düzenlenmiş video çıktısı. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`
