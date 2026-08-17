# HappyHorse Video Düzenleme

HappyHorse modeliyle metin talimatlarını veya referans görsellerini kullanarak bir videoyu düzenleyin. Çıktı süresi 3-15 saniyedir ve giriş videosuyla eşleşir; 15 saniyeden uzun girişler kısaltılır.
## Girişler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `model` | Kullanılacak HappyHorse video düzenleme modeli. Bu seçim, hangi prompt, çözünürlük, oran ve referans görsel seçeneklerinin kullanılabilir olduğunu belirler. | DYNAMIC_COMBO | Evet | "happyhorse-1.0-video-edit" |
| `video` | Düzenlenecek video. | VIDEO | Evet | 3 to 60 seconds |
| `seed` | Üretim için kullanılacak seed (varsayılan: 0). | INT | Evet | 0 to 2147483647 |
| `watermark` | Sonuca yapay zeka tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Evet | True<br>False |

### happyhorse-1.0-video-edit Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt` | Düzenleme talimatları veya stil aktarımı gereksinimleri. En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `resolution` | Çıktı çözünürlüğü. | COMBO | Evet | "720P"<br>"1080P" |
| `ratio` | En boy oranı. Değiştirilmezse, giriş videosunun oranına yaklaşır. | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `reference_images` | Genişletilebilir yuva: düzenlemeyi yönlendirmek için 0 ila 5 referans görseli bağlayın (`image1`...`image5`). | IMAGE | Hayır | 0 to 5 images |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `video` | The edited video output. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`
