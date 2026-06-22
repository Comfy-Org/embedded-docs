# VOIDInpaintConditioning

VOIDInpaintConditioning düğümü, CogVideoX modelleriyle iç boyama (inpainting) için gereken koşullandırma verilerini hazırlar. Bir kaynak video ve ön işlenmiş dörtlü maskeyi (quadmask) alır, bunları VAE aracılığıyla kodlar ve modelin maskelenmiş alanları doldurmak için kullandığı 32 kanallı bir koşullandırma sinyalinde birleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İç boyama gizli bilgisiyle zenginleştirilecek pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | İç boyama gizli bilgisiyle zenginleştirilecek negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Maskeyi ve maskelenmiş videoyu gizli uzaya kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `video` | Kaynak video kareleri [T, Y, X, 3] | IMAGE | Evet | - |
| `quadmask` | VOIDQuadmaskPreprocess'ten ön işlenmiş dörtlü maske [T, Y, X] | MASK | Evet | - |
| `width` | Video ve maskenin yeniden boyutlandırılacağı genişlik (varsayılan: 672) | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK (adım: 8) |
| `height` | Video ve maskenin yeniden boyutlandırılacağı yükseklik (varsayılan: 384) | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK (adım: 8) |
| `length` | İşlenecek piksel kare sayısı. CogVideoX-Fun-V1.5 (patch_size_t=2) için latent_t çift olmalıdır — tek latent_t üreten uzunluklar aşağı yuvarlanır (örn. 49 → 45) (varsayılan: 45) | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK (adım: 1) |
| `batch_size` | Çıktı gürültü gizli değişkeni için toplu iş boyutu (varsayılan: 1) | INT | Evet | 1 - 64 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `negative` | İç boyama gizli bilgisi eklenmiş pozitif koşullandırma | CONDITIONING |
| `latent` | İç boyama gizli bilgisi eklenmiş negatif koşullandırma | CONDITIONING |
| `latent` | [batch_size, 16, latent_t, latent_h, latent_w] şeklinde sıfır dolu gürültü gizli değişken tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
