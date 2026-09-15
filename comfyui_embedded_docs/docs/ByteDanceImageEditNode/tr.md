# ByteDanceImageEditNode

ByteDance Image Edit düğümü, ByteDance'in yapay zeka modellerini bir API aracılığıyla kullanarak görüntüleri değiştirmenize olanak tanır. İstediğiniz değişiklikleri açıklayan bir metin istemi ve bir girdi görüntüsü sağlarsınız; düğüm, görüntüyü talimatlarınıza göre işler. Düğüm, API iletişimini otomatik olarak yönetir ve düzenlenmiş görüntüyü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Girdi Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `model` | Model adı | MODEL | COMBO | seededit_3 | Image2ImageModelName seçenekleri |
| `image` | Düzenlenecek temel görüntü | IMAGE | IMAGE | - | - |
| `prompt` | Görüntüyü düzenleme talimatı | STRING | STRING | "" | - |
| `seed` | Üretim için kullanılacak tohum değeri | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | Daha yüksek bir değer, görüntünün istemi daha yakından takip etmesini sağlar | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | Görüntüye "AI generated" filigranı eklenip eklenmeyeceği | BOOLEAN | BOOLEAN | True | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | ByteDance API'sinden döndürülen düzenlenmiş görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
