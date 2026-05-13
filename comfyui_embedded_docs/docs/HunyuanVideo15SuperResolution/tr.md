> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/tr.md)

HunyuanVideo15SuperResolution düğümü, bir video süper çözünürlük işlemi için koşullama (conditioning) verilerini hazırlar. Bir videonun gizli (latent) temsilini ve isteğe bağlı olarak bir başlangıç görüntüsünü alır; bunları gürültü artırımı (noise augmentation) ve CLIP görsel verileriyle birlikte, bir model tarafından daha yüksek çözünürlüklü bir çıktı üretmek için kullanılabilecek bir formata paketler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | Yok | Gizli (latent) ve artırım (augmentation) verileriyle değiştirilecek pozitif koşullama girişi. |
| `negative` | CONDITIONING | Evet | Yok | Gizli (latent) ve artırım (augmentation) verileriyle değiştirilecek negatif koşullama girişi. |
| `vae` | VAE | Hayır | Yok | İsteğe bağlı `start_image`'i kodlamak için kullanılan VAE. `start_image` sağlanmışsa gereklidir. |
| `start_image` | IMAGE | Hayır | Yok | Süper çözünürlüğü yönlendirmek için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, yükseltilir (upscale) ve koşullama gizli (latent) değişkenine kodlanır. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | Yok | Koşullamaya eklenecek isteğe bağlı CLIP görsel yerleştirmeleri (embeddings). |
| `latent` | LATENT | Evet | Yok | Koşullamaya dahil edilecek giriş gizli (latent) video temsili. |
| `noise_augmentation` | FLOAT | Hayır | 0.0 - 1.0 | Koşullamaya uygulanacak gürültü artırımının (noise augmentation) gücü (varsayılan: 0.70). |

**Not:** Bir `start_image` sağlarsanız, kodlanması için bir `vae` de bağlamanız gerekir. `start_image`, giriş `latent` tarafından belirtilen boyutlarla eşleşecek şekilde otomatik olarak yükseltilecektir (upscale).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `positive` | CONDITIONING | Artık birleştirilmiş gizli (latent), gürültü artırımı (noise augmentation) ve isteğe bağlı CLIP görsel verilerini içeren değiştirilmiş pozitif koşullama. |
| `negative` | CONDITIONING | Artık birleştirilmiş gizli (latent), gürültü artırımı (noise augmentation) ve isteğe bağlı CLIP görsel verilerini içeren değiştirilmiş negatif koşullama. |
| `latent` | LATENT | Giriş gizli (latent) değişkeni değiştirilmeden iletilir. |

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
