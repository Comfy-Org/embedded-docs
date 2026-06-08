ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maske ile birleştirerek, iç boyama (inpainting) görevleri için ControlNet koşullandırması uygular. Giriş görüntüsünü ve maskeyi işleyerek, görüntünün hangi alanlarının boyanacağı üzerinde hassas kontrol sağlayan, üretim sürecini yönlendiren değiştirilmiş koşullandırma oluşturur. Düğüm, ControlNet'in üretim sürecinin farklı aşamalarındaki etkisini ince ayarlamak için güç ayarı ve zamanlama kontrollerini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `kontrol_ağı` | Üretim üzerinde ek kontrol sağlayan ControlNet modeli | CONTROL_NET | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Değişken Otomatik Kodlayıcı) | VAE | Evet | - |
| `görüntü` | ControlNet için kontrol kılavuzu görevi gören giriş görüntüsü | IMAGE | Evet | - |
| `maske` | Görüntünün hangi alanlarının boyanması gerektiğini tanımlayan maske | MASK | Evet | - |
| `güç` | ControlNet etkisinin gücü (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 10.0 |
| `başlangıç_yüzdesi` | ControlNet etkisinin üretim sırasında başladığı başlangıç noktası (yüzde olarak) (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `bitiş_yüzdesi` | ControlNet etkisinin üretim sırasında durduğu bitiş noktası (yüzde olarak) (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işlemeden önce görüntüye uygulanır; ayrıca maske, ControlNet'e gönderilen ek birleştirme verilerine dahil edilir.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | İç boyama için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | İç boyama için ControlNet uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
