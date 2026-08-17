# StabilKaskad_SüperÇözünürlükKontrolAğı

StableCascade_SuperResolutionControlnet düğümü, Stable Cascade süper çözünürlük işlemi için girdileri hazırlar. Bir girdi görüntüsü alır ve controlnet girdisi oluşturmak için bunu bir VAE kullanarak kodlar; ayrıca Stable Cascade işlem hattının C aşaması ve B aşaması için yer tutucu latent temsiller üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Süper çözünürlük için işlenecek girdi görüntüsü | IMAGE | Evet | - |
| `vae` | Girdi görüntüsünü kodlamak için kullanılan VAE modeli | VAE | Evet | - |

Not: VAE ile kodlama sırasında girdi görüntüsünün yalnızca ilk üç renk kanalı kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `controlnet_input` | Controlnet girdisi için uygun kodlanmış görüntü temsili | IMAGE |
| `stage_c` | Stable Cascade işleminin C aşaması için yer tutucu latent temsil; boyutları, girdi görüntüsü boyutunun 16'ya bölünmesine dayanır | LATENT |
| `stage_b` | Stable Cascade işleminin B aşaması için yer tutucu latent temsil; boyutları, girdi görüntüsü boyutunun 2'ye bölünmesine dayanır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
