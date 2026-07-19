# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution düğümü, bir video süper çözünürlük işlemi için koşullama (conditioning) verilerini hazırlar. Bir videonun gizli (latent) temsilini ve isteğe bağlı olarak bir başlangıç görüntüsünü alır; bunları gürültü artırımı (noise augmentation) ve CLIP görsel verileriyle birlikte, bir model tarafından daha yüksek çözünürlüklü bir çıktı üretmek için kullanılabilecek bir formata paketler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Gizli (latent) ve artırım (augmentation) verileriyle değiştirilecek pozitif koşullama girişi. | CONDITIONING | Evet | Yok |
| `negatif` | Gizli (latent) ve artırım (augmentation) verileriyle değiştirilecek negatif koşullama girişi. | CONDITIONING | Evet | Yok |
| `vae` | İsteğe bağlı `başlangıç_görseli`'i kodlamak için kullanılan VAE. `başlangıç_görseli` sağlanmışsa gereklidir. | VAE | Hayır | Yok |
| `başlangıç_görseli` | Süper çözünürlüğü yönlendirmek için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, yükseltilir (upscale) ve koşullama gizli (latent) değişkenine kodlanır. | IMAGE | Hayır | Yok |
| `clip_vision_output` | Koşullamaya eklenecek isteğe bağlı CLIP görsel yerleştirmeleri (embeddings). | CLIP_VISION_OUTPUT | Hayır | Yok |
| `latent` | Koşullamaya dahil edilecek giriş gizli (latent) video temsili. | LATENT | Evet | Yok |
| `gürültü_artırımı` | Koşullamaya uygulanacak gürültü artırımının (noise augmentation) gücü (varsayılan: 0.70). | FLOAT | Hayır | 0.0 - 1.0 |

**Not:** Bir `start_image` sağlarsanız, kodlanması için bir `vae` de bağlamanız gerekir. `start_image`, giriş `latent` tarafından belirtilen boyutlarla eşleşecek şekilde otomatik olarak yükseltilecektir (upscale).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Artık birleştirilmiş gizli (latent), gürültü artırımı (noise augmentation) ve isteğe bağlı CLIP görsel verilerini içeren değiştirilmiş pozitif koşullama. | CONDITIONING |
| `negatif` | Artık birleştirilmiş gizli (latent), gürültü artırımı (noise augmentation) ve isteğe bağlı CLIP görsel verilerini içeren değiştirilmiş negatif koşullama. | CONDITIONING |
| `latent` | Giriş gizli (latent) değişkeni değiştirilmeden iletilir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/tr.md)

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
