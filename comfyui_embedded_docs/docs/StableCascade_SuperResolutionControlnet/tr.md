> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/tr.md)

StableCascade_SuperResolutionControlnet düğümü, Stable Cascade süper çözünürlük işleme için girdileri hazırlar. Bir girdi görüntüsünü alır ve kontrol ağı girdisi oluşturmak için bir VAE kullanarak kodlarken, aynı zamanda Stable Cascade işlem hattının C aşaması ve B aşaması için yer tutucu gizli temsiller de oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Süper çözünürlük için işlenecek girdi görüntüsü |
| `vae` | VAE | Evet | - | Girdi görüntüsünü kodlamak için kullanılan VAE modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | Kontrol ağı girdisi için uygun kodlanmış görüntü temsili |
| `stage_c` | LATENT | Stable Cascade işlemenin C aşaması için yer tutucu gizli temsil |
| `stage_b` | LATENT | Stable Cascade işlemenin B aşaması için yer tutucu gizli temsil |