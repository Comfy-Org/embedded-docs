# VOIDInpaintConditioning

VOIDInpaintConditioning düğümü, CogVideoX modelleriyle inpainting için gereken koşullandırma verilerini hazırlar. Bir kaynak video ve ön işlenmiş bir quadmask alır, bunları VAE üzerinden kodlar ve modelin maskelenmiş alanları doldurmak için kullandığı 32 kanallı bir koşullandırma sinyaline (maskeden 16 kanal + maskelenmiş videodan 16 kanal) birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Inpainting latent bilgisiyle zenginleştirilecek pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Inpainting latent bilgisiyle zenginleştirilecek negatif koşullandırma | CONDITIONING | Evet | - |
| `vae` | Maskeyi ve maskelenmiş videoyu latent uzayına kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `video` | Kaynak video kareleri [T, H, W, 3] | IMAGE | Evet | - |
| `quadmask` | VOIDQuadmaskPreprocess'ten ön işlenmiş quadmask [T, H, W] | MASK | Evet | - |
| `width` | Video ve maskenin yeniden boyutlandırılacağı genişlik (varsayılan: 672) | INT | Evet | 16 - MAX_RESOLUTION (adım: 8) |
| `height` | Video ve maskenin yeniden boyutlandırılacağı yükseklik (varsayılan: 384) | INT | Evet | 16 - MAX_RESOLUTION (adım: 8) |
| `length` | İşlenecek piksel kare sayısı. CogVideoX-Fun-V1.5 için (patch_size_t=2), latent_t çift olmalıdır — tek latent_t üreten uzunluklar aşağı yuvarlanır (örn. 49 → 45) (varsayılan: 45) | INT | Evet | 1 - MAX_RESOLUTION (adım: 1) |
| `batch_size` | Çıktı gürültü latentı için toplu iş boyutu (varsayılan: 1) | INT | Evet | 1 - 64 |

**Not:** CogVideoX-Fun-V1.5 `patch_size_t=2` kullandığından, kodlanan latentın çift zamansal boyutu olmalıdır. `length` tek bir `latent_t` üretecekse, düğüm bunu otomatik olarak en yakın geçerli değere aşağı yuvarlar ve bir uyarı günlüğe kaydeder. Tek `latent_t` kullanmak, dairesel dolgu yoluyla son kareyi bozar; bu da çözülen videonun sonunda görünür titremeye veya öznelerin kaybolmasına neden olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `positive` | Inpainting latent bilgisi eklenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Inpainting latent bilgisi eklenmiş negatif koşullandırma | CONDITIONING |
| `latent` | [batch_size, 16, latent_t, latent_h, latent_w] şeklinde sıfırlarla doldurulmuş gürültü latent tensörü | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
