# StabilKaskad_SüperÇözünürlükKontrolAğı

Bu düğüm, deneysel Stable Cascade grubunun bir parçasıdır. Bir girdi görüntüsünü VAE ile kodlayarak bir ControlNet girdisi oluşturur ve Stable Cascade işlem hattının C aşaması ile B aşaması için boş (sıfırlarla doldurulmuş) latent yer tutucuları üretir; böylece Stable Cascade süper çözünürlük işlemesi için girdileri hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Süper çözünürlük için işlenecek girdi görüntüsü. Kodlama için görüntünün yalnızca ilk 3 renk kanalı (RGB) kullanılır. | IMAGE | Evet | - |
| `vae` | Girdi görüntüsünü kodlamak için kullanılan VAE modeli | VAE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `controlnet_input` | ControlNet girdisi için uygun, VAE ile kodlanmış görüntü temsili | IMAGE |
| `stage_c` | Stable Cascade işlemesinin C aşaması için yer tutucu (sıfırlarla doldurulmuş) latent temsili; 16 kanallıdır ve boyutları girdi görüntü boyutunun 16'ya bölünmesine dayanır | LATENT |
| `stage_b` | Stable Cascade işlemesinin B aşaması için yer tutucu (sıfırlarla doldurulmuş) latent temsili; 4 kanallıdır ve boyutları girdi görüntü boyutunun 2'ye bölünmesine dayanır | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/tr.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
