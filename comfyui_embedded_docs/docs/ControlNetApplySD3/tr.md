> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet kılavuzluğu uygular. Pozitif ve negatif koşullandırma girdilerini, bir ControlNet modeli ve görüntü ile birlikte alır, ardından üretim sürecini etkilemek için ayarlanabilir güç ve zamanlama parametreleriyle kontrol kılavuzluğunu uygular.

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecek sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | ControlNet kılavuzluğunun uygulanacağı pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | ControlNet kılavuzluğunun uygulanacağı negatif koşullandırma |
| `kontrol_ağı` | CONTROL_NET | Evet | - | Kılavuzluk için kullanılacak ControlNet modeli |
| `vae` | VAE | Evet | - | Süreçte kullanılan VAE modeli |
| `görüntü` | IMAGE | Evet | - | ControlNet'in kılavuz olarak kullanacağı girdi görüntüsü |
| `güç` | FLOAT | Evet | 0.0 - 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmaya başlayacağı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmayı durduracağı üretim sürecindeki bitiş noktası (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | ControlNet kılavuzluğu uygulanmış değiştirilmiş pozitif koşullandırma |
| `negatif` | CONDITIONING | ControlNet kılavuzluğu uygulanmış değiştirilmiş negatif koşullandırma |