# VOIDInpaintConditioning

VOIDInpaintConditioning düğümü, CogVideoX modelleriyle inpainting için gereken koşullandırma verilerini hazırlar. Bir kaynak video ve ön işlenmiş bir kuadmask alır, bunları VAE aracılığıyla kodlar ve modelin maskelenmiş alanları doldurmak için kullandığı 32 kanallı bir koşullandırma sinyalinde (16 kanal maske + 16 kanal maskelenmiş video) birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İnpainting latent bilgisiyle genişletilecek pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | İnpainting latent bilgisiyle genişletilecek negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Maskeyi ve maskelenmiş videoyu latent uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `video` | Kaynak video kareleri [T, H, W, 3] | IMAGE | Evet | - |
| `quadmask` | VOIDQuadmaskPreprocess'ten ön işlenmiş kuadmask [T, H, W] | MASK | Evet | - |
| `width` | Video ve maskenin yeniden boyutlandırılacağı genişlik (varsayılan: 672) | INT | Evet | 16 ila MAX_RESOLUTION (adım: 8) |
| `height` | Video ve maskenin yeniden boyutlandırılacağı yükseklik (varsayılan: 384) | INT | Evet | 16 ila MAX_RESOLUTION (adım: 8) |
| `length` | İşlenecek piksel kare sayısı. CogVideoX-Fun-V1.5 (patch_size_t=2) için latent_t çift olmalıdır — tek latent_t üreten uzunluklar aşağı yuvalanır (örn. 49 → 45) (varsayılan: 45) | INT | Evet | 1 ila MAX_RESOLUTION (adım: 1) |
| `batch_size` | Çıktı gürültü latenti için grup boyutu (varsayılan: 1) | INT | Evet | 1 ila 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | İnpainting latent bilgisi eklenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | İnpainting latent bilgisi eklenmiş negatif koşullandırma | CONDITIONING |
| `latent` | [batch_size, 16, latent_t, latent_h, latent_w] şeklinde sıfırlarla doldurulmuş gürültü latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
