# LMS Örnekleyici

SamplerLMS düğümü, difüzyon modellerinde kullanılmak üzere bir En Küçük Ortalama Kareler (LMS) örnekleyici oluşturur. Örnekleme sürecinde kullanılabilen bir örnekleyici nesnesi üretir ve sayısal kararlılık ile doğruluk için LMS algoritmasının derecesini kontrol etmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `order` | LMS örnekleyici algoritması için derece parametresi; sayısal yöntemin doğruluğunu ve kararlılığını kontrol eder (varsayılan: 4; gelişmiş parametre) | INT | Evet | 1 to 100 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanılabilen yapılandırılmış bir LMS örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/tr.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
