# GizliİşlemUygula

LatentApplyOperation düğümü, belirtilen bir latent işlemini latent örneklere uygular. Girdi olarak latent verisi ve bir işlem alır, sağlanan işlemi kullanarak latent örnekleri işler ve değiştirilmiş latent verisini döndürür. Bu düğüm, iş akışınızda latent temsilleri dönüştürmenize veya değiştirmenize olanak tanır. Bu düğüm şu anda deneysel olarak işaretlenmiştir.

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
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
