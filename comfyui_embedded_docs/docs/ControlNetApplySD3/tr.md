# VAE ile Controlnet Uygula

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet yönlendirmesi uygular. Pozitif ve negatif koşullandırma girdilerini bir ControlNet modeli ve görüntü ile birlikte alır, ardından üretim sürecini etkilemek için ayarlanabilir güç ve zamanlama parametreleriyle kontrol yönlendirmesini uygular.

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecekteki sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | ControlNet yönlendirmesinin uygulanacağı pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | ControlNet yönlendirmesinin uygulanacağı negatif koşullandırma | CONDITIONING | Evet | - |
| `kontrol_ağı` | Yönlendirme için kullanılacak ControlNet modeli | CONTROL_NET | Evet | - |
| `vae` | Süreçte kullanılan VAE modeli | VAE | Evet | - |
| `görüntü` | ControlNet'in yönlendirme olarak kullanacağı girdi görüntüsü | IMAGE | Evet | - |
| `güç` | ControlNet etkisinin gücü (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `başlangıç_yüzdesi` | ControlNet'in uygulanmaya başladığı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | ControlNet'in uygulanmasının durduğu üretim sürecindeki bitiş noktası (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | ControlNet yönlendirmesi uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | ControlNet yönlendirmesi uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
