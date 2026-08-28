# VAE ile Controlnet Uygula

Bu düğüm, Stable Diffusion 3 koşullandırmasına ControlNet rehberliği uygular. Pozitif ve negatif koşullandırma girdilerini, bir ControlNet modeli ve bir görüntü ile birlikte alır; ardından üretim sürecini etkilemek için ayarlanabilir güç ve zamanlama parametreleriyle kontrol rehberliğini uygular.

**Not:** Bu düğüm kullanımdan kaldırılmıştır (deprecated) ve gelecekteki sürümlerde kaldırılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | ControlNet rehberliğinin uygulanacağı pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | ControlNet rehberliğinin uygulanacağı negatif koşullandırma | CONDITIONING | Evet | - |
| `kontrol_ağı` | Rehberlik için kullanılacak ControlNet modeli | CONTROL_NET | Evet | - |
| `vae` | Süreçte kullanılan VAE modeli | VAE | Evet | - |
| `görüntü` | ControlNet'in rehberlik olarak kullanacağı girdi görüntüsü | IMAGE | Evet | - |
| `güç` | ControlNet etkisinin gücü (varsayılan: 1.0). 0.0 olarak ayarlandığında, düğüm ControlNet uygulamasını atlar ve koşullandırmayı değiştirmeden döndürür. | FLOAT | Evet | 0.0 - 10.0 |
| `başlangıç_yüzdesi` | ControlNet'in uygulanmaya başladığı üretim sürecindeki başlangıç noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `bitiş_yüzdesi` | ControlNet'in uygulanmayı bıraktığı üretim sürecindeki bitiş noktası (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** `strength` 0.0 olarak ayarlandığında, herhangi bir ControlNet rehberliği uygulanmaz ve girdi koşullandırması her iki çıktıya da değiştirilmeden iletilir.

**Not:** Aynı koşullandırma başka bir yerde yeniden kullanılıyorsa ve zaten kontrol bilgisi içeriyorsa, yeni ControlNet öncekinin ardına bağlanır; böylece birden fazla ControlNet sırayla uygulanabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | ControlNet rehberliği uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | ControlNet rehberliği uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/tr.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
