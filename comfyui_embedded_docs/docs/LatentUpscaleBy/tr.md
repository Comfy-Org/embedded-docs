> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/tr.md)

LatentUpscaleBy düğümü, görüntülerin gizli (latent) temsillerini büyütmek için tasarlanmıştır. Ölçek faktörünün ve büyütme yönteminin ayarlanmasına olanak tanıyarak, gizli örneklerin çözünürlüğünü artırmada esneklik sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|---------------|--------------|-------------|
| `örnekler` | `LATENT` | Büyütülecek görüntülerin gizli temsilidir. Bu parametre, büyütme işlemine girecek giriş verilerini belirlemek için çok önemlidir. |
| `büyütme_yöntemi` | COMBO[STRING] | Gizli örnekleri büyütmek için kullanılan yöntemi belirtir. Yöntem seçimi, büyütülmüş çıktının kalitesini ve özelliklerini önemli ölçüde etkileyebilir. |
| `oranla_büyüt` | `FLOAT` | Gizli örneklerin hangi faktörle ölçeklendirileceğini belirler. Bu parametre, çıktının çözünürlüğünü doğrudan etkileyerek büyütme işlemi üzerinde hassas kontrol sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent` | `LATENT` | Daha ileri işleme veya üretim görevleri için hazır olan büyütülmüş gizli temsildir. Bu çıktı, oluşturulan görüntülerin çözünürlüğünü artırmak veya sonraki model işlemleri için gereklidir. |