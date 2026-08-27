# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution düğümü, video süper çözünürlük süreci için koşullandırma verilerini hazırlar. Bir videonun latent temsilini ve isteğe bağlı olarak bir başlangıç görüntüsünü alır; bunları gürültü artırımı ve CLIP görüş verileriyle birlikte, bir modelin daha yüksek çözünürlüklü çıktı üretmek için kullanabileceği bir biçimde paketler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Latent ve artırım verileriyle değiştirilecek pozitif koşullandırma girdisi. | CONDITIONING | Evet | N/A |
| `negatif` | Latent ve artırım verileriyle değiştirilecek negatif koşullandırma girdisi. | CONDITIONING | Evet | N/A |
| `vae` | İsteğe bağlı `start_image` görüntüsünü kodlamak için kullanılan VAE. `start_image` sağlanırsa gereklidir. | VAE | Hayır | N/A |
| `başlangıç_görseli` | Süper çözünürlük sürecini yönlendirmek için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, büyütülür ve koşullandırma latentine kodlanır. | IMAGE | Hayır | N/A |
| `clip_vision_output` | Koşullandırmaya eklenecek isteğe bağlı CLIP görüş yerleştirmeleri. | CLIP_VISION_OUTPUT | Hayır | N/A |
| `latent` | Koşullandırmaya dahil edilen girdi latent video temsili. | LATENT | Evet | N/A |
| `gürültü_artırımı` | Koşullandırmaya uygulanacak gürültü artırımının gücü (varsayılan: 0.70). Bu, gelişmiş bir parametredir. | FLOAT | Hayır | 0.0 - 1.0 (step 0.01) |

**Not:** Bir `start_image` sağlarsanız, kodlanabilmesi için bir `vae` de bağlamanız gerekir. `start_image`, girdi `latent`inin uzamsal boyutlarının (genişlik ve yükseklik) 16 katına otomatik olarak büyütülür, ardından kodlanır ve koşullandırma latentine yerleştirilir. Kodlama için `start_image`in yalnızca RGB kanalları kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Birleştirilmiş latent, gürültü artırımı ve isteğe bağlı CLIP görüş verilerini artık içeren değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negatif` | Birleştirilmiş latent, gürültü artırımı ve isteğe bağlı CLIP görüş verilerini artık içeren değiştirilmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Girdi latent, değiştirilmeden olduğu gibi iletilir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/tr.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
