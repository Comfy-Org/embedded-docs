> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/tr.md)

HunyuanVideo15SuperResolution düğümü, bir video süper çözünürlük işlemi için koşullandırma verilerini hazırlar. Bir video temsilinin gizli (latent) gösterimini ve isteğe bağlı olarak bir başlangıç görüntüsünü alır; bunları gürültü artırma ve CLIP görüntü verileriyle birlikte, bir model tarafından daha yüksek çözünürlüklü bir çıktı üretmek için kullanılabilecek bir formata paketler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | Yok | Gizli ve artırma verileriyle değiştirilecek olumlu koşullandırma girdisi. |
| `negative` | CONDITIONING | Evet | Yok | Gizli ve artırma verileriyle değiştirilecek olumsuz koşullandırma girdisi. |
| `vae` | VAE | Hayır | Yok | İsteğe bağlı `start_image`'ı kodlamak için kullanılan VAE. `start_image` sağlanmışsa gereklidir. |
| `start_image` | IMAGE | Hayır | Yok | Süper çözünürlüğü yönlendirmek için isteğe bağlı bir başlangıç görüntüsü. Sağlanırsa, yükseltilir ve koşullandırma gizli alanına kodlanır. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Hayır | Yok | Koşullandırmaya eklemek için isteğe bağlı CLIP görüntü yerleştirmeleri. |
| `latent` | LATENT | Evet | Yok | Koşullandırmaya dahil edilecek olan girdi gizli video temsili. |
| `noise_augmentation` | FLOAT | Hayır | 0.0 - 1.0 | Koşullandırmaya uygulanacak gürültü artırmanın gücü (varsayılan: 0.70). |

**Not:** Bir `start_image` sağlarsanız, onun kodlanabilmesi için bir `vae` de bağlamanız gerekir. `start_image`, girdi `latent`'ın gerektirdiği boyutlarla eşleşecek şekilde otomatik olarak yükseltilecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Değiştirilmiş olumlu koşullandırma; artık birleştirilmiş gizli alan, gürültü artırma ve isteğe bağlı CLIP görüntü verilerini içerir. |
| `negative` | CONDITIONING | Değiştirilmiş olumsuz koşullandırma; artık birleştirilmiş gizli alan, gürültü artırma ve isteğe bağlı CLIP görüntü verilerini içerir. |
| `latent` | LATENT | Girdi gizli alanı değişmeden iletilir. |
