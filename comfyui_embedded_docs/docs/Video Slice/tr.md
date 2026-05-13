> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/tr.md)

Video Slice düğümü, bir videodan belirli bir bölümü çıkarmanızı sağlar. Videoyu kırpmak için bir başlangıç zamanı ve süre tanımlayabilir veya yalnızca başlangıç karelerini atlayabilirsiniz. İstenen süre kalan videodan daha uzunsa, düğüm mevcut olanı döndürebilir veya bir hata verebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Kırpılacak giriş videosu. |
| `start_time` | FLOAT | Hayır | -1e5 ila 1e5 | Saniye cinsinden başlangıç zamanı (varsayılan: 0.0). |
| `duration` | FLOAT | Hayır | 0.0 ve üzeri | Saniye cinsinden süre veya sınırsız süre için 0 (varsayılan: 0.0). |
| `strict_duration` | BOOLEAN | Hayır | - | True ise, belirtilen süre mümkün olmadığında bir hata oluşturulur (varsayılan: False). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Kırpılmış video bölümü. |

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
