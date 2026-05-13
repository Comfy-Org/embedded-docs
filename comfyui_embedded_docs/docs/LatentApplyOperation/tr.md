> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/tr.md)

**LatentApplyOperation** düğümü, latent örneklere belirtilen bir işlemi uygular. Girdi olarak latent verileri ve bir işlem alır, sağlanan işlemi kullanarak latent örnekleri işler ve değiştirilmiş latent verilerini döndürür. Bu düğüm, iş akışınızda latent temsilleri dönüştürmenize veya manipüle etmenize olanak tanır.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `örnekler` | LATENT | Evet | - | İşlem tarafından işlenecek latent örnekler |
| `işlem` | LATENT_OPERATION | Evet | - | Latent örneklere uygulanacak işlem |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | LATENT | İşlem uygulandıktan sonra değiştirilmiş latent örnekler |

---
**Source fingerprint (SHA-256):** `77147b480fe8cb48eb26a31f6f0c7bc038e07d26e628ebe361861394946d8678`
