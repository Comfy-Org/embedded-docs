> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/tr.md)

SamplerLMS düğümü, difüzyon modellerinde kullanılmak üzere bir En Küçük Kareler Ortalaması (LMS) örnekleyicisi oluşturur. Örnekleme sürecinde kullanılabilecek bir örnekleyici nesnesi üretir ve sayısal kararlılık ile doğruluk için LMS algoritmasının sırasını kontrol etmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `sıra` | INT | Evet | 1 ile 100 | LMS örnekleyici algoritması için sıra parametresi; sayısal yöntemin doğruluğunu ve kararlılığını kontrol eder (varsayılan: 4) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `sampler` | SAMPLER | Örnekleme hattında kullanılabilecek yapılandırılmış bir LMS örnekleyici nesnesi |

---
**Source fingerprint (SHA-256):** `0c045ef15890fe611dc0b9d455bafa313d28373a29c881a0c8bf5d80e69bc114`
