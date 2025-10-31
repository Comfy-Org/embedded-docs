> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet kılavuzluğu uygular. Pozitif ve negatif koşullandırma girdilerini, bir ControlNet modeli ve görüntü ile birlikte alır, ardından üretim sürecini etkilemek için ayarlanabilir güç ve zamanlama parametreleriyle kontrol kılavuzluğunu uygular.

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecek sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | ControlNet kılavuzluğunun uygulanacağı pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | ControlNet kılavuzluğunun uygulanacağı negatif koşullandırma |
| `control_net` | CONTROL_NET | Evet | - | Kılavuzluk için kullanılacak ControlNet modeli |
| `vae` | VAE | Evet | - | Süreçte kullanılan VAE modeli |
| `image` | IMAGE | Evet | - | ControlNet'in kılavuz olarak kullanacağı girdi görüntüsü |
| `strength` | FLOAT | Evet | 0.0 - 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmaya başlayacağı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmayı durduracağı üretim sürecindeki bitiş noktası (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | ControlNet kılavuzluğu uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | ControlNet kılavuzluğu uygulanmış değiştirilmiş negatif koşullandırma |