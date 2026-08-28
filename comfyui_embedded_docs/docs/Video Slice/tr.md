# Video Dilimle

Video Slice düğümü, bir videodan belirli bir bölümü çıkarmanızı sağlar. Videoyu kırpmak için bir başlangıç zamanı ve süre tanımlayabilir veya başlangıç karelerini atlayabilirsiniz. İstenen süre kalan videodan daha uzunsa, düğüm mevcut kısmı döndürebilir ya da bir hata yükseltebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kırpılacak girdi videosu. | VIDEO | Evet | - |
| `başlangıç zamanı` | Başlangıç zamanı saniye cinsinden (varsayılan: 0.0). | FLOAT | Evet | -1e5 ile 1e5 |
| `süre` | Saniye cinsinden süre; 0 ise sınırsız süre (varsayılan: 0.0). | FLOAT | Evet | 0.0 ve üzeri |
| `kesin süre` | True ise, belirtilen süre mümkün olmadığında bir hata yükseltilir (varsayılan: False). | BOOLEAN | Evet | - |

**Not:** Video, verilen `start_time` ve `duration` için kırpılamazsa düğüm bir hata yükseltir. `strict_duration` False olduğunda, istenen süre kalan uzunluğu aşarsa düğüm videonun mevcut kısmını döndürür; True olduğunda ise bunun yerine bir hata yükseltir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Kırpılmış video bölümü. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/tr.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
