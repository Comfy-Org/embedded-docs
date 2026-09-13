# Tohum

Seed düğümü, diğer düğümlerdeki rastgele işlemlerin yeniden üretilebilirliğini kontrol etmek için tohum olarak kullanılabilecek bir tam sayı değeri sağlar. Tutarlı bir başlangıç değeri sağlayarak, gerektiğinde üretilen sonuçların yinelenebilir kalmasına yardımcı olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `seed` | Kullanılacak tohum değeri. Üretim sonrası kontrol seçeneği, değerin sabit kalıp kalmayacağını veya her üretimden sonra değişip değişmeyeceğini belirler; bu düğümde sabit olarak ayarlanmıştır. | INT | Evet | 0 ile 9223372036854775807 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `seed` | Üretilen tohum değeri. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/tr.md)

---
**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`
