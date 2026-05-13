> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maske ile birleştirerek, iç boyama (inpainting) görevleri için ControlNet koşullandırması uygular. Giriş görüntüsünü ve maskeyi işleyerek, görüntünün hangi alanlarının boyanacağı üzerinde hassas kontrol sağlayan, üretim sürecini yönlendiren değiştirilmiş koşullandırma oluşturur. Düğüm, ControlNet'in üretim sürecinin farklı aşamalarındaki etkisini ince ayarlamak için güç ayarı ve zamanlama kontrollerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `kontrol_ağı` | CONTROL_NET | Evet | - | Üretim üzerinde ek kontrol sağlayan ControlNet modeli |
| `vae` | VAE | Evet | - | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Değişken Otomatik Kodlayıcı) |
| `görüntü` | IMAGE | Evet | - | ControlNet için kontrol kılavuzu görevi gören giriş görüntüsü |
| `maske` | MASK | Evet | - | Görüntünün hangi alanlarının boyanması gerektiğini tanımlayan maske |
| `güç` | FLOAT | Evet | 0.0 ila 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 ila 1.0 | ControlNet etkisinin üretim sırasında başladığı başlangıç noktası (yüzde olarak) (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 ila 1.0 | ControlNet etkisinin üretim sırasında durduğu bitiş noktası (yüzde olarak) (varsayılan: 1.0) |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işlemeden önce görüntüye uygulanır; ayrıca maske, ControlNet'e gönderilen ek birleştirme verilerine dahil edilir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `pozitif` | CONDITIONING | İç boyama için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma |
| `negatif` | CONDITIONING | İç boyama için ControlNet uygulanmış değiştirilmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
