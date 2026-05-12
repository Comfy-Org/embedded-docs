> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/tr.md)

VOIDInpaintConditioning düğümü, CogVideoX modelleriyle iç boyama (inpainting) için gereken koşullandırma verilerini hazırlar. Bir kaynak video ve ön işlenmiş dörtlü maskeyi (quadmask) alır, bunları VAE aracılığıyla kodlar ve modelin maskelenmiş alanları doldurmak için kullandığı 32 kanallı bir koşullandırma sinyalinde birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|----------|
| `positive` | CONDITIONING | Evet | - | İç boyama gizil (latent) bilgisiyle zenginleştirilecek pozitif koşullandırma |
| `negative` | VAE | Evet | - | İç boyama gizil (latent) bilgisiyle zenginleştirilecek negatif koşullandırma |
| `vae` | VAE | Evet | - | Maskeyi ve maskelenmiş videoyu gizil uzaya kodlamak için kullanılan VAE modeli |
| `video` | IMAGE | Evet | - | [T, Y, G, 3] formatında kaynak video kareleri |
| `quadmask` | MASK | Evet | - | VOIDQuadmaskPreprocess'ten [T, Y, G] formatında ön işlenmiş dörtlü maske |
| `width` | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK (adım: 8) | Video ve maskenin yeniden boyutlandırılacağı genişlik (varsayılan: 672) |
| `height` | INT | Evet | 16 - MAKS_ÇÖZÜNÜRLÜK (adım: 8) | Video ve maskenin yeniden boyutlandırılacağı yükseklik (varsayılan: 384) |
| `length` | INT | Evet | 1 - MAKS_ÇÖZÜNÜRLÜK (adım: 1) | İşlenecek piksel kare sayısı. CogVideoX-Fun-V1.5 (patch_size_t=2) için latent_t çift olmalıdır — tek latent_t üreten uzunluklar aşağı yuvarlanır (örn. 49 → 45) (varsayılan: 45) |
| `batch_size` | INT | Evet | 1 - 64 | Çıktı gürültü gizil (noise latent) için toplu iş boyutu (varsayılan: 1) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | İç boyama gizil bilgisi eklenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | İç boyama gizil bilgisi eklenmiş negatif koşullandırma |
| `latent` | LATENT | [batch_size, 16, latent_t, latent_h, latent_w] şeklinde sıfır dolu gürültü gizil tensörü |