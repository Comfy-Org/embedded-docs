# GizliİşlemUygula

**LatentApplyOperation** düğümü, latent örneklere belirtilen bir işlemi uygular. Girdi olarak latent verileri ve bir işlem alır, sağlanan işlemi kullanarak latent örnekleri işler ve değiştirilmiş latent verilerini döndürür. Bu düğüm, iş akışınızda latent temsilleri dönüştürmenize veya manipüle etmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | İşlem tarafından işlenecek latent örnekler | LATENT | Evet | - |
| `işlem` | Latent örneklere uygulanacak işlem | LATENT_OPERATION | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | İşlem uygulandıktan sonra değiştirilmiş latent örnekler | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/tr.md)

---
**Source fingerprint (SHA-256):** `77147b480fe8cb48eb26a31f6f0c7bc038e07d26e628ebe361861394946d8678`
