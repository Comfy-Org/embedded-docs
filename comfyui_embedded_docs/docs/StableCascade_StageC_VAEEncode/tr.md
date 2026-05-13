> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/tr.md)

StableCascade_StageC_VAEEncode düğümü, Stable Cascade modelleri için gizli temsiller oluşturmak amacıyla görüntüleri bir VAE kodlayıcı aracılığıyla işler. Bir giriş görüntüsü alır ve belirtilen VAE modelini kullanarak sıkıştırır, ardından iki gizli temsil çıktısı verir: biri C aşaması için, diğeri B aşaması için bir yer tutucu. Sıkıştırma parametresi, kodlamadan önce görüntünün ne kadar küçültüleceğini kontrol eder.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görüntü` | IMAGE | Evet | - | Gizli uzaya kodlanacak giriş görüntüsü |
| `vae` | VAE | Evet | - | Görüntüyü kodlamak için kullanılan VAE modeli |
| `sıkıştırma` | INT | Hayır | 4-128 | Kodlamadan önce görüntüye uygulanan sıkıştırma faktörü (varsayılan: 42) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `aşama_b` | LATENT | Stable Cascade modelinin C aşaması için kodlanmış gizli temsil |
| `stage_b` | LATENT | B aşaması için bir yer tutucu gizli temsil (şu anda sıfır döndürür) |

---
**Source fingerprint (SHA-256):** `e7b9bd83d263903567ab06c00324575e01b79b50881fa807cd6f006955935c63`
