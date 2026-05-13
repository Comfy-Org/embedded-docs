> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet yönlendirmesi uygular. Pozitif ve negatif koşullandırma girdilerini bir ControlNet modeli ve görüntü ile birlikte alır, ardından üretim sürecini etkilemek için ayarlanabilir güç ve zamanlama parametreleriyle kontrol yönlendirmesini uygular.

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecekteki sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | ControlNet yönlendirmesinin uygulanacağı pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | ControlNet yönlendirmesinin uygulanacağı negatif koşullandırma |
| `kontrol_ağı` | CONTROL_NET | Evet | - | Yönlendirme için kullanılacak ControlNet modeli |
| `vae` | VAE | Evet | - | Süreçte kullanılan VAE modeli |
| `görüntü` | IMAGE | Evet | - | ControlNet'in yönlendirme olarak kullanacağı girdi görüntüsü |
| `güç` | FLOAT | Evet | 0.0 - 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmaya başladığı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | ControlNet'in uygulanmasının durduğu üretim sürecindeki bitiş noktası (varsayılan: 1.0) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `negatif` | CONDITIONING | ControlNet yönlendirmesi uygulanmış değiştirilmiş pozitif koşullandırma |
| `negatif` | CONDITIONING | ControlNet yönlendirmesi uygulanmış değiştirilmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
