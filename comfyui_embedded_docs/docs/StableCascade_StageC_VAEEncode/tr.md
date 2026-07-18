StableCascade_StageC_VAEEncode düğümü, Stable Cascade modelleri için gizli temsiller oluşturmak amacıyla görüntüleri bir VAE kodlayıcı aracılığıyla işler. Bir giriş görüntüsü alır ve belirtilen VAE modelini kullanarak sıkıştırır, ardından iki gizli temsil çıktısı verir: biri C aşaması için, diğeri B aşaması için bir yer tutucu. Sıkıştırma parametresi, kodlamadan önce görüntünün ne kadar küçültüleceğini kontrol eder.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Gizli uzaya kodlanacak giriş görüntüsü | IMAGE | Evet | - |
| `vae` | Görüntüyü kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `sıkıştırma` | Kodlamadan önce görüntüye uygulanan sıkıştırma faktörü (varsayılan: 42) | INT | Hayır | 4-128 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `aşama_c` | Stable Cascade modelinin C aşaması için kodlanmış gizli temsil | LATENT |
| `aşama_b` | B aşaması için bir yer tutucu gizli temsil (şu anda sıfır döndürür) | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/tr.md)

---
**Source fingerprint (SHA-256):** `e7b9bd83d263903567ab06c00324575e01b79b50881fa807cd6f006955935c63`
