# VOIDInpaintConditioning

VOIDInpaintConditioning düğümü, CogVideoX modelleriyle inpainting için gereken koşullandırma verilerini hazırlar. Kaynak videoyu ve ön işlenmiş quadmask'ı alır, bunları VAE aracılığıyla kodlar ve modelin maskelenmiş alanları doldurmak için kullandığı 32 kanallı bir koşullandırma sinyalinde (maskeden 16 kanal + maskeli videodan 16 kanal) birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Inpainting latent bilgisiyle artırılacak pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Inpainting latent bilgisiyle artırılacak negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Maskeyi ve maskeli videoyu latent uzayına kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `video` | Kaynak video kareleri [T, H, W, 3] | IMAGE | Evet | - |
| `quadmask` | VOIDQuadmaskPreprocess'ten ön işlenmiş quadmask [T, H, W] | MASK | Evet | - |
| `width` | Videonun ve maskenin yeniden boyutlandırılacağı genişlik (varsayılan: 672) | INT | Evet | 16 to MAX_RESOLUTION (step: 8) |
| `height` | Videonun ve maskenin yeniden boyutlandırılacağı yükseklik (varsayılan: 384) | INT | Evet | 16 to MAX_RESOLUTION (step: 8) |
| `length` | İşlenecek piksel kare sayısı. CogVideoX-Fun-V1.5 için (patch_size_t=2), latent_t çift olmalıdır; tek latent_t üreten uzunluklar aşağı yuvarlanır (ör. 49 → 45) (varsayılan: 45) | INT | Evet | 1 to MAX_RESOLUTION (step: 1) |
| `batch_size` | Çıktıdaki gürültü latenti için batch boyutu (varsayılan: 1) | INT | Evet | 1 ile 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Inpainting latent bilgisi eklenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Inpainting latent bilgisi eklenmiş negatif koşullandırma | CONDITIONING |
| `latent` | [batch_size, 16, latent_t, latent_h, latent_w] boyutlu, sıfırlarla doldurulmuş bir gürültü latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
