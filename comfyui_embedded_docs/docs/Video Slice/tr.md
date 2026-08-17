# Video Dilimle

Video Slice düğümü, bir videodan belirli bir bölümü çıkarmanızı sağlar. Videoyu kırpmak için bir başlangıç zamanı ve süre tanımlayabilir veya yalnızca başlangıç karelerini atlayabilirsiniz. İstenen süre, kalan videodan daha uzunsa, düğüm mevcut olanı döndürebilir veya bir hata fırlatabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kesilecek giriş videosu. | VIDEO | Evet | - |
| `start_time` | Saniye cinsinden başlangıç zamanı (varsayılan: 0.0). | FLOAT | Hayır | -1e5 ila 1e5 |
| `duration` | Saniye cinsinden süre veya sınırsız süre için 0 (varsayılan: 0.0). | FLOAT | Hayır | 0.0 ve üzeri |
| `strict_duration` | True ise, belirtilen süre mümkün olmadığında bir hata fırlatılır (varsayılan: False). | BOOLEAN | Hayır | - |

Not: `duration` 0 olduğunda, düğüm `start_time`'dan videonun sonuna kadar dilimler. İstenen bölüm oluşturulamazsa — örneğin `start_time` videonun sonunun ötesindeyse — düğüm bir hata fırlatır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Kırpılmış video bölümü. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/tr.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
