> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maske ile birleştirerek, iç boyama (inpainting) görevleri için ControlNet koşullandırması uygular. Giriş görüntüsünü ve maskeyi işleyerek, görüntünün hangi alanlarının boyanacağı üzerinde hassas kontrol sağlayan, üretim sürecini yönlendiren değiştirilmiş koşullandırma oluşturur. Düğüm, ControlNet'in üretim sürecinin farklı aşamalarındaki etkisini ince ayarlamak için güç ayarı ve zamanlama kontrollerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `control_net` | CONTROL_NET | Evet | - | Üretim üzerinde ek kontrol sağlayan ControlNet modeli |
| `vae` | VAE | Evet | - | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Değişken Otomatik Kodlayıcı) |
| `image` | IMAGE | Evet | - | ControlNet için kontrol kılavuzu görevi gören giriş görüntüsü |
| `mask` | MASK | Evet | - | Görüntünün hangi alanlarının boyanması gerektiğini tanımlayan maske |
| `strength` | FLOAT | Evet | 0.0 ila 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `start_percent` | FLOAT | Evet | 0.0 ila 1.0 | ControlNet etkisinin üretim sırasında başladığı başlangıç noktası (yüzde olarak) (varsayılan: 0.0) |
| `end_percent` | FLOAT | Evet | 0.0 ila 1.0 | ControlNet etkisinin üretim sırasında durduğu bitiş noktası (yüzde olarak) (varsayılan: 1.0) |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işlemeden önce görüntüye uygulanır; ayrıca maske, ControlNet'e gönderilen ek birleştirme verilerine dahil edilir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | İç boyama için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | İç boyama için ControlNet uygulanmış değiştirilmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
