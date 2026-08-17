# VAE ile Controlnet Uygula

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet rehberliği uygular. Pozitif ve negatif koşullandırma girdilerini bir ControlNet modeli ve görüntüsüyle birlikte alır, ardından ayarlanabilir güç ve zamanlama parametreleriyle kontrol rehberliğini uygulayarak üretim sürecini etkiler.

**Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecek sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | ControlNet rehberliğinin uygulanacağı pozitif koşullandırma | CONDITIONING | Yes | - |
| `negative` | ControlNet rehberliğinin uygulanacağı negatif koşullandırma | CONDITIONING | Yes | - |
| `control_net` | Rehberlik için kullanılacak ControlNet modeli | CONTROL_NET | Yes | - |
| `vae` | İşlemde kullanılan VAE modeli | VAE | Yes | - |
| `image` | ControlNet'in rehberlik olarak kullanacağı girdi görüntüsü | IMAGE | Yes | - |
| `strength` | ControlNet efektinin gücü (varsayılan: 1.0) | FLOAT | Yes | 0.0 - 10.0 |
| `start_percent` | ControlNet'in uygulanmaya başladığı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) | FLOAT | Yes | 0.0 - 1.0 |
| `end_percent` | ControlNet'in uygulanmasının sona erdiği üretim sürecindeki bitiş noktası (varsayılan: 1.0) | FLOAT | Yes | 0.0 - 1.0 |

**Not:** `strength` 0 olarak ayarlandığında, düğüm ControlNet'i uygulamadan pozitif ve negatif koşullandırmayı değiştirmeden döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | ControlNet rehberliği uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative` | ControlNet rehberliği uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
