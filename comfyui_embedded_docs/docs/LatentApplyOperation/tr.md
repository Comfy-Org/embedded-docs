# GizliİşlemUygula

LatentApplyOperation düğümü, belirtilen bir işlemi latent örneklere uygular. Girdi olarak latent verileri ve bir işlem alır, girdi latent örneklerini kopyalar, işlemi latent tensörüne uygular ve değiştirilmiş latent verileri döndürür. Bu düğüm, iş akışınızdaki latent temsilleri dönüştürmenize veya değiştirmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `samples` | İşlem tarafından işlenecek latent örnekler | LATENT | Evet | - |
| `operation` | Latent örneklere uygulanacak işlem | LATENT_OPERATION | Evet | - |

Not: Bu düğüm deneysel olarak işaretlenmiştir. İşlem, latent yapısının `samples` anahtarı altında depolanan latent tensörüne uygulanır. Girdi latent örnekleri, işlem uygulanmadan önce kopyalanır; böylece orijinal girdi latent verileri değiştirilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | İşlem uygulandıktan sonra değiştirilmiş latent örnekler | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/tr.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
