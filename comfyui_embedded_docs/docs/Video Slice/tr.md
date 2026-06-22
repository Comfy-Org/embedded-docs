# Video Dilimle

Video Slice düğümü, bir videodan belirli bir bölümü çıkarmanızı sağlar. Videoyu kırpmak için bir başlangıç zamanı ve süre tanımlayabilir veya yalnızca başlangıç karelerini atlayabilirsiniz. İstenen süre kalan videodan daha uzunsa, düğüm mevcut olanı döndürebilir veya bir hata verebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kırpılacak giriş videosu. | VIDEO | Evet | - |
| `başlangıç zamanı` | Saniye cinsinden başlangıç zamanı (varsayılan: 0.0). | FLOAT | Hayır | -1e5 ila 1e5 |
| `süre` | Saniye cinsinden süre veya sınırsız süre için 0 (varsayılan: 0.0). | FLOAT | Hayır | 0.0 ve üzeri |
| `kesin süre` | True ise, belirtilen süre mümkün olmadığında bir hata oluşturulur (varsayılan: False). | BOOLEAN | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Kırpılmış video bölümü. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/tr.md)

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
