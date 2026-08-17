# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution düğümü, video süper çözünürlük süreci için koşullandırma verilerini hazırlar. Bir videonun latent temsilini ve isteğe bağlı olarak bir başlangıç görüntüsünü alır; bunları bir gürültü artırma değeri ve isteğe bağlı CLIP vision verileriyle birlikte, bir modelin daha yüksek çözünürlüklü bir çıktı üretmek için kullanabileceği bir biçimde paketler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Birleştirilmiş latent ve gürültü artırma verileriyle değiştirilecek pozitif koşullandırma girdisi. | CONDITIONING | Evet | N/A |
| `negative` | Birleştirilmiş latent ve gürültü artırma verileriyle değiştirilecek negatif koşullandırma girdisi. | CONDITIONING | Evet | N/A |
| `vae` | İsteğe bağlı `start_image` görüntüsünü kodlamak için kullanılan VAE. `start_image` sağlanmışsa gereklidir. | VAE | Hayır | N/A |
| `start_image` | Süper çözünürlük sürecini yönlendiren isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, ölçeği büyütülür, `vae` ile kodlanır ve koşullandırma latenti'nin başına yerleştirilir. | IMAGE | Hayır | N/A |
| `clip_vision_output` | İsteğe bağlı CLIP vision gömme vektörleri. Sağlandığında, hem pozitif hem de negatif koşullandırmaya eklenir. | CLIP_VISION_OUTPUT | Hayır | N/A |
| `latent` | Koşullandırmaya dahil edilecek latent video temsili. | LATENT | Evet | N/A |
| `noise_augmentation` | Koşullandırmaya uygulanacak gürültü artırmanın gücü (varsayılan: 0.70). Bu gelişmiş bir parametredir. | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |

**Not:** Bir `start_image` sağlarsanız, kodlanması için bir `vae` de bağlamanız gerekir. `start_image`, girdi `latent` tarafından ima edilen boyutlara uyacak şekilde otomatik olarak ölçeği büyütülür ve VAE tarafından yalnızca ilk üç renk kanalı (RGB) kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Birleştirilmiş latent, gürültü artırma ve isteğe bağlı CLIP vision verilerini artık içeren değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Birleştirilmiş latent, gürültü artırma ve isteğe bağlı CLIP vision verilerini artık içeren değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Girdi latent, değiştirilmeden olduğu gibi iletilir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/tr.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
