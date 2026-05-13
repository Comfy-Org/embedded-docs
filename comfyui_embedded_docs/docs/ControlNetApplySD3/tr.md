> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet yönlendirmesi uygular. Pozitif ve negatif koşullandırma girdilerini bir ControlNet modeli ve görüntü ile birlikte alır, ardından üretim sürecini etkilemek için ayarlanabilir güç ve zamanlama parametreleriyle kontrol yönlendirmesini uygular.

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecekteki sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | ControlNet yönlendirmesinin uygulanacağı pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | ControlNet yönlendirmesinin uygulanacağı negatif koşullandırma |
| `control_net` | CONTROL_NET | Evet | - | Yönlendirme için kullanılacak ControlNet modeli |
| `vae` | VAE | Evet | - | Süreçte kullanılan VAE modeli |
| `image` | IMAGE | Evet | - | ControlNet'in yönlendirme olarak kullanacağı girdi görüntüsü |
| `strength` | FLOAT | Evet | 0.0 - 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmaya başladığı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmasının durduğu üretim sürecindeki bitiş noktası (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `positive` | CONDITIONING | ControlNet yönlendirmesi uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | ControlNet yönlendirmesi uygulanmış değiştirilmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
