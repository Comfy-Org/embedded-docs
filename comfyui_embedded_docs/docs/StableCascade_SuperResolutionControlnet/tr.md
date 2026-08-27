# StabilKaskad_SüperÇözünürlükKontrolAğı

StableCascade_SuperResolutionControlnet düğümü, Stable Cascade süper çözünürlük işlemi için girdileri hazırlar. Girdi görüntüsünü alır ve controlnet girdisi oluşturmak için bir VAE kullanarak kodlar; ayrıca Stable Cascade hattının C ve B aşamaları için yer tutucu latent temsiller üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Süper çözünürlük için işlenecek girdi görüntüsü. Kodlama için görüntünün yalnızca ilk 3 renk kanalı (RGB) kullanılır. | IMAGE | Evet | - |
| `vae` | Girdi görüntüsünü kodlamak için kullanılan VAE modeli | VAE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `kontrol_ağı_girişi` | Controlnet girdisi için uygun, VAE ile kodlanmış görüntü temsili | IMAGE |
| `aşama_c` | Stable Cascade işleminin C aşaması için yer tutucu (sıfır dolu) latent temsil; 16 kanallıdır ve boyutları girdi görüntü boyutunun 16'ya bölünmesine dayanır | LATENT |
| `aşama_b` | Stable Cascade işleminin B aşaması için yer tutucu (sıfır dolu) latent temsil; 4 kanallıdır ve boyutları girdi görüntü boyutunun 2'ye bölünmesine dayanır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
