> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maske ile birleştirerek boyama görevleri için ControlNet koşullandırması uygular. Girdi görüntüsünü ve maskeyi işleyerek, üretim sürecini yönlendiren ve görüntünün hangi alanlarının boyanacağı üzerinde hassas kontrol sağlayan değiştirilmiş koşullandırma oluşturur. Düğüm, ControlNet'in etkisini üretim sürecinin farklı aşamalarında ince ayar yapmak için güç ayarlaması ve zamanlama kontrollerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma |
| `negatif` | CONDITIONING | Evet | - | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `kontrol_ağı` | CONTROL_NET | Evet | - | Üretim üzerinde ek kontrol sağlayan ControlNet modeli |
| `vae` | VAE | Evet | - | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Varyasyonel Otokodlayıcı) |
| `görüntü` | IMAGE | Evet | - | ControlNet için kontrol kılavuzu olarak hizmet veren girdi görüntüsü |
| `maske` | MASK | Evet | - | Görüntünün hangi alanlarının boyanması gerektiğini tanımlayan maske |
| `güç` | FLOAT | Evet | 0.0 - 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `başlangıç_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | ControlNet etkisinin üretim sırasında başladığı başlangıç noktası (yüzde olarak) (varsayılan: 0.0) |
| `bitiş_yüzdesi` | FLOAT | Evet | 0.0 - 1.0 | ControlNet etkisinin üretim sırasında durduğu bitiş noktası (yüzde olarak) (varsayılan: 1.0) |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işlemeden önce görüntüye uygulanır ve maske, ControlNet'e gönderilen ek birleştirme verilerine dahil edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `negatif` | CONDITIONING | Boyama için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma |
| `negatif` | CONDITIONING | Boyama için ControlNet uygulanmış değiştirilmiş negatif koşullandırma |