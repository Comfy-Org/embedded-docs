> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/tr.md)

StableCascade_StageC_VAEEncode düğümü, görüntüleri bir VAE kodlayıcı aracılığıyla işleyerek Stable Cascade modelleri için gizli temsiller oluşturur. Bir girdi görüntüsü alır ve belirtilen VAE modelini kullanarak sıkıştırır, ardından biri C aşaması ve diğeri B aşaması için bir yer tutucu olmak üzere iki gizli temsil çıktılar. Sıkıştırma parametresi, görüntünün kodlanmadan önce ne kadar küçültüleceğini kontrol eder.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Gizli uzaya kodlanacak girdi görüntüsü |
| `vae` | VAE | Evet | - | Görüntüyü kodlamak için kullanılan VAE modeli |
| `compression` | INT | Hayır | 4-128 | Görüntü kodlanmadan önce uygulanan sıkıştırma faktörü (varsayılan: 42) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `stage_c` | LATENT | Stable Cascade modelinin C aşaması için kodlanmış gizli temsil |
| `stage_b` | LATENT | B aşaması için bir yer tutucu gizli temsil (şu anda sıfır değerler döndürür) |