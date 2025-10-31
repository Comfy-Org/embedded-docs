> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/tr.md)

HunyuanRefinerLatent düğümü, iyileştirme işlemleri için koşullandırma ve gizli girdileri işler. Gizli görüntü verilerini dahil ederken hem pozitif hem de negatif koşullandırmaya gürültü artırımı uygular ve daha fazla işleme için belirli boyutlarda yeni bir gizli çıktı üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | İşlenecek pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | İşlenecek negatif koşullandırma girdisi |
| `latent` | LATENT | Evet | - | Gizli temsil girdisi |
| `noise_augmentation` | FLOAT | Evet | 0.0 - 1.0 | Uygulanacak gürültü artırımı miktarı (varsayılan: 0.10) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Uygulanan gürültü artırımı ve gizli görüntü birleştirmesi ile işlenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Uygulanan gürültü artırımı ve gizli görüntü birleştirmesi ile işlenmiş negatif koşullandırma |
| `latent` | LATENT | [batch_size, 32, height, width, channels] boyutlarında yeni bir gizli çıktı |