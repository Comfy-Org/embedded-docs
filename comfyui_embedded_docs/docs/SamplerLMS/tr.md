SamplerLMS düğümü, difüzyon modellerinde kullanılmak üzere bir En Küçük Kareler Ortalaması (LMS) örnekleyicisi oluşturur. Örnekleme sürecinde kullanılabilecek bir örnekleyici nesnesi üretir ve sayısal kararlılık ile doğruluk için LMS algoritmasının sırasını kontrol etmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sıra` | LMS örnekleyici algoritması için sıra parametresi; sayısal yöntemin doğruluğunu ve kararlılığını kontrol eder (varsayılan: 4) | INT | Evet | 1 ile 100 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilecek yapılandırılmış bir LMS örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/tr.md)

---
**Source fingerprint (SHA-256):** `0c045ef15890fe611dc0b9d455bafa313d28373a29c881a0c8bf5d80e69bc114`
