> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/tr.md)

VOIDInpaintConditioning düğümü, CogVideoX modelleriyle iç boyama (inpainting) için gereken koşullandırma verilerini hazırlar. Bir kaynak video ve ön işlenmiş dörtlü maskeyi (quadmask) alır, bunları VAE aracılığıyla kodlar ve modelin maskelenmiş alanları doldurmak için kullandığı 32 kanallı bir koşullandırma sinyalinde birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | İç boyama gizli bilgisiyle zenginleştirilecek pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | İç boyama gizli bilgisiyle zenginleştirilecek negatif koşullandırma |
| `vae` | VAE | Evet | - | Maskeyi ve maskelenmiş videoyu gizli uzaya kodlamak için kullanılan VAE modeli |
| `video` | IMAGE | Evet | - | Kaynak video kareleri [T, Y, X, 3] |
| `quadmask` | MASK | Evet | - | VOIDQuadmaskPreprocess'ten ön işlenmiş dörtlü maske [T, Y, X] |
| `width` | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK (adım: 8) | Video ve maskenin yeniden boyutlandırılacağı genişlik (varsayılan: 672) |
| `height` | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK (adım: 8) | Video ve maskenin yeniden boyutlandırılacağı yükseklik (varsayılan: 384) |
| `length` | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK (adım: 1) | İşlenecek piksel kare sayısı. CogVideoX-Fun-V1.5 (patch_size_t=2) için latent_t çift olmalıdır — tek latent_t üreten uzunluklar aşağı yuvarlanır (örn. 49 → 45) (varsayılan: 45) |
| `batch_size` | INT | Evet | 1 - 64 | Çıktı gürültü gizli değişkeni için toplu iş boyutu (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | İç boyama gizli bilgisi eklenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | İç boyama gizli bilgisi eklenmiş negatif koşullandırma |
| `latent` | LATENT | [batch_size, 16, latent_t, latent_h, latent_w] şeklinde sıfır dolu gürültü gizli değişken tensörü |

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
