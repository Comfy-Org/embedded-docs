> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/tr.md)

LatentUpscaleBy düğümü, görüntülerin gizli temsillerini büyütmek için tasarlanmıştır. Ölçek faktörünün ve büyütme yönteminin ayarlanmasına olanak tanıyarak, gizli örneklerin çözünürlüğünü artırmada esneklik sağlar.

## Girdiler

| Parametre     | Veri Tipi    | Açıklama |
|---------------|--------------|-------------|
| `örnekler`     | `LATENT`     | Büyütülecek görüntülerin gizli temsili. Bu parametre, büyütme işlemine tabi tutulacak girdi verisini belirlemede çok önemlidir. |
| `büyütme_yöntemi` | COMBO[STRING] | Gizli örnekleri büyütmek için kullanılan yöntemi belirtir. Yöntem seçimi, büyütülmüş çıktının kalitesini ve özelliklerini önemli ölçüde etkileyebilir. |
| `oranla_büyüt`    | `FLOAT`      | Gizli örneklerin hangi faktörle ölçekleneceğini belirler. Bu parametre, çıktının çözünürlüğünü doğrudan etkileyerek büyütme süreci üzerinde hassas kontrol sağlar. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Daha fazla işleme veya oluşturma görevleri için hazır olan büyütülmüş gizli temsil. Bu çıktı, oluşturulan görüntülerin çözünürlüğünü artırmak veya sonraki model işlemleri için gereklidir. |